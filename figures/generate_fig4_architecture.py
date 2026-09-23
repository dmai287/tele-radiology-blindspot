"""
Generate Figure 4: The 4-Layer Diagnostic-Aware Tele-Radiology Architecture
IEEE ICOIN 2027 Conference Publication Figure (Compact Publication Version)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set high-quality font settings
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'Times']
plt.rcParams['mathtext.fontset'] = 'cm'

# Compact aspect ratio: 10.5 x 3.1 inches
fig = plt.figure(figsize=(10.5, 3.1), dpi=300)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title banner
ax.text(50, 96.5, "4-LAYER DIAGNOSTIC-AWARE TELE-RADIOLOGY ARCHITECTURE (DARDO + CSA + 5G URLLC)",
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#111111')

# =============================================================================
# COLUMN 1: LAYER 1 & LAYER 2 (MOBILE AMBULANCE EDGE)
# =============================================================================
card_col1 = patches.FancyBboxPatch((1.2, 7), 31.2, 85, boxstyle="round,pad=0.7,rounding_size=1.8",
                                   facecolor='#f0f4f9', edgecolor='#1f77b4', linewidth=1.5)
ax.add_patch(card_col1)

# Header
ax.text(16.8, 88.0, "MOBILE STROKE UNIT (AMBULANCE)", ha='center', va='center',
        fontsize=9, fontweight='bold', color='#08519c')

# Subcard: Layer 1 - Perception & Safety Audit (CSA)
card_l1 = patches.FancyBboxPatch((2.6, 49), 28.4, 34, boxstyle="round,pad=0.5,rounding_size=1.2",
                                 facecolor='#ffffff', edgecolor='#1f77b4', linewidth=1.1)
ax.add_patch(card_l1)
ax.text(4.0, 78.5, "LAYER 1: PERCEPTION & AUDIT (CSA)", fontsize=7.8, fontweight='bold', color='#08519c')
ax.text(4.0, 72.5, r"$\bullet$ Counterfactual: $\mathbf{Y}_{\mathrm{cf}} = \mathbf{Y} + \mathbf{A}\boldsymbol{\delta}$", fontsize=7.4, color='#222222')
ax.text(4.0, 66.5, r"$\bullet$ Gabor Channelised Hotelling Observer (CHO)", fontsize=7.4, color='#222222')
ax.text(4.0, 60.5, r"$\bullet$ Clinical Detectability Metric ($d' \geq 1.5$)", fontsize=7.4, color='#222222')
ax.text(4.0, 54.5, r"$\bullet$ Replaces blind pixel-averaged PSNR/SSIM", fontsize=7.2, fontstyle='italic', color='#08519c')

# Subcard: Layer 2 - Diagnostic-Aware Rate-Distortion (DARDO)
card_l2 = patches.FancyBboxPatch((2.6, 11), 28.4, 35, boxstyle="round,pad=0.5,rounding_size=1.2",
                                 facecolor='#ffffff', edgecolor='#2ca02c', linewidth=1.1)
ax.add_patch(card_l2)
ax.text(4.0, 41.5, "LAYER 2: COMPRESSION (DARDO)", fontsize=7.8, fontweight='bold', color='#1b7837')
ax.text(4.0, 35.5, r"$\bullet$ Task Spectral Density: $W(k_x, k_y) = |\mathcal{F}\{\mathbf{w}\}|^2$", fontsize=7.4, color='#222222')
ax.text(4.0, 29.5, r"$\bullet$ Diagnostic Gradient: $\gamma_k = \sum_y W(k, y)\|\mathcal{F}\mathcal{S}_k\|_2$", fontsize=7.4, color='#222222')
ax.text(4.0, 23.5, r"$\bullet$ Greedy Line Allocation ($< 2\,\mathrm{ms}$ on Edge CPU)", fontsize=7.4, color='#222222')
ax.text(4.0, 17.5, r"$\bullet$ Cuts silent stroke erasure: 28.8% to <4.5%", fontsize=7.4, fontweight='bold', color='#b2182b')

# =============================================================================
# COLUMN 2: LAYER 3 (5G WIRELESS NETWORK SLICING & RAN)
# =============================================================================
card_col2 = patches.FancyBboxPatch((34.4, 7), 31.2, 85, boxstyle="round,pad=0.7,rounding_size=1.8",
                                   facecolor='#fdf8f4', edgecolor='#d95f02', linewidth=1.5)
ax.add_patch(card_col2)

# Header
ax.text(50.0, 88.0, "5G/B5G CELLULAR RADIO ACCESS", ha='center', va='center',
        fontsize=9, fontweight='bold', color='#a63603')

# Subcard: Layer 3 - 5G URLLC Slicing
card_l3a = patches.FancyBboxPatch((35.8, 49), 28.4, 34, boxstyle="round,pad=0.5,rounding_size=1.2",
                                  facecolor='#ffffff', edgecolor='#d95f02', linewidth=1.1)
ax.add_patch(card_l3a)
ax.text(37.2, 78.5, "LAYER 3: 5G URLLC SLICE (CRITICAL)", fontsize=7.8, fontweight='bold', color='#a63603')
ax.text(37.2, 72.5, r"$\bullet$ High Diagnostic Gradient Bands ($\gamma_k \geq \tau$)", fontsize=7.4, color='#222222')
ax.text(37.2, 66.5, r"$\bullet$ Tagged: 5G QCI 1 / 65 (URLLC Slice)", fontsize=7.4, fontweight='bold', color='#a63603')
ax.text(37.2, 60.5, r"$\bullet$ Block Error Rate (BLER) $< 10^{-5}$", fontsize=7.4, color='#222222')
ax.text(37.2, 54.5, r"$\bullet$ Sub-10 ms latency; immune to fading drops", fontsize=7.2, fontstyle='italic', color='#a63603')

# Subcard: Layer 3 - eMBB Bulk Slice
card_l3b = patches.FancyBboxPatch((35.8, 11), 28.4, 35, boxstyle="round,pad=0.5,rounding_size=1.2",
                                  facecolor='#ffffff', edgecolor='#7f7f7f', linewidth=1.1)
ax.add_patch(card_l3b)
ax.text(37.2, 41.5, "LAYER 3: 5G eMBB SLICE (BULK)", fontsize=7.8, fontweight='bold', color='#444444')
ax.text(37.2, 35.5, r"$\bullet$ Low Diagnostic Gradient Bands ($\gamma_k < \tau$)", fontsize=7.4, color='#222222')
ax.text(37.2, 29.5, r"$\bullet$ Best-Effort Enhanced Mobile Broadband", fontsize=7.4, color='#222222')
ax.text(37.2, 23.5, r"$\bullet$ Carries gross anatomical background", fontsize=7.4, color='#222222')
ax.text(37.2, 17.5, r"$\bullet$ Tolerates packet loss without diagnostic harm", fontsize=7.2, fontstyle='italic', color='#555555')

# =============================================================================
# COLUMN 3: LAYER 4 (HOSPITAL EDGE AI & SEMANTIC VERIFICATION)
# =============================================================================
card_col3 = patches.FancyBboxPatch((67.6, 7), 31.2, 85, boxstyle="round,pad=0.7,rounding_size=1.8",
                                   facecolor='#f7f5fa', edgecolor='#7570b3', linewidth=1.5)
ax.add_patch(card_col3)

# Header
ax.text(83.2, 88.0, "HOSPITAL EDGE CLOUD SERVER", ha='center', va='center',
        fontsize=9, fontweight='bold', color='#4d4682')

# Subcard: Edge AI Reconstruction
card_recon = patches.FancyBboxPatch((69.0, 49), 28.4, 34, boxstyle="round,pad=0.5,rounding_size=1.2",
                                    facecolor='#ffffff', edgecolor='#7570b3', linewidth=1.1)
ax.add_patch(card_recon)
ax.text(70.4, 78.5, "EDGE AI RECONSTRUCTION", fontsize=7.8, fontweight='bold', color='#4d4682')
ax.text(70.4, 72.5, r"$\bullet$ Multi-Coil Deep Variational Net (VarNet)", fontsize=7.4, color='#222222')
ax.text(70.4, 66.5, r"$\bullet$ Inference Latency: $1.8\,\mathrm{s}$ on GPU server", fontsize=7.4, color='#222222')
ax.text(70.4, 60.5, r"$\bullet$ Recovers patient cross-sectional slice $\hat{\mathbf{X}}$", fontsize=7.4, color='#222222')
ax.text(70.4, 54.5, r"$\bullet$ Generates high cosmetic PSNR ($>25\,\mathrm{dB}$)", fontsize=7.2, fontstyle='italic', color='#4d4682')

# Subcard: Layer 4 - Semantic Verification & S-NACK
card_l4 = patches.FancyBboxPatch((69.0, 11), 28.4, 35, boxstyle="round,pad=0.5,rounding_size=1.2",
                                 facecolor='#ffffff', edgecolor='#e7298a', linewidth=1.1)
ax.add_patch(card_l4)
ax.text(70.4, 41.5, "LAYER 4: SEMANTIC AUDIT & S-NACK", fontsize=7.8, fontweight='bold', color='#980043')
ax.text(70.4, 35.5, r"$\bullet$ 128-Byte Semantic Token in QUIC Header", fontsize=7.4, color='#222222')
ax.text(70.4, 29.5, r"$\bullet$ On-Edge CHO Audit: score $z_{\mathrm{recon}}$ ($< 15\,\mathrm{ms}$)", fontsize=7.4, color='#222222')
ax.text(70.4, 23.5, r"$\bullet$ Pass: $z \geq 1.5 \Rightarrow$ Verified; Fail: $z < 1.5 \Rightarrow$ Erased!", fontsize=7.4, fontweight='bold', color='#d62728')
ax.text(70.4, 17.5, r"$\bullet$ Targeted S-NACK requests missing $\Delta k$ lines", fontsize=7.2, fontstyle='italic', color='#980043')

# =============================================================================
# ARROWS AND INTER-LAYER FLOW
# =============================================================================
arrow_fwd1 = patches.FancyArrowPatch((32.4, 65.0), (34.4, 65.0),
                                     arrowstyle='-|>,head_width=3,head_length=4.5',
                                     color='#1f77b4', linewidth=2.2)
ax.add_patch(arrow_fwd1)

arrow_fwd2 = patches.FancyArrowPatch((65.6, 65.0), (67.6, 65.0),
                                     arrowstyle='-|>,head_width=3,head_length=4.5',
                                     color='#d95f02', linewidth=2.2)
ax.add_patch(arrow_fwd2)

arrow_snack = patches.FancyArrowPatch((69, 12), (32.4, 12),
                                      connectionstyle="arc3,rad=-0.12",
                                      arrowstyle='-|>,head_width=3,head_length=5',
                                      color='#d62728', linestyle='--', linewidth=1.8)
ax.add_patch(arrow_snack)
ax.text(50, 3.2, r"CLOSED-LOOP S-NACK (Requests only missing $\Delta k$ bands, $\sim 15\,\mathrm{ms}$)",
        ha='center', va='center', fontsize=7.5, fontweight='bold', color='#d62728',
        bbox=dict(boxstyle="round,pad=0.2", fc="#fff5f5", ec="#d62728", lw=0.8))

# Save PDF and PNG
fig_dir = os.path.dirname(os.path.abspath(__file__))
out_pdf = os.path.join(fig_dir, 'fig4_architecture.pdf')
out_png = os.path.join(fig_dir, 'fig4_architecture.png')

plt.savefig(out_pdf, format='pdf', dpi=300)
plt.savefig(out_png, format='png', dpi=300)
plt.close()

print(f"Successfully generated compact Figure 4:")
print(" -", out_pdf)
print(" -", out_png)
