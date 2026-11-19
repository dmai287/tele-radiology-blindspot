# ICOIN 2027 camera-ready: changes and submission checklist

Paper: *Silent Stroke Loss in Tele-Radiology: The Network QoS Illusion* (EDAS, ICOIN 2027, Nha Trang, 13–15 Jan 2027).
Build: `latexmk -pdf main.tex` → `main.pdf`, **6 pages** (limit 6), US Letter, no bookmarks, no link annotations.

## 1. How each reviewer comment was addressed

| # | Reviewer comment | Change in the camera-ready |
|---|---|---|
| R1-1 | Section I presents numerical results before background, problem statement and method | Introduction rewritten: clinical background → communication bottleneck → problem statement → four qualitative contributions → paper organization. All numbers removed from the contribution list. Paper reordered: II System Model + two propositions (new "System Model" subsection with the end-to-end pipeline) → III Proposed CSA + four-layer architecture (DARDO, URLLC, S-NACK) → IV Results (Table I, DARDO, Table II, case study, latency, limitations) → V Conclusion. DARDO is now defined *before* its results appear. |
| R1-2 | References [5] and [7] could not be verified | Both were unverifiable and have been **removed**: [5] Hossain & Muhammad, "5G-enabled secure healthcare framework for IoMT", *IEEE Network* 2020 (no such paper found); [7] Chundugari et al., *IEEE Access* 2024 (no such paper found). Replaced by two verified IEEE Access papers: Ahad, Tahir & Yau 2019 (vol. 7, pp. 100747–100762) and Mahmeen et al. 2021 (vol. 9, pp. 102899–102907). |
| R1-3 | Global SSIM is 0.866 for R=4, 6, 8 while PSNR drops ~4 dB | This was a **transcription error** in Table I, not a plateau. `scripts/reproduce_tables.py` on `data/exp1_classical_R468.csv` gives SSIM = 0.846 / 0.801 / 0.760 (Fig. 3a already plotted the correct values). Table I corrected; a new row "lesion-induced \|ΔSSIM\|" (1–2 × 10⁻⁴) was added, and the text now explains that PSNR *and* SSIM decline smoothly with R while the lesion-induced shift stays negligible (the actual point of Proposition 1). |
| R1-4 | Index terms IoMT and AI Safety never appear; QoS missing | Index terms are now: Tele-radiology, Quality of Service (QoS), Rate-Distortion Optimization, Deep Learning Reconstruction, Edge AI, Model Observer, Silent Erasure, 5G URLLC. Every term appears in the body. |
| R1-5 | Reference [15] not cited | Removed (`latif2021ai`). Also removed the never-cited `muckley2021results`. |
| R1-6 | R defined as both acceleration factor and compression factor | R is defined once (Introduction, repeated in the system model) as the **acceleration factor**; "compression factor" no longer appears. Payload reduction is stated as 1 − 1/R. Table III row renamed "Acceleration Factor". |
| R1-7 | Follow IEEE bibliographic abbreviations | All journal names abbreviated per IEEE style (IEEE Trans. Med. Imag., IEEE Trans. Image Process., IEEE Commun. Surveys Tuts., Proc. Natl. Acad. Sci. USA, Magn. Reson. Med., Lancet Neurol., Amer. J. Neuroradiol.). MICCAI entry converted to `@inproceedings` ("in Proc. … (MICCAI), 2020, pp. 64–73"). |
| R3 | Evaluation relies on simulated lesions; network-level claims require validation | New subsection IV-G "Limitations and Future Work" (simulated spherical lesions; CHO vs. reader study; reconstruction scope; Layers 3–4 budgeted analytically, not measured). Abstract and conclusion now say DARDO's gain is a *projection*. |

## 2. Reference corrections beyond R1-2 (all verified 16 Nov 2026)

* `fassbender2017mobile`: real title is "Mobile stroke units for prehospital thrombolysis, triage, and beyond: Benefits and challenges", *Lancet Neurol.* **16**(3), 227–237 (was 16(11), 938–950 with a wrong title).
* `lang2024ultrafast` ("Ultrafast sub-two-minute brain MRI protocols…", Radiology 310(2) e231500) does not exist. Replaced by the two real papers it conflated: Altmann et al., *Radiology* 310(2):e231938, 2024 (DL-reconstructed ultrafast stroke MRI) and Lang et al., *AJNR* 45(4):379–385, 2024 (2-minute ultrafast protocol).
* `zhang2022semantic`: published in *Engineering* 8(1):60–73, 2022 with 11 authors (was listed as IEEE Commun. Mag. with a wrong author list).
* `al2020internet` (Al-Turjman & Baali): real but year/volume were wrong (2022, vol. 33) and it did not support the sentence it was cited for; removed.
* Added `saver2006time` (Stroke 37:263–266) for "two million neurons per minute" and `3gpp23501` (TS 23.501) for the 5QI classes.
* `fassbender2017mobile` and `altmann2024ultrafast` author first names were taken from the publisher record; `lang2024twominute` is "M. Lang et al." because only the first and senior authors were confirmed.

## 3. Data-integrity findings that changed the wording (please confirm you agree)

These came from reading `data/` and `scripts/` while fixing the SSIM row. Each is reversible, but the camera-ready is final, so decide now.

1. **DARDO numbers are projections, not measurements.** `scripts/benchmark_full_dardo.py` never reconstructs with a DARDO mask; it computes the task-spectral-energy fraction captured by the DARDO vs. equispaced mask and *rescales* each pair's measured z-loss by it. The paper now calls these "first-order projections" (Table I caption, Sec. IV-C, Table III "0.0% (projected)" (was 1.89 %, see item 6), abstract, conclusion, limitations). The old text called them empirical results of "3,960 physical audits".
2. **No VarNet in the released data.** `exp1_classical_R468.csv` contains only `cg_sense_tuned` and `zero_filled` (1,980 pairs each). The setup now says "zero-filled and CG-SENSE … with a learned-prior reconstruction examined qualitatively (Fig. 4)". If a VarNet run exists outside the repo, add it to `data/` and restore the claim.
3. **"Mean z_recon" row** in the old Table I (1.74 / 1.41 / 1.05) matched neither the overall mean (1.47 / 1.35 / 1.12) nor the 64 mm³ values (1.74 / 1.51 / 1.05). The row now shows the overall mean, conventional / projected DARDO (1.47/2.47, 1.35/2.37, 1.12/2.19, all from the script).
4. **5G QoS class.** "QCI 1/65 (URLLC)" is incorrect (QCI 1 = conversational voice, QCI 65 = MC-PTT). Changed to delay-critical GBR 5QI 82–85 per 3GPP TS 23.501, in the paper and README.
5. **Latency budget.** The 90 s scan is now stated as a *budget* ("validated two-minute protocols acquire five sequences in ~2 min; we budget 90 s for the stroke-relevant subset") because no cited paper reports a <90 s stroke scan. The 30 Mbps uplink is stated as an assumption.
6. **Silent-erasure rule (fixed 18 Nov 2026).** Sec. III-C stated `z_recon < z_crit = 1.5` with `|ΔPSNR| <= 0.05 dB`, but the released labels (`erased`, `silently_erased`, 100 % agreement) use the pre-registered CSA rule: `z_ref >= z_det = 3.0`, `z_recon < z_miss = 2.0` (2.0–3.0 indeterminate), and lesion-present PSNR inside the central 95 % interval of lesion-free PSNR at the same model/R/mask (`thresholds_sha256` 911de8625fec = CSA `configs/thresholds.yaml`, committed 8 Sep 2026). Worse, `benchmark_full_dardo.py` scored the DARDO projection with the 1.5 rule, so "28.8 % → 1.89 %", "15.2×", "17.4 % → 4.55 %" and the micro-infarct "Pareto cost" (11.7 % → 15.2 %) compared two different rules. Now one rule everywhere: Eq. (6) states it; the script applies it (and asserts it reproduces the released labels); DARDO projections are 0 % for 64 mm³ at every R, 0.83 % [0.34, 1.32] mean at R = 8, and 11.7 % → 4.17 % for micro-infarcts (the only non-zero cell). Conventional numbers and Fig. 3(c) are unchanged; Fig. 3(b) now marks z_miss = 2.0; abstract "below 2 %" → "below 1 %". The paper stays at 6 pages.

7. **Case-study figure replaced (19 Nov 2026).** The previous Fig. 4 (`fig6_qualitative_case_study`) was described as "a clinical scan" with an ℓ1-ESPIRiT and a learned-prior reconstruction, but it was a synthetic illustration: no script, data or model behind it existed anywhere (it was written on 16 Sep 2026 together with the unused fig3/fig4_cho/fig5, which share the problem), panel (a) had no anatomical texture, and panel (c) equalled (a) except in a 45 × 45-pixel patch around the lesion. It is replaced by `fig6_real_case`: released pair `file_brain_AXFLAIR_200_6002588`, slice 9, 64 mm³ lesion at (276, 213), contrast +1.5, equispaced R = 8, reconstructed by `figures/generate_fig6_case.py` with the audit's own code (ESPIRiT maps from the 32 centre lines, ZeroFilled, CGSense λ = 1e-2) from the audit's case pack; PSNR and residual match the released row to every printed digit. CG-SENSE keeps the lesion (z = 4.53), zero-filled misses it (z = 1.73; ΔPSNR 0.054 dB, residual −0.09 %): silently erased. Text changed accordingly: Sec. IV-A no longer claims a qualitative learned-prior examination, Sec. IV-E describes the real pair, and limitation (3) says learned reconstructions are not yet audited. The paper stays at 6 pages. Paper 2 (`csa_paper2_v2.tex`) uses the same synthetic fig3–fig6 and needs the same treatment.

## 4. Items for you to verify before upload

* Author list, order, affiliations and e-mails on page 1 (unchanged from submission).
* The GitHub URL `https://github.com/dmai287/tele-radiology-blindspot` is public and matches the README.
* 95% CIs: 28.79 % [23.3, 34.2] and the DARDO mean 0.83 % [0.34, 1.32] were recomputed on 18 Nov 2026 (normal approximation, n = 264 and 1,320).
* Figures 1, 2 and 4 were only rescaled (0.86 / 0.86 / 0.78 textwidth); Fig. 3 was already correct. Figure numbering changed with the reorder (architecture is now Fig. 2, network RD Fig. 3, case study Fig. 4) — all `\ref`s resolve.

## 5. ICOIN 2027 camera-ready + copyright procedure (from icoin.org/authors_paperSubmission)

Deadline: **4 December 2026**. Late papers are not included in the proceedings.

1. **Do not add** the IEEE copyright notice, page numbers or the conference name — the organisers insert the copyright line. (`main.tex` has no `\IEEEpubid`, no `hyperref`.)
2. **IEEE PDF eXpress**: https://ieee-pdf-express.org, conference ID **72679X**. Create a new title with the exact paper title. Option 1 (recommended): upload the LaTeX source as a zip (`main.tex`, `references.bib`, `IEEEtran.cls`, `figures/*.pdf`). Option 2: upload `main.pdf` (fonts embedded, no bookmarks, no links — all three checked). Note: the matplotlib figures embed fonts as Type 3; PDF eXpress accepts them, but if it objects, regenerate `fig1`/`fig2` with `matplotlib.rcParams['pdf.fonttype'] = 42` and rebuild.
3. **IEEE copyright form (eCF)**: log in to EDAS (https://edas.info/N35408) → your paper → click the **copyright icon** → "IEEE Copyright Submission" → complete the eCF on the IEEE site. Use the exact title and author list from `main.tex`. Standard IEEE copyright transfer applies (RMIT, no government/Crown variant). Compulsory for inclusion.
4. **Registration**: at least one author (students included) must register at the **full** rate and present. Registration: http://icoin.org/registration_reg (queries: Prof. Woongsoo Na, wsna@kongju.ac.kr).
5. **Upload**: EDAS → paper page → "Final Manuscript" → upload the PDF-eXpress-certified PDF only (EDAS rejects the original). No further revision is possible after upload.
6. Publication chair for camera-ready problems: Prof. Seunghyun Park (sp@hansung.ac.kr).
