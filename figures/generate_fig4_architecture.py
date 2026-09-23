"""
Generate Figure 4 (Publication-Grade Masterpiece): The 4-Layer Diagnostic-Aware Tele-Radiology Architecture
IEEE ICOIN 2027 Conference Publication Figure
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# High-quality typography settings
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'Times']
plt.rcParams['mathtext.fontset'] = 'cm'

fig = plt.figure(figsize=(11.0, 3.55), dpi=300)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Main Title Banner
ax.text(50, 96.8, "4-LAYER DIAGNOSTIC-AWARE TELE-RADIOLOGY ARCHITECTURE (DARDO + CSA + 5G URLLC)",
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#111111')

# =============================================================================
# COLUMN 1: TRANSMITTER (MOBILE STROKE UNIT / AMBULANCE)
# Coordinates: x in [1.7, 29.9] (width 28.2, center 15.8), y in [17.5, 91.5] (height 74.0)
# =============================================================================
card_col1 = patches.FancyBboxPatch((1.7, 17.5), 28.2, 74.0, boxstyle="round,pad=0.7,rounding_size=1.8",
                                   facecolor='#f0f4f9', edgecolor='#1f77b4', linewidth=1.5)
ax.add_patch(card_col1)

# Header Banner
badge_tx = patches.FancyBboxPatch((3.0, 84.0), 25.6, 5.8, boxstyle="round,pad=0.3,rounding_size=1.0",
                                  facecolor='#1f77b4', edgecolor='none')
ax.add_patch(badge_tx)
ax.text(15.8, 86.9, "TRANSMITTER: MOBILE STROKE UNIT", ha='center', va='center',
        fontsize=8.0, fontweight='bold', color='#ffffff')

# Layer 1: Perception & Audit (CSA) [y in 53.0 to 82.0]
card_l1 = patches.FancyBboxPatch((2.6, 53.0), 26.4, 29.0, boxstyle="round,pad=0.5,rounding_size=1.2",
                                 facecolor='#ffffff', edgecolor='#1f77b4', linewidth=1.1)
ax.add_patch(card_l1)
tag_l1 = patches.FancyBboxPatch((3.8, 76.0), 17.2, 4.4, boxstyle="round,pad=0.2,rounding_size=0.8",
                                facecolor='#e1edf7', edgecolor='#1f77b4', linewidth=0.8)
ax.add_patch(tag_l1)
ax.text(12.4, 78.2, "LAYER 1: PERCEPTION & AUDIT", ha='center', va='center',
        fontsize=6.6, fontweight='bold', color='#08519c')

ax.text(3.8, 71.8, r"$\bullet$ Counterfactual: $\mathbf{Y}_{\mathrm{cf}} = \mathbf{Y} + \mathbf{A}\boldsymbol{\delta}$",
        fontsize=7.1, color='#222222')
ax.text(3.8, 66.4, r"$\bullet$ Gabor Channelised Hotelling Observer (CHO)",
        fontsize=7.1, color='#222222')
ax.text(3.8, 61.0, r"$\bullet$ Clinical Detectability Metric ($d'_{\mathrm{CHO}} \geq 1.5$)",
        fontsize=7.1, color='#222222')
ax.text(3.8, 55.6, r"$\bullet$ Replaces blind whole-image PSNR / SSIM",
        fontsize=6.9, fontstyle='italic', color='#08519c')

# Internal Downward Arrow (Layer 1 -> Layer 2) in 5.4-unit gap [47.6, 53.0]
arrow_intra1 = patches.FancyArrowPatch((15.8, 53.0), (15.8, 48.0),
                                       arrowstyle='-|>,head_width=2.2,head_length=2.6',
                                       color='#1f77b4', linewidth=1.4)
ax.add_patch(arrow_intra1)
ax.text(17.4, 50.5, r"Task Prior $\mathbf{w}_{\mathrm{CHO}}$", ha='left', va='center',
        fontsize=6.2, fontweight='bold', color='#08519c')

# Layer 2: Compression (DARDO) [y in 18.6 to 47.6]
card_l2 = patches.FancyBboxPatch((2.6, 18.6), 26.4, 29.0, boxstyle="round,pad=0.5,rounding_size=1.2",
                                 facecolor='#ffffff', edgecolor='#2ca02c', linewidth=1.1)
ax.add_patch(card_l2)
tag_l2 = patches.FancyBboxPatch((3.8, 41.6), 19.6, 4.4, boxstyle="round,pad=0.2,rounding_size=0.8",
                                facecolor='#e5f5e0', edgecolor='#2ca02c', linewidth=0.8)
ax.add_patch(tag_l2)
ax.text(13.6, 43.8, "LAYER 2: COMPRESSION (DARDO)", ha='center', va='center',
        fontsize=6.6, fontweight='bold', color='#1b7837')

ax.text(3.8, 37.4, r"$\bullet$ Task Spectral Density: $W = |\mathcal{F}\{\mathbf{w}\}|^2$",
        fontsize=7.1, color='#222222')
ax.text(3.8, 32.0, r"$\bullet$ Diagnostic Grad: $\gamma_k = \sum_y W(k,y)\|\mathcal{F}\mathcal{S}_k\|_2$",
        fontsize=7.1, color='#222222')
ax.text(3.8, 26.6, r"$\bullet$ Greedy Line Allocation ($< 2\,\mathrm{ms}$ Edge CPU)",
        fontsize=7.1, color='#222222')
ax.text(3.8, 21.2, r"$\bullet$ Slashes stroke erasure: 28.8% $\to <4.5\%$",
        fontsize=7.1, fontweight='bold', color='#b2182b')

# =============================================================================
# COLUMN 2: 5G/B5G CELLULAR RADIO ACCESS NETWORK
# Coordinates: x in [35.9, 64.1] (width 28.2, center 50.0), y in [17.5, 91.5] (height 74.0)
# =============================================================================
card_col2 = patches.FancyBboxPatch((35.9, 17.5), 28.2, 74.0, boxstyle="round,pad=0.7,rounding_size=1.8",
                                   facecolor='#fdf8f4', edgecolor='#d95f02', linewidth=1.5)
ax.add_patch(card_col2)

# Header Banner
badge_ran = patches.FancyBboxPatch((37.2, 84.0), 25.6, 5.8, boxstyle="round,pad=0.3,rounding_size=1.0",
                                   facecolor='#d95f02', edgecolor='none')
ax.add_patch(badge_ran)
ax.text(50.0, 86.9, "5G / B5G CELLULAR RADIO ACCESS", ha='center', va='center',
        fontsize=8.0, fontweight='bold', color='#ffffff')

# Layer 3 (Slice A): 5G URLLC Slice (Critical Diagnostic Bands) [y in 53.0 to 82.0]
card_l3a = patches.FancyBboxPatch((36.8, 53.0), 26.4, 29.0, boxstyle="round,pad=0.5,rounding_size=1.2",
                                  facecolor='#ffffff', edgecolor='#d95f02', linewidth=1.1)
ax.add_patch(card_l3a)
tag_l3a = patches.FancyBboxPatch((38.0, 76.0), 21.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.8",
                                 facecolor='#feedde', edgecolor='#d95f02', linewidth=0.8)
ax.add_patch(tag_l3a)
ax.text(48.5, 78.2, "LAYER 3: 5G URLLC SLICE (CRITICAL)", ha='center', va='center',
        fontsize=6.6, fontweight='bold', color='#a63603')

ax.text(38.0, 71.8, r"$\bullet$ High Diagnostic Bands ($\gamma_k \geq \tau$) + 128B Token",
        fontsize=7.1, color='#222222')
ax.text(38.0, 66.4, r"$\bullet$ Tagged: 5G QCI 1 / 65 (URLLC Priority)",
        fontsize=7.1, fontweight='bold', color='#a63603')
ax.text(38.0, 61.0, r"$\bullet$ Guaranteed BLER $< 10^{-5}$, Latency $< 10\,\mathrm{ms}$",
        fontsize=7.1, color='#222222')
ax.text(38.0, 55.6, r"$\bullet$ Immune to cellular fading & dropouts",
        fontsize=6.9, fontstyle='italic', color='#a63603')

# Layer 3 (Slice B): 5G eMBB Slice (Bulk Anatomy) [y in 18.6 to 47.6]
card_l3b = patches.FancyBboxPatch((36.8, 18.6), 26.4, 29.0, boxstyle="round,pad=0.5,rounding_size=1.2",
                                  facecolor='#ffffff', edgecolor='#7f7f7f', linewidth=1.1)
ax.add_patch(card_l3b)
tag_l3b = patches.FancyBboxPatch((38.0, 41.6), 20.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.8",
                                 facecolor='#f0f0f0', edgecolor='#7f7f7f', linewidth=0.8)
ax.add_patch(tag_l3b)
ax.text(48.0, 43.8, "LAYER 3: 5G eMBB SLICE (BULK)", ha='center', va='center',
        fontsize=6.6, fontweight='bold', color='#444444')

ax.text(38.0, 37.4, r"$\bullet$ Low Diagnostic Gradient Bands ($\gamma_k < \tau$)",
        fontsize=7.1, color='#222222')
ax.text(38.0, 32.0, r"$\bullet$ Best-Effort Enhanced Mobile Broadband",
        fontsize=7.1, color='#222222')
ax.text(38.0, 26.6, r"$\bullet$ Transmits gross structural skull & anatomy",
        fontsize=7.1, color='#222222')
ax.text(38.0, 21.2, r"$\bullet$ Dynamic DASH streaming; tolerates packet loss",
        fontsize=6.9, fontstyle='italic', color='#555555')

# =============================================================================
# COLUMN 3: RECEIVER (HOSPITAL EDGE CLOUD SERVER)
# Coordinates: x in [70.1, 98.3] (width 28.2, center 84.2), y in [17.5, 91.5] (height 74.0)
# =============================================================================
card_col3 = patches.FancyBboxPatch((70.1, 17.5), 28.2, 74.0, boxstyle="round,pad=0.7,rounding_size=1.8",
                                   facecolor='#f7f5fa', edgecolor='#7570b3', linewidth=1.5)
ax.add_patch(card_col3)

# Header Banner
badge_rx = patches.FancyBboxPatch((71.4, 84.0), 25.6, 5.8, boxstyle="round,pad=0.3,rounding_size=1.0",
                                  facecolor='#7570b3', edgecolor='none')
ax.add_patch(badge_rx)
ax.text(84.2, 86.9, "RECEIVER: HOSPITAL EDGE SERVER", ha='center', va='center',
        fontsize=8.0, fontweight='bold', color='#ffffff')

# Subcard: Edge AI Reconstruction [y in 53.0 to 82.0]
card_recon = patches.FancyBboxPatch((71.0, 53.0), 26.4, 29.0, boxstyle="round,pad=0.5,rounding_size=1.2",
                                    facecolor='#ffffff', edgecolor='#7570b3', linewidth=1.1)
ax.add_patch(card_recon)
tag_recon = patches.FancyBboxPatch((72.2, 76.0), 21.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.8",
                                   facecolor='#efedf5', edgecolor='#7570b3', linewidth=0.8)
ax.add_patch(tag_recon)
ax.text(82.7, 78.2, "EDGE AI RECONSTRUCTION (VarNet)", ha='center', va='center',
        fontsize=6.6, fontweight='bold', color='#4d4682')

ax.text(72.2, 71.8, r"$\bullet$ End-to-End Variational Network ($1.8\,\mathrm{s}$ GPU)",
        fontsize=7.1, color='#222222')
ax.text(72.2, 66.4, r"$\bullet$ Recovers patient slice $\hat{\mathbf{X}}$ (URLLC + eMBB)",
        fontsize=7.1, color='#222222')
ax.text(72.2, 61.0, r"$\bullet$ Cosmetic PSNR $> 25.3\,\mathrm{dB}$, SSIM $> 0.86$",
        fontsize=7.1, color='#222222')
ax.text(72.2, 55.6, r"$\bullet$ Passes unweighted data-consistency gates",
        fontsize=6.9, fontstyle='italic', color='#4d4682')

# Internal Downward Arrow (Reconstruction -> Layer 4 Semantic Audit) in 5.4-unit gap [47.6, 53.0]
arrow_intra2 = patches.FancyArrowPatch((84.2, 53.0), (84.2, 48.0),
                                       arrowstyle='-|>,head_width=2.2,head_length=2.6',
                                       color='#7570b3', linewidth=1.4)
ax.add_patch(arrow_intra2)
ax.text(85.8, 50.5, r"$\hat{\mathbf{X}}$ + Token", ha='left', va='center',
        fontsize=6.2, fontweight='bold', color='#4d4682')

# Subcard: Layer 4 - Semantic Verification & S-NACK Decision Gate [y in 18.6 to 47.6]
card_l4 = patches.FancyBboxPatch((71.0, 18.6), 26.4, 29.0, boxstyle="round,pad=0.5,rounding_size=1.2",
                                 facecolor='#ffffff', edgecolor='#e7298a', linewidth=1.1)
ax.add_patch(card_l4)
tag_l4 = patches.FancyBboxPatch((72.2, 41.6), 23.5, 4.4, boxstyle="round,pad=0.2,rounding_size=0.8",
                                facecolor='#fde0dd', edgecolor='#e7298a', linewidth=0.8)
ax.add_patch(tag_l4)
ax.text(83.95, 43.8, "LAYER 4: SEMANTIC AUDIT & S-NACK", ha='center', va='center',
        fontsize=6.6, fontweight='bold', color='#980043')

ax.text(72.2, 37.4, r"$\bullet$ 128-Byte Semantic Token in QUIC/RTP Header",
        fontsize=7.1, color='#222222')
ax.text(72.2, 32.2, r"$\bullet$ Edge CHO Validation in $< 15\,\mathrm{ms}$ (Score $z_{\mathrm{recon}}$)",
        fontsize=7.1, color='#222222')

# Pass / Fail Decision Badges
pass_badge = patches.FancyBboxPatch((72.2, 25.4), 24.0, 4.2, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor='#e5f5e0', edgecolor='#2ca02c', linewidth=0.8)
ax.add_patch(pass_badge)
ax.text(84.2, 27.5, r"PASS ($z \geq 1.5$): Verified Safe Diagnostic", ha='center', va='center',
        fontsize=6.7, fontweight='bold', color='#1b7837')

fail_badge = patches.FancyBboxPatch((72.2, 19.8), 24.0, 4.2, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor='#fee8e8', edgecolor='#d62728', linewidth=0.8)
ax.add_patch(fail_badge)
ax.text(84.2, 21.9, r"FAIL ($z < 1.5$): Erasure! $\Rightarrow$ Trigger S-NACK", ha='center', va='center',
        fontsize=6.7, fontweight='bold', color='#b2182b')

# =============================================================================
# FORWARD FLOW ARROWS (TX -> RAN -> RX) ACROSS 6.0-UNIT GAPS
# Gap 1: x in [29.9, 35.9] (center 32.9)
# Gap 2: x in [64.1, 70.1] (center 67.1)
# Vertically aligned with exact center of top subcard (y=67.5) and bottom subcard (y=33.1)
# =============================================================================
# Top forward flow: URLLC Slice (Critical)
arrow_fwd1 = patches.FancyArrowPatch((30.4, 67.5), (35.4, 67.5),
                                     arrowstyle='-|>,head_width=2.4,head_length=2.8',
                                     color='#d95f02', linewidth=2.0)
ax.add_patch(arrow_fwd1)

arrow_fwd2 = patches.FancyArrowPatch((64.6, 67.5), (69.6, 67.5),
                                     arrowstyle='-|>,head_width=2.4,head_length=2.8',
                                     color='#d95f02', linewidth=2.0)
ax.add_patch(arrow_fwd2)

# Bottom forward flow: eMBB Slice (Bulk)
arrow_fwd3 = patches.FancyArrowPatch((30.4, 33.1), (35.4, 33.1),
                                     arrowstyle='-|>,head_width=2.4,head_length=2.8',
                                     color='#7f7f7f', linewidth=2.0)
ax.add_patch(arrow_fwd3)

arrow_fwd4 = patches.FancyArrowPatch((64.6, 33.1), (69.6, 33.1),
                                     arrowstyle='-|>,head_width=2.4,head_length=2.8',
                                     color='#7f7f7f', linewidth=2.0)
ax.add_patch(arrow_fwd4)

# Text labels centered in 6.0-unit gaps
ax.text(32.9, 69.8, "URLLC", ha='center', va='bottom', fontsize=6.8, fontweight='bold', color='#d95f02')
ax.text(32.9, 65.2, "(Critical)", ha='center', va='top', fontsize=5.6, fontstyle='italic', color='#a63603')

ax.text(67.1, 69.8, "URLLC", ha='center', va='bottom', fontsize=6.8, fontweight='bold', color='#d95f02')
ax.text(67.1, 65.2, "(Critical)", ha='center', va='top', fontsize=5.6, fontstyle='italic', color='#a63603')

ax.text(32.9, 35.4, "eMBB", ha='center', va='bottom', fontsize=6.8, fontweight='bold', color='#555555')
ax.text(32.9, 30.8, "(Bulk Data)", ha='center', va='top', fontsize=5.6, fontstyle='italic', color='#666666')

ax.text(67.1, 35.4, "eMBB", ha='center', va='bottom', fontsize=6.8, fontweight='bold', color='#555555')
ax.text(67.1, 30.8, "(Bulk Data)", ha='center', va='top', fontsize=5.6, fontstyle='italic', color='#666666')

# =============================================================================
# CLOSED-LOOP RETURN PATH: S-NACK RETRANSMISSION CHANNEL (DEDICATED BOTTOM BAND)
# S-NACK returns from Receiver (Hospital Edge Server) to Transmitter (MSU)
# =============================================================================
# Step 1: Smooth right-angle arrow leaving Hospital Edge Server (x=84.2, y=17.5) and entering S-NACK banner (x=74.0, y=7.5)
arrow_snack_down = patches.FancyArrowPatch((84.2, 17.5), (74.0, 7.5),
                                           connectionstyle="angle,angleA=-90,angleB=180,rad=3.5",
                                           arrowstyle='-|>,head_width=2.5,head_length=3.2',
                                           color='#d62728', linestyle='--', linewidth=1.7)
ax.add_patch(arrow_snack_down)
ax.text(79.1, 10.2, "FAIL Audit", ha='center', va='bottom', fontsize=5.8, fontweight='bold', color='#b2182b')

# Step 2: S-NACK Central Pill Banner in dedicated bottom channel [x in 26.0 to 74.0]
snack_banner = patches.FancyBboxPatch((26.0, 4.3), 48.0, 6.4, boxstyle="round,pad=0.3,rounding_size=1.0",
                                      facecolor='#fff5f5', edgecolor='#d62728', linewidth=1.3)
ax.add_patch(snack_banner)
ax.text(50.0, 7.5, r"CLOSED-LOOP S-NACK RETRANSMISSION: Requests only missing $\Delta k$ bands ($\sim 1.2\,\mathrm{MB}$, $\sim 15\,\mathrm{ms}$)",
        ha='center', va='center', fontsize=7.2, fontweight='bold', color='#a50f15')

# Step 3: Smooth right-angle arrow leaving S-NACK banner (x=26.0, y=7.5) and entering Mobile Stroke Unit (x=15.8, y=17.5)
arrow_snack_up = patches.FancyArrowPatch((26.0, 7.5), (15.8, 17.5),
                                         connectionstyle="angle,angleA=180,angleB=90,rad=3.5",
                                         arrowstyle='-|>,head_width=2.5,head_length=3.2',
                                         color='#d62728', linestyle='--', linewidth=1.7)
ax.add_patch(arrow_snack_up)
ax.text(20.9, 10.2, r"Resend $\Delta k$", ha='center', va='bottom', fontsize=5.8, fontweight='bold', color='#b2182b')

# Save high-res PDF and PNG
fig_dir = os.path.dirname(os.path.abspath(__file__))
out_pdf = os.path.join(fig_dir, 'fig4_architecture.pdf')
out_png = os.path.join(fig_dir, 'fig4_architecture.png')

plt.savefig(out_pdf, format='pdf', dpi=300)
plt.savefig(out_png, format='png', dpi=300)
plt.close()

print("Successfully generated refined publication Figure 4:")
print(" -", out_pdf)
print(" -", out_png)
