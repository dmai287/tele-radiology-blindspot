#!/usr/bin/env python
"""
Fig. 6 (case study): one real counterfactual pair from the audit, reconstructed with the audit's own code.

Case  : file_brain_AXFLAIR_200_6002588, slice 9 (fastMRI brain, multi-coil FLAIR), 64 mm^3 lesion at
        (row 276, col 213), contrast +1.5, equispaced mask, R = 8. This is one of the 3,960 released pairs
        (data/exp1_classical_R468.csv); the audit labelled it silently erased under zero-filled reconstruction
        (z_ref 8.27 -> z_recon 1.73) and detected under CG-SENSE (z_recon 4.53).
Input : the case's data-pack file (case.npz from the Causal Safety Audit counterfactual pack, val/case04), which
        holds the sampled lines of both arms, the 32 fully sampled centre lines, the references and the lesion.
        fastMRI data are covered by the fastMRI data-use agreement and are not redistributed here.
Code  : the csa-audit package (https://github.com/dmai287/csa-audit): ESPIRiT maps from the centre lines with the
        audit's parameters, ZeroFilled and CGSense (lam = 1e-2, tol 1e-5, 80 iterations, as `cg_sense_tuned`).
        The script re-computes PSNR and the relative residual and checks them against the released row.

Usage : python figures/generate_fig6_case.py --case <pack>/val/case04_AXFLAIR_64mm3_cp150/case.npz --csa <csa-audit repo>
"""
import argparse
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DEF_CSA = os.path.join(VAULT, "Causal Safety Audit - Paper 2", "github_repo")
DEF_CASE = os.path.join(DEF_CSA, "outputs", "csa_pack_multisplit", "val", "case04_AXFLAIR_64mm3_cp150", "case.npz")
RELEASED = {  # data/exp1_classical_R468.csv, contrast 1.5, R = 8
    "zero_filled": dict(psnr_f=25.30033, psnr_cf=25.246174, res_f=0.160603, res_cf=0.160461, z=1.731129),
    "cg_sense_tuned": dict(psnr_f=28.072629, psnr_cf=28.004983, res_f=0.133483, res_cf=0.13332, z=4.52624),
}
Z_REF = 8.269519


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", default=DEF_CASE)
    ap.add_argument("--csa", default=DEF_CSA)
    ap.add_argument("--out", default=HERE)
    a = ap.parse_args()
    sys.path.insert(0, a.csa)
    from csa.metrics.image import center_crop, psnr
    from csa.physics.espirit import espirit_maps
    from csa.physics.operator import SenseOperator
    from csa.recon.base import CGSense, ZeroFilled

    z = np.load(a.case, allow_pickle=True)
    meta = json.loads(str(z["meta"]))
    C, (H, W) = meta["n_coils"], meta["image_shape"]
    mask = z["mask"]
    y = np.zeros((C, H, W), np.complex128)
    y_cf = np.zeros((C, H, W), np.complex128)
    y[:, :, mask] = z["kspace_sampled_lesion_absent"]
    y_cf[:, :, mask] = z["kspace_sampled_lesion_present"]
    calib = np.zeros((C, H, W), np.complex64)
    lo = int(z["calibration_first_line"])
    calib[:, :, lo:lo + meta["calibration_lines"]] = z["calibration_kspace"]
    maps = espirit_maps(calib).astype(np.complex128)
    X = z["reference_lesion_absent"].astype(np.complex128)
    X_cf = z["reference_lesion_present"].astype(np.complex128)
    ell = z["lesion"].astype(np.complex128)
    op = SenseOperator(maps, mask)

    recs = {"zero_filled": ZeroFilled(), "cg_sense_tuned": CGSense(lam=1e-2, tol=1e-5, maxiter=80)}
    out = {}
    crop = lambda v: center_crop(v, 320)  # noqa: E731
    maxval = float(np.abs(crop(X)).max())
    print(f"{'model':16s} {'PSNR f':>8s} {'PSNR cf':>8s} {'res f':>8s} {'res cf':>8s}   released")
    for name, rec in recs.items():
        xh, xh_cf = rec(y, mask, maps), rec(y_cf, mask, maps)
        out[name] = (xh, xh_cf)
        m = dict(psnr_f=psnr(crop(X), crop(xh), maxval=maxval), psnr_cf=psnr(crop(X_cf), crop(xh_cf), maxval=maxval),
                 res_f=op.relative_residual(xh, y), res_cf=op.relative_residual(xh_cf, y_cf))
        r = RELEASED[name]
        print(f"{name:16s} {m['psnr_f']:8.3f} {m['psnr_cf']:8.3f} {m['res_f']:8.5f} {m['res_cf']:8.5f}   "
              f"{r['psnr_f']:.3f} {r['psnr_cf']:.3f} {r['res_f']:.5f} {r['res_cf']:.5f}")
        out[name + "_metrics"] = m

    # ---- figure ---------------------------------------------------------------------------------
    sr, sc = meta["lesion"]["site_row"], meta["lesion"]["site_col"]
    rad = meta["lesion"]["radius_px"]
    hr, hc = 44, 44
    r0, r1 = sr - hr, sr + hr
    c1 = min(W, sc + 16)
    c0 = c1 - 2 * hc
    win = lambda v: np.abs(v[r0:r1, c0:c1])  # noqa: E731
    vmax = np.percentile(win(X_cf), 99.7)
    zf, zf_cf = out["zero_filled"]
    cg, cg_cf = out["cg_sense_tuned"]
    tr = win(zf_cf - zf)
    lv = win(ell)
    tmax = lv.max()
    mz, mc = out["zero_filled_metrics"], out["cg_sense_tuned_metrics"]
    panels = [
        (win(X_cf), "gray", vmax, "(a) Reference", f"z = {Z_REF:.1f}"),
        (win(cg_cf), "gray", vmax, "(b) CG-SENSE, R = 8", f"z = {RELEASED['cg_sense_tuned']['z']:.1f}"),
        (win(zf_cf), "gray", vmax, "(c) Zero-filled, R = 8", f"z = {RELEASED['zero_filled']['z']:.1f}"),
        (tr, "magma", tmax, "(d) Transfer in (c)", None),
        (lv, "magma", tmax, "(e) Inserted lesion", None),
    ]
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Arial", "DejaVu Sans"],
                         "font.size": 7.5, "pdf.fonttype": 42})
    fig, axs = plt.subplots(1, 5, figsize=(7.0, 1.56))
    for ax, (img, cmap, vm, title, note) in zip(axs, panels):
        ax.imshow(img, cmap=cmap, vmin=0, vmax=vm, interpolation="nearest")
        ax.set_title(title, fontsize=7.5, pad=3)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.add_patch(Circle((sc - c0, sr - r0), 3.2 * rad, fill=False, ec="#e8412c", lw=0.9, ls="--"))
        if note:
            ax.text(0.04, 0.04, note, transform=ax.transAxes, color="white", fontsize=7, fontweight="bold",
                    va="bottom", ha="left", bbox=dict(boxstyle="round,pad=0.15", fc="black", ec="none", alpha=0.55))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.88, bottom=0.01, wspace=0.05)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(a.out, f"fig6_real_case.{ext}"), dpi=300)
    print("wrote", os.path.join(a.out, "fig6_real_case.{pdf,png}"))
    print(f"zero-filled: dPSNR {mz['psnr_f'] - mz['psnr_cf']:.3f} dB, residual {100 * (mz['res_cf'] / mz['res_f'] - 1):+.2f} %")
    print(f"CG-SENSE   : dPSNR {mc['psnr_f'] - mc['psnr_cf']:.3f} dB, residual {100 * (mc['res_cf'] / mc['res_f'] - 1):+.2f} %")


if __name__ == "__main__":
    main()
