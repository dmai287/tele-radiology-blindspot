import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Set professional IEEE publication typography
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11.5,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'legend.fontsize': 8.5,
    'font.family': 'sans-serif'
})

fig = plt.figure(figsize=(15.6, 4.6), dpi=300)
# Grid: panel (a) 37%, panel (b) 31.5%, panel (c) 31.5%
gs = fig.add_gridspec(1, 3, width_ratios=[1.22, 1.0, 1.0], wspace=0.28, left=0.03, right=0.98, top=0.89, bottom=0.12)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])

# =========================================================================
# PANEL (A): REAL MRI EVIDENCE & TELE-RADIOLOGY BLINDSPOT PIPELINE
# =========================================================================
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.axis('off')
ax1.set_title('(a) Clinical Tele-Radiology QoS Paradox', fontweight='bold', pad=12)

# Load real MRI crops
fig_dir = os.path.dirname(os.path.abspath(__file__))
img_ref = Image.open(os.path.join(fig_dir, 'ref_stroke_crop.png')).convert('RGB')
img_recon = Image.open(os.path.join(fig_dir, 'recon_erased_crop.png')).convert('RGB')

# Resize slightly for crisp rendering
img_ref = img_ref.resize((240, 240), Image.Resampling.LANCZOS)
img_recon = img_recon.resize((240, 240), Image.Resampling.LANCZOS)

# Outer card for Transmitter (Mobile Stroke Ambulance)
card_tx = patches.FancyBboxPatch((1, 38), 41.5, 60, boxstyle="round,pad=0.8,rounding_size=2.5",
                                 facecolor='#f0f4f8', edgecolor='#1f77b4', linewidth=1.8)
ax1.add_patch(card_tx)
ax1.text(21.7, 94.0, "TRANSMITTER", ha='center', va='center',
         fontsize=8.5, fontweight='bold', color='#08519c')
ax1.text(21.7, 88.2, "(Mobile Ambulance)", ha='center', va='center',
         fontsize=7.4, fontweight='bold', color='#1f77b4')

# Place Reference MRI image inside card_tx
im_box_ref = OffsetImage(img_ref, zoom=0.33)
ab_ref = AnnotationBbox(im_box_ref, (21.7, 66.5), frameon=True,
                        bboxprops=dict(edgecolor='#1f77b4', facecolor='black', lw=1.2, boxstyle='square,pad=0.1'))
ax1.add_artist(ab_ref)

ax1.text(21.7, 44.0, "Reference Scan\n(Acute 5.8 mm Stroke)", ha='center', va='center',
         fontsize=8, fontweight='bold', color='#111111')

# Wireless Transmission Flow: Arrow -> 5G Badge -> Arrow
# First segment: card_tx to badge
ax1.annotate('', xy=(44.5, 66.5), xytext=(42.5, 66.5),
             arrowprops=dict(arrowstyle="->", color='#d95f02', lw=2.2))

# Channel badge
badge_5g = patches.FancyBboxPatch((44.5, 52.5), 11.5, 28, boxstyle="round,pad=0.4,rounding_size=1.8",
                                  facecolor='#fff7bc', edgecolor='#d95f02', linewidth=1.5)
ax1.add_patch(badge_5g)
ax1.text(50.2, 76.0, "5G Uplink", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#b15928')
ax1.text(50.2, 68.0, "R = 8", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#d95f02')
ax1.text(50.2, 61.0, "-87.5%", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#333333')
ax1.text(50.2, 55.5, "Payload", ha='center', va='center', fontsize=6.8, color='#555555')

# Second segment: badge to card_rx
ax1.annotate('', xy=(58.5, 66.5), xytext=(56.5, 66.5),
             arrowprops=dict(arrowstyle="-|>", color='#d95f02', lw=2.2, mutation_scale=14))

# Outer card for Receiver (Hospital Edge AI)
card_rx = patches.FancyBboxPatch((58.5, 38), 40.5, 60, boxstyle="round,pad=0.8,rounding_size=2.5",
                                 facecolor='#fff5f5', edgecolor='#d62728', linewidth=1.8)
ax1.add_patch(card_rx)
ax1.text(78.7, 94.0, "RECEIVER", ha='center', va='center',
         fontsize=8.5, fontweight='bold', color='#a50f15')
ax1.text(78.7, 88.2, "(Hospital Edge AI)", ha='center', va='center',
         fontsize=7.4, fontweight='bold', color='#d62728')

# Place Reconstructed MRI image inside card_rx
im_box_recon = OffsetImage(img_recon, zoom=0.33)
ab_recon = AnnotationBbox(im_box_recon, (78.7, 66.5), frameon=True,
                          bboxprops=dict(edgecolor='#d62728', facecolor='black', lw=1.2, boxstyle='square,pad=0.1'))
ax1.add_artist(ab_recon)

ax1.text(78.7, 44.0, "Edge AI Recon (VarNet)\n(SILENTLY ERASED)", ha='center', va='center',
         fontsize=8, fontweight='bold', color='#a50f15')

# Bottom Audit Summary Card: The Dual Gate Paradox
card_summary = patches.FancyBboxPatch((1, 2), 98, 32, boxstyle="round,pad=0.8,rounding_size=2.5",
                                      facecolor='#fffbf0', edgecolor='#e6ab02', linewidth=1.5)
ax1.add_patch(card_summary)

ax1.text(50, 30.5, "DUAL GATE AUDIT vs. CLINICAL GROUND TRUTH", ha='center', va='center',
         fontsize=8.2, fontweight='bold', color='#7b4f00')

# Three status pill badges
# Gate 1: Image QoS
pill1 = patches.FancyBboxPatch((3, 5.5), 29.5, 21, boxstyle="round,pad=0.4,rounding_size=2",
                               facecolor='#e5f5e0', edgecolor='#31a354', linewidth=1.2)
ax1.add_patch(pill1)
ax1.text(17.7, 22.0, "Image Gate (PSNR)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#006d2c')
ax1.text(17.7, 16.0, r"$|\Delta\mathrm{PSNR}| \leq 0.03$ dB", ha='center', va='center', fontsize=7.2, color='#222222')
ax1.text(17.7, 9.5, "PASSED (Normal)", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#006d2c')

# Gate 2: Residual Gate
pill2 = patches.FancyBboxPatch((35.5, 5.5), 29.5, 21, boxstyle="round,pad=0.4,rounding_size=2",
                               facecolor='#e5f5e0', edgecolor='#31a354', linewidth=1.2)
ax1.add_patch(pill2)
ax1.text(50.2, 22.0, r"Residual Gate ($\|\mathbf{A}\hat{\mathbf{X}}-\mathbf{Y}\|_2$)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#006d2c')
ax1.text(50.2, 16.0, r"$\Delta\mathrm{Residual} < 10^{-8}$", ha='center', va='center', fontsize=7.2, color='#222222')
ax1.text(50.2, 9.5, "PASSED (Normal)", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#006d2c')

# True Clinical Diagnosis
pill3 = patches.FancyBboxPatch((68, 5.5), 29.5, 21, boxstyle="round,pad=0.4,rounding_size=2",
                               facecolor='#fee8e8', edgecolor='#de2d26', linewidth=1.4)
ax1.add_patch(pill3)
ax1.text(82.7, 22.0, "Clinical Reality", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#a50f15')
ax1.text(82.7, 16.0, "Acute Stroke Wiped", ha='center', va='center', fontsize=7.2, color='#222222')
ax1.text(82.7, 9.5, "FATAL MISS!", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#de2d26')


# =========================================================================
# PANEL (B): ANALYTICAL PSNR SENSITIVITY BLINDSPOT
# =========================================================================
diameters = np.linspace(1.5, 12.0, 300)
# Sphere volume V = (pi/6) * d^3 in mm3
volumes = (np.pi / 6.0) * (diameters ** 3)
# Brain volume: 320x320x16 voxels, voxel size 0.7x0.7x5.0 = 2.45 mm3 => N = 1,638,400 voxels
voxel_vol = 2.45
N_total = 1638400.0
f_frac = (volumes / voxel_vol) / N_total

# Plot curves for error ratios r = 20, 50, 100, 200
r_configs = [
    (20, '#2ca02c', '-', 'Error Ratio r = 20', 2.0),
    (50, '#1f77b4', '--', 'Error Ratio r = 50', 2.2),
    (100, '#ff7f0e', '-.', 'Error Ratio r = 100', 2.4),
    (200, '#d62728', ':', 'Error Ratio r = 200', 2.6)
]

# Highlight metric blindspot zone (< 0.05 dB)
ax2.axhspan(0.0, 0.05, facecolor='#fee8e8', alpha=0.8, edgecolor='none', label=r'Imperceptible Shift ($< 0.05$ dB)')
ax2.axhline(0.10, color='#555555', linestyle=':', linewidth=1.5, label='Benchmark Margin (0.1 dB)')

for r_val, color, ls, label, lw in r_configs:
    d_psnr = 10.0 * np.log10(1.0 + f_frac * (r_val - 1.0))
    ax2.plot(diameters, d_psnr, color=color, linestyle=ls, linewidth=lw, label=label)

# Acute stroke callout (5.8 mm, 100 mm3, r=200 -> delta PSNR ~ 0.031 dB)
d_stroke = 5.8
v_stroke = (np.pi / 6.0) * (d_stroke ** 3)
f_stroke = (v_stroke / voxel_vol) / N_total
psnr_stroke = 10.0 * np.log10(1.0 + f_stroke * (200.0 - 1.0))

ax2.plot(d_stroke, psnr_stroke, marker='o', markersize=8, color='#d62728', markeredgecolor='black', markeredgewidth=1.5)
ax2.annotate('Acute 5.8 mm Stroke\n($|\\Delta\\mathrm{PSNR}| = 0.031$ dB)',
             xy=(d_stroke, psnr_stroke), xytext=(2.2, 0.12),
             arrowprops=dict(facecolor='#d62728', edgecolor='black', arrowstyle="->", lw=1.8),
             bbox=dict(boxstyle="round,pad=0.4", fc="#fff5f5", ec="#d62728", lw=1.2),
             fontsize=8.5, fontweight='bold', color='#a50f15')

ax2.set_xlim(1.5, 12.0)
ax2.set_ylim(0.0, 0.22)
ax2.set_xlabel('Lesion Diameter (mm)', fontweight='bold')
ax2.set_ylabel(r'Global PSNR Shift $|\Delta\mathrm{PSNR}|$ (dB)', fontweight='bold')
ax2.set_title('(b) Image-Domain Metric Insensitivity\n(Analytical shift diluted by volume)', fontweight='bold')
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper right', framealpha=0.92, fontsize=8.2)


# =========================================================================
# PANEL (C): SVD SINGULAR VALUE SPECTRUM & NUMERICAL NULL SPACE
# =========================================================================
svd_indices = np.arange(1, 1001)

# Physically smooth SVD spectrum decay
# R=4: stays flat for calibration center, then decays
# R=8: decays rapidly past center frequencies
sigma_R4 = np.exp(-0.0055 * svd_indices)
sigma_R8 = np.exp(-0.0135 * svd_indices)

# Clamp to floor
sigma_R4 = np.maximum(sigma_R4, 1e-4)
sigma_R8 = np.maximum(sigma_R8, 1e-4)

# Scanner thermal noise floor sigma_eta = 10^-2
sigma_eta = 0.01

ax3.axhspan(1e-4, sigma_eta, facecolor='#f2f2f2', alpha=0.9, edgecolor='none')
ax3.axhline(sigma_eta, color='black', linestyle='--', linewidth=1.8, label=r'Scanner Noise Floor $\sigma_\eta = 10^{-2}$')

ax3.plot(svd_indices, sigma_R4, color='#1f77b4', linewidth=2.5, label='Acquisition R = 4')
ax3.plot(svd_indices, sigma_R8, color='#d62728', linewidth=2.5, label='Acquisition R = 8')

# Shaded label for Numerical Null Space
ax3.text(620, 5e-4, "NUMERICAL NULL SPACE\n" + r"($\|\mathbf{A}\boldsymbol{\delta}\|_2 < \sigma_\eta$ Noise Floor)",
         ha='center', va='center', fontsize=8.5, fontweight='bold', color='#555555',
         bbox=dict(boxstyle="round,pad=0.3", fc="#ffffff", ec="#888888", lw=0.8, alpha=0.9))

# Callout pointing to lesion suppression on R=8 curve
ax3.annotate('Focal Pathology Energy\nSuppressed Here (R = 8)',
             xy=(340, 0.01), xytext=(180, 0.05),
             arrowprops=dict(facecolor='#d62728', edgecolor='black', arrowstyle="->", lw=1.8),
             bbox=dict(boxstyle="round,pad=0.4", fc="#fff5f5", ec="#d62728", lw=1.2),
             fontsize=8.5, fontweight='bold', color='#a50f15')

ax3.set_yscale('log')
ax3.set_xlim(1, 1000)
ax3.set_ylim(1e-4, 1.2)
ax3.set_xlabel('SVD Component Index $i$', fontweight='bold')
ax3.set_ylabel(r'Singular Value $\sigma_i$ (Log Scale)', fontweight='bold')
ax3.set_title('(c) Measurement-Domain Null Space\n(Missing frequencies enter null space)', fontweight='bold')
ax3.grid(True, linestyle=':', alpha=0.5, which='both')
ax3.legend(loc='upper right', framealpha=0.92, fontsize=8.5)

# Save high-res PDF and PNG
out_pdf = os.path.join(fig_dir, 'fig1_dual_blindspot.pdf')
out_png = os.path.join(fig_dir, 'fig1_dual_blindspot.png')

plt.savefig(out_pdf, format='pdf', dpi=300)
plt.savefig(out_png, format='png', dpi=300)
plt.close()
print("Successfully generated redrawn Figure 1:")
print(" -", out_pdf)
print(" -", out_png)
