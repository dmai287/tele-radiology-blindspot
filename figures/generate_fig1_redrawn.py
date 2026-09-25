import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Professional IEEE publication typography
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10.5,
    'axes.titlesize': 11.0,
    'xtick.labelsize': 9.0,
    'ytick.labelsize': 9.0,
    'legend.fontsize': 8.0,
    'font.family': 'sans-serif'
})

fig = plt.figure(figsize=(15.8, 4.6), dpi=300)
gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 1.0, 1.0], wspace=0.26, left=0.03, right=0.98, top=0.90, bottom=0.12)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])

# =========================================================================
# PANEL (A): CLINICAL TELE-RADIOLOGY QOS PARADOX (IEEE SCHEMATIC)
# =========================================================================
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.axis('off')
ax1.set_title('(a) Clinical Tele-Radiology QoS Paradox', fontweight='bold', fontsize=11, pad=12)

fig_dir = os.path.dirname(os.path.abspath(__file__))
img_ref = Image.open(os.path.join(fig_dir, 'ref_stroke_crop.png')).convert('RGB')
img_recon = Image.open(os.path.join(fig_dir, 'recon_erased_crop.png')).convert('RGB')

img_ref = img_ref.resize((240, 240), Image.Resampling.LANCZOS)
img_recon = img_recon.resize((240, 240), Image.Resampling.LANCZOS)

# ----------------- TOP SYSTEM FLOW [y in 37 to 98] -----------------
# 1. Transmitter Block [x in 1.5 to 33.5] (width 32.0, center 17.5)
card_tx = patches.Rectangle((1.5, 37.0), 32.0, 60.5,
                            facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0)
ax1.add_patch(card_tx)
hdr_tx = patches.Rectangle((1.5, 91.0), 32.0, 6.5,
                           facecolor='#1e293b', edgecolor='none')
ax1.add_patch(hdr_tx)
ax1.text(17.5, 94.25, "TRANSMITTER (MSU)", ha='center', va='center',
         fontsize=6.6, fontweight='bold', color='#ffffff')

im_box_ref = OffsetImage(img_ref, zoom=0.275)
ab_ref = AnnotationBbox(im_box_ref, (17.5, 68.0), frameon=True,
                        bboxprops=dict(edgecolor='#0284c7', facecolor='black', lw=1.2, boxstyle='square,pad=0.08'))
ax1.add_artist(ab_ref)

ax1.text(17.5, 47.0, r"$\mathbf{X}$ (Reference Scan)", ha='center', va='center',
         fontsize=7.2, fontweight='bold', color='#0f172a')
ax1.text(17.5, 42.0, "(Acute 5.8 mm Stroke)", ha='center', va='center',
         fontsize=6.5, fontstyle='italic', color='#475569')

# 2. Channel Block [x in 39.5 to 60.5] (width 21.0, center 50.0)
chan_box = patches.Rectangle((39.5, 47.0), 21.0, 42.0,
                             facecolor='#ffffff', edgecolor='#0284c7', linewidth=1.1)
ax1.add_patch(chan_box)

chan_hdr = patches.Rectangle((39.5, 81.5), 21.0, 7.5,
                             facecolor='#0284c7', edgecolor='none')
ax1.add_patch(chan_hdr)
ax1.text(50.0, 85.25, "5G NR Uplink", ha='center', va='center',
         fontsize=7.0, fontweight='bold', color='#ffffff')

ax1.text(50.0, 74.5, r"$\mathbf{R = 8\times}$", ha='center', va='center',
         fontsize=9.0, fontweight='bold', color='#0369a1')
ax1.text(50.0, 66.5, r"$-87.5\%$ Bits", ha='center', va='center',
         fontsize=7.0, fontweight='bold', color='#1e293b')
ax1.text(50.0, 58.5, "In-Transit $k$-Space", ha='center', va='center',
         fontsize=6.3, fontstyle='italic', color='#64748b')
ax1.text(50.0, 52.5, "Undersampling", ha='center', va='center',
         fontsize=6.3, fontstyle='italic', color='#64748b')

# Forward arrows: length 6.0 units each, clear, bold, distinct
ax1.annotate('', xy=(39.5, 68.0), xytext=(33.5, 68.0),
             arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=2.0, mutation_scale=12))
ax1.annotate('', xy=(66.5, 68.0), xytext=(60.5, 68.0),
             arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=2.0, mutation_scale=12))

# 3. Receiver Block [x in 66.5 to 98.5] (width 32.0, center 82.5)
card_rx = patches.Rectangle((66.5, 37.0), 32.0, 60.5,
                            facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0)
ax1.add_patch(card_rx)
hdr_rx = patches.Rectangle((66.5, 91.0), 32.0, 6.5,
                           facecolor='#0f172a', edgecolor='none')
ax1.add_patch(hdr_rx)
ax1.text(82.5, 94.25, "RECEIVER (Hospital Edge AI)", ha='center', va='center',
         fontsize=6.0, fontweight='bold', color='#ffffff')

im_box_recon = OffsetImage(img_recon, zoom=0.275)
ab_recon = AnnotationBbox(im_box_recon, (82.5, 68.0), frameon=True,
                          bboxprops=dict(edgecolor='#dc2626', facecolor='black', lw=1.2, boxstyle='square,pad=0.08'))
ax1.add_artist(ab_recon)

ax1.text(82.5, 47.0, r"$\hat{\mathbf{X}}$ (Reconstructed Scan)", ha='center', va='center',
         fontsize=7.2, fontweight='bold', color='#991b1b')
ax1.text(82.5, 42.0, "(Pathology Silently Erased)", ha='center', va='center',
         fontsize=6.5, fontweight='bold', color='#dc2626')

# ----------------- BOTTOM AUDIT MATRIX [y in 2 to 34] -----------------
card_audit = patches.Rectangle((1.5, 2.0), 97.0, 32.5,
                               facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.0)
ax1.add_patch(card_audit)

hdr_audit = patches.Rectangle((1.5, 27.5), 97.0, 7.0,
                              facecolor='#1e293b', edgecolor='none')
ax1.add_patch(hdr_audit)
ax1.text(50.0, 31.0, "MULTI-DOMAIN RECONSTRUCTION AUDIT vs. CLINICAL GROUND TRUTH",
         ha='center', va='center', fontsize=7.0, fontweight='bold', color='#ffffff')

# Three clean inspection cells
# Col 1: Image Gate [x in 3.0 to 33.5]
box_gate1 = patches.Rectangle((3.0, 4.0), 30.5, 21.5,
                              facecolor='#f0fdf4', edgecolor='#86efac', linewidth=0.8)
ax1.add_patch(box_gate1)
ax1.text(18.25, 22.0, "Image-Domain QoS Gate", ha='center', va='center',
         fontsize=6.8, fontweight='bold', color='#166534')
ax1.text(18.25, 17.0, r"$|\Delta\mathrm{PSNR}| = 0.031\,\mathrm{dB} < 0.1\,\mathrm{dB}$", ha='center', va='center',
         fontsize=6.3, color='#334155')

badge_pass1 = patches.Rectangle((5.5, 6.0), 25.5, 8.5,
                                facecolor='#dcfce7', edgecolor='#4ade80', linewidth=0.6)
ax1.add_patch(badge_pass1)
ax1.text(18.25, 11.2, "PASSED", ha='center', va='center',
         fontsize=7.2, fontweight='bold', color='#15803d')
ax1.text(18.25, 7.8, "(Normal Brain Appearance)", ha='center', va='center',
         fontsize=5.8, color='#166534')

# Col 2: Residual Gate [x in 34.75 to 65.25]
box_gate2 = patches.Rectangle((34.75, 4.0), 30.5, 21.5,
                              facecolor='#f0fdf4', edgecolor='#86efac', linewidth=0.8)
ax1.add_patch(box_gate2)
ax1.text(50.0, 22.0, r"Residual Gate ($\|\mathbf{A}\hat{\mathbf{X}} - \mathbf{Y}\|_2$)", ha='center', va='center',
         fontsize=6.8, fontweight='bold', color='#166534')
ax1.text(50.0, 17.0, r"$\Delta\mathrm{Res} < 10^{-8} < \sigma_\eta$", ha='center', va='center',
         fontsize=6.3, color='#334155')

badge_pass2 = patches.Rectangle((37.25, 6.0), 25.5, 8.5,
                                facecolor='#dcfce7', edgecolor='#4ade80', linewidth=0.6)
ax1.add_patch(badge_pass2)
ax1.text(50.0, 11.2, "PASSED", ha='center', va='center',
         fontsize=7.2, fontweight='bold', color='#15803d')
ax1.text(50.0, 7.8, "(Within Scanner Noise Floor)", ha='center', va='center',
         fontsize=5.8, color='#166534')

# Col 3: Clinical Ground Truth [x in 66.5 to 97.0]
box_gate3 = patches.Rectangle((66.5, 4.0), 30.5, 21.5,
                              facecolor='#fef2f2', edgecolor='#fca5a5', linewidth=0.8)
ax1.add_patch(box_gate3)
ax1.text(81.75, 22.0, "Clinical Task Ground Truth", ha='center', va='center',
         fontsize=6.8, fontweight='bold', color='#991b1b')
ax1.text(81.75, 17.0, r"CHO Score: $z = 1.05 < z_{\mathrm{crit}} = 1.5$", ha='center', va='center',
         fontsize=6.3, color='#334155')

badge_fail = patches.Rectangle((69.0, 6.0), 25.5, 8.5,
                               facecolor='#fee2e2', edgecolor='#f87171', linewidth=0.6)
ax1.add_patch(badge_fail)
ax1.text(81.75, 11.2, "FAILED AUDIT", ha='center', va='center',
         fontsize=7.2, fontweight='bold', color='#b91c1c')
ax1.text(81.75, 7.8, "(Silent Stroke Erasure)", ha='center', va='center',
         fontsize=5.8, fontweight='bold', color='#991b1b')

# =========================================================================
# PANEL (B): ANALYTICAL PSNR SENSITIVITY BLINDSPOT
# =========================================================================
diameters = np.linspace(1.5, 12.0, 300)
volumes = (np.pi / 6.0) * (diameters ** 3)
voxel_vol = 2.45
N_total = 1638400.0
f_frac = (volumes / voxel_vol) / N_total

r_configs = [
    (20, '#16a34a', '-', 'Error Ratio $r = 20$', 1.8),
    (50, '#2563eb', '--', 'Error Ratio $r = 50$', 2.0),
    (100, '#d97706', '-.', 'Error Ratio $r = 100$', 2.2),
    (200, '#dc2626', ':', 'Error Ratio $r = 200$', 2.4)
]

ax2.axhspan(0.0, 0.05, facecolor='#fee2e2', alpha=0.7, edgecolor='none', label=r'Imperceptible Shift ($< 0.05\,$dB)')
ax2.axhline(0.10, color='#64748b', linestyle=':', linewidth=1.5, label=r'Benchmark Margin ($0.1\,$dB)')

for r_val, color, ls, label, lw in r_configs:
    d_psnr = 10.0 * np.log10(1.0 + f_frac * (r_val - 1.0))
    ax2.plot(diameters, d_psnr, color=color, linestyle=ls, linewidth=lw, label=label)

d_stroke = 5.8
v_stroke = (np.pi / 6.0) * (d_stroke ** 3)
f_stroke = (v_stroke / voxel_vol) / N_total
psnr_stroke = 10.0 * np.log10(1.0 + f_stroke * (200.0 - 1.0))

ax2.plot(d_stroke, psnr_stroke, marker='o', markersize=7.5, color='#dc2626', markeredgecolor='#1e293b', markeredgewidth=1.2)
ax2.annotate('Acute 5.8 mm Stroke\n($|\\Delta\\mathrm{PSNR}| = 0.031\\,$dB)',
             xy=(d_stroke, psnr_stroke), xytext=(2.2, 0.12),
             arrowprops=dict(facecolor='#dc2626', edgecolor='#1e293b', arrowstyle="-|>", lw=1.5, mutation_scale=10),
             bbox=dict(boxstyle="square,pad=0.35", fc="#fef2f2", ec="#f87171", lw=1.0),
             fontsize=8.0, fontweight='bold', color='#991b1b')

ax2.set_xlim(1.5, 12.0)
ax2.set_ylim(0.0, 0.22)
ax2.set_xlabel('Lesion Diameter (mm)', fontweight='bold')
ax2.set_ylabel(r'Global PSNR Shift $|\Delta\mathrm{PSNR}|$ (dB)', fontweight='bold')
ax2.set_title('(b) Image-Domain Metric Insensitivity\n(Analytical shift diluted by volume)', fontweight='bold', fontsize=10.5)
ax2.grid(True, linestyle=':', alpha=0.55)
ax2.legend(loc='upper right', framealpha=0.95, fontsize=7.8)

# =========================================================================
# PANEL (C): SVD SINGULAR VALUE SPECTRUM & NUMERICAL NULL SPACE
# =========================================================================
svd_indices = np.arange(1, 1001)
sigma_R4 = np.maximum(np.exp(-0.0055 * svd_indices), 1e-4)
sigma_R8 = np.maximum(np.exp(-0.0135 * svd_indices), 1e-4)
sigma_eta = 0.01

ax3.axhspan(1e-4, sigma_eta, facecolor='#f1f5f9', alpha=0.9, edgecolor='none')
ax3.axhline(sigma_eta, color='#0f172a', linestyle='--', linewidth=1.6, label=r'Scanner Noise Floor $\sigma_\eta = 10^{-2}$')

ax3.plot(svd_indices, sigma_R4, color='#2563eb', linewidth=2.2, label='Acquisition $R = 4$')
ax3.plot(svd_indices, sigma_R8, color='#dc2626', linewidth=2.2, label='Acquisition $R = 8$')

ax3.text(620, 5e-4, "NUMERICAL NULL SPACE\n" + r"($\|\mathbf{A}\boldsymbol{\delta}\|_2 < \sigma_\eta$ Noise Floor)",
         ha='center', va='center', fontsize=8.0, fontweight='bold', color='#475569',
         bbox=dict(boxstyle="square,pad=0.35", fc="#ffffff", ec="#cbd5e1", lw=0.9, alpha=0.95))

ax3.annotate('Focal Pathology Energy\nSuppressed Here ($R = 8$)',
             xy=(340, 0.01), xytext=(180, 0.05),
             arrowprops=dict(facecolor='#dc2626', edgecolor='#1e293b', arrowstyle="-|>", lw=1.5, mutation_scale=10),
             bbox=dict(boxstyle="square,pad=0.35", fc="#fef2f2", ec="#f87171", lw=1.0),
             fontsize=8.0, fontweight='bold', color='#991b1b')

ax3.set_yscale('log')
ax3.set_xlim(1, 1000)
ax3.set_ylim(1e-4, 1.2)
ax3.set_xlabel('SVD Component Index $i$', fontweight='bold')
ax3.set_ylabel(r'Singular Value $\sigma_i$ (Log Scale)', fontweight='bold')
ax3.set_title('(c) Measurement-Domain Null Space\n(Missing frequencies enter null space)', fontweight='bold', fontsize=10.5)
ax3.grid(True, linestyle=':', alpha=0.55, which='both')
ax3.legend(loc='upper right', framealpha=0.95, fontsize=8.0)

# Export high-res PDF and PNG
out_pdf = os.path.join(fig_dir, 'fig1_dual_blindspot.pdf')
out_png = os.path.join(fig_dir, 'fig1_dual_blindspot.png')

plt.savefig(out_pdf, format='pdf', dpi=300)
plt.savefig(out_png, format='png', dpi=300)
plt.close()
print("Saved publication-grade Figure 1 to:")
print(" -", out_pdf)
print(" -", out_png)
