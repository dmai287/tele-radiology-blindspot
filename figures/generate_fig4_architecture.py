"""
Generate Figure 4: The 4-Layer Diagnostic-Aware Tele-Radiology Architecture
IEEE ICOIN 2027 Conference Publication Figure
Publication-Grade Architecture Diagram
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Publication typography
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 8.0,
    'mathtext.fontset': 'cm'
})

fig = plt.figure(figsize=(11.0, 3.45), dpi=300)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Main Architecture Title
ax.text(50.0, 97.4, "FOUR-LAYER DIAGNOSTIC-AWARE TELE-RADIOLOGY ARCHITECTURE (DARDO + CSA + 5G URLLC)",
        ha='center', va='center', fontsize=9.2, fontweight='bold', color='#0f172a')

# =============================================================================
# DOMAIN 1: TRANSMITTER (MOBILE STROKE UNIT)
# x: [1.5, 30.5] (width 29.0), y: [16.5, 93.0] (height 76.5)
# =============================================================================
card_tx = patches.Rectangle((1.5, 16.5), 29.0, 76.5, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0)
ax.add_patch(card_tx)

hdr_tx = patches.Rectangle((1.5, 87.5), 29.0, 5.5, facecolor='#1e293b', edgecolor='none')
ax.add_patch(hdr_tx)
ax.text(16.0, 90.25, "TRANSMITTER: MOBILE STROKE UNIT (MSU)", ha='center', va='center',
        fontsize=7.0, fontweight='bold', color='#ffffff')

# Sub-block 1: Acquisition & Task Profiler (Layer 1)
# y: [54.0, 85.0] (height 31.0)
b1_box = patches.Rectangle((2.7, 54.0), 26.6, 31.0, facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=0.8)
ax.add_patch(b1_box)
b1_hdr = patches.Rectangle((2.7, 81.0), 26.6, 4.0, facecolor='#e0f2fe', edgecolor='#bae6fd', linewidth=0.6)
ax.add_patch(b1_hdr)
ax.text(16.0, 83.0, "LAYER 1: CLINICAL TASK PROFILER (CSA)", ha='center', va='center',
        fontsize=6.3, fontweight='bold', color='#0369a1')

ax.text(3.8, 76.5, "Acquisition:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(10.2, 76.5, r"RF Coils $\to$ Raw $k$-space $\mathbf{Y} \in \mathbb{C}^{C \times K_x \times K_y}$", fontsize=6.3, color='#334155')

ax.text(3.8, 70.0, "Observer Prior:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(11.8, 70.0, r"Gabor CHO Template $\mathbf{w}_{\mathrm{CHO}}$", fontsize=6.3, color='#334155')

ax.text(3.8, 63.5, "Task Spectrum:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(11.8, 63.5, r"$W(k_x, k_y) = |\mathcal{F}\{\mathbf{w}_{\mathrm{CHO}}\}|^2$", fontsize=6.3, color='#0369a1')

tag_l1 = patches.Rectangle((3.8, 56.0), 24.4, 4.8, facecolor='#f0f9ff', edgecolor='#7dd3fc', linewidth=0.6)
ax.add_patch(tag_l1)
ax.text(16.0, 58.4, r"Pre-Transmission Safety Goal: $d'_{\mathrm{CHO}} \geq 1.5$", ha='center', va='center',
        fontsize=5.9, fontweight='bold', color='#0284c7')

# Downward Arrow Layer 1 -> Layer 2
ax.annotate('', xy=(16.0, 49.0), xytext=(16.0, 54.0),
            arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=1.3, mutation_scale=8))
ax.text(17.5, 51.5, r"Task Prior $W(k_x, k_y)$", ha='left', va='center',
        fontsize=5.8, fontweight='bold', color='#0369a1')

# Sub-block 2: Diagnostic Compression (Layer 2 DARDO)
# y: [18.0, 49.0] (height 31.0)
b2_box = patches.Rectangle((2.7, 18.0), 26.6, 31.0, facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=0.8)
ax.add_patch(b2_box)
b2_hdr = patches.Rectangle((2.7, 45.0), 26.6, 4.0, facecolor='#dcfce7', edgecolor='#bbf7d0', linewidth=0.6)
ax.add_patch(b2_hdr)
ax.text(16.0, 47.0, "LAYER 2: DIAGNOSTIC COMPRESSION (DARDO)", ha='center', va='center',
        fontsize=6.3, fontweight='bold', color='#15803d')

ax.text(3.8, 40.5, "Diagnostic Grad:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(12.8, 40.5, r"$\gamma_k = \sum_y W(k,y)\|\mathcal{F}\mathcal{S}_k\|_2$", fontsize=6.3, color='#166534')

ax.text(3.8, 34.0, "Greedy Ranking:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(13.2, 34.0, r"Trajectory Sort ($< 2\,\mathrm{ms}$ Edge CPU)", fontsize=6.3, color='#334155')

ax.text(3.8, 27.5, "Slicing Split:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(11.0, 27.5, r"Threshold $\tau \Rightarrow \mathcal{K}_{\mathrm{diag}}$ vs. $\mathcal{K}_{\mathrm{bulk}}$", fontsize=6.3, color='#334155')

tag_l2 = patches.Rectangle((3.8, 20.0), 24.4, 4.8, facecolor='#f0fdf4', edgecolor='#86efac', linewidth=0.6)
ax.add_patch(tag_l2)
ax.text(16.0, 22.4, r"Token Embed: 128B Semantic Token $\boldsymbol{\theta}$ in Header", ha='center', va='center',
        fontsize=5.8, fontweight='bold', color='#15803d')

# =============================================================================
# DOMAIN 2: 5G / B5G CELLULAR RADIO ACCESS NETWORK
# x: [36.0, 64.0] (width 28.0), y: [16.5, 93.0] (height 76.5)
# =============================================================================
card_ran = patches.Rectangle((36.0, 16.5), 28.0, 76.5, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0)
ax.add_patch(card_ran)

hdr_ran = patches.Rectangle((36.0, 87.5), 28.0, 5.5, facecolor='#1e293b', edgecolor='none')
ax.add_patch(hdr_ran)
ax.text(50.0, 90.25, "5G / B5G CELLULAR RADIO ACCESS NETWORK", ha='center', va='center',
        fontsize=7.0, fontweight='bold', color='#ffffff')

# Layer 3 Slice A: URLLC Slice (Critical Diagnostic Lines)
# y: [54.0, 85.0] (height 31.0)
b3a_box = patches.Rectangle((37.2, 54.0), 25.6, 31.0, facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=0.8)
ax.add_patch(b3a_box)
b3a_hdr = patches.Rectangle((37.2, 81.0), 25.6, 4.0, facecolor='#ffedd5', edgecolor='#fed7aa', linewidth=0.6)
ax.add_patch(b3a_hdr)
ax.text(50.0, 83.0, "LAYER 3: 5G URLLC SLICE (MISSION-CRITICAL)", ha='center', va='center',
        fontsize=6.3, fontweight='bold', color='#c2410c')

ax.text(38.2, 76.5, "Critical Payload:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(47.2, 76.5, r"$\mathcal{K}_{\mathrm{diag}} = \{k \mid \gamma_k \geq \tau\} + \boldsymbol{\theta}$", fontsize=6.3, color='#c2410c')

ax.text(38.2, 70.0, "3GPP Service:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(46.0, 70.0, "QCI 1 / 65 (Dedicated BWP)", fontsize=6.3, color='#334155')

ax.text(38.2, 63.5, "QoS Bounds:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(45.2, 63.5, r"BLER $< 10^{-5}$, Latency $< 10\,\mathrm{ms}$", fontsize=6.3, color='#334155')

tag_l3a = patches.Rectangle((38.2, 56.0), 23.6, 4.8, facecolor='#fff7ed', edgecolor='#fdba74', linewidth=0.6)
ax.add_patch(tag_l3a)
ax.text(50.0, 58.4, "High Fading Margin (Zero Burst Dropout)", ha='center', va='center',
        fontsize=5.8, fontweight='bold', color='#ea580c')

# Layer 3 Slice B: eMBB Slice (Bulk Anatomy)
# y: [18.0, 49.0] (height 31.0)
b3b_box = patches.Rectangle((37.2, 18.0), 25.6, 31.0, facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=0.8)
ax.add_patch(b3b_box)
b3b_hdr = patches.Rectangle((37.2, 45.0), 25.6, 4.0, facecolor='#f1f5f9', edgecolor='#e2e8f0', linewidth=0.6)
ax.add_patch(b3b_hdr)
ax.text(50.0, 47.0, "LAYER 3: 5G eMBB SLICE (BULK ANATOMY)", ha='center', va='center',
        fontsize=6.3, fontweight='bold', color='#475569')

ax.text(38.2, 40.5, "Bulk Payload:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(45.8, 40.5, r"$\mathcal{K}_{\mathrm{bulk}} = \{k \mid \gamma_k < \tau\}$", fontsize=6.3, color='#475569')

ax.text(38.2, 34.0, "Transmitted Data:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(47.6, 34.0, "Gross Skull & Brain Shape", fontsize=6.3, color='#334155')

ax.text(38.2, 27.5, "Transport Mode:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(47.2, 27.5, "Dynamic DASH Streaming", fontsize=6.3, color='#334155')

tag_l3b = patches.Rectangle((38.2, 20.0), 23.6, 4.8, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=0.6)
ax.add_patch(tag_l3b)
ax.text(50.0, 22.4, "Best-Effort Throughput (Loss-Tolerant)", ha='center', va='center',
        fontsize=5.8, fontstyle='italic', color='#64748b')

# =============================================================================
# DOMAIN 3: RECEIVER (HOSPITAL EDGE SERVER)
# x: [69.5, 98.5] (width 29.0), y: [16.5, 93.0] (height 76.5)
# =============================================================================
card_rx = patches.Rectangle((69.5, 16.5), 29.0, 76.5, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0)
ax.add_patch(card_rx)

hdr_rx = patches.Rectangle((69.5, 87.5), 29.0, 5.5, facecolor='#0f172a', edgecolor='none')
ax.add_patch(hdr_rx)
ax.text(84.0, 90.25, "RECEIVER: HOSPITAL EDGE SERVER", ha='center', va='center',
        fontsize=7.0, fontweight='bold', color='#ffffff')

# Sub-block: Edge AI Reconstruction Engine (VarNet)
# y: [54.0, 85.0] (height 31.0)
brx1_box = patches.Rectangle((70.7, 54.0), 26.6, 31.0, facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=0.8)
ax.add_patch(brx1_box)
brx1_hdr = patches.Rectangle((70.7, 81.0), 26.6, 4.0, facecolor='#ede9fe', edgecolor='#ddd6fe', linewidth=0.6)
ax.add_patch(brx1_hdr)
ax.text(84.0, 83.0, "EDGE AI RECONSTRUCTION (VarNet)", ha='center', va='center',
        fontsize=6.3, fontweight='bold', color='#6d28d9')

ax.text(71.8, 76.5, "Input Stream:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(79.0, 76.5, r"Fused $\mathbf{Y}_{\mathrm{URLLC}} \cup \mathbf{Y}_{\mathrm{eMBB}}$", fontsize=6.3, color='#334155')

ax.text(71.8, 70.0, "Reconstruction:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(80.2, 70.0, r"$\hat{\mathbf{X}} = \mathcal{R}_{\boldsymbol{\theta}}(\mathbf{Y})$ ($1.8\,\mathrm{s}$ GPU)", fontsize=6.3, color='#6d28d9')

ax.text(71.8, 63.5, "Standard QoS:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(79.8, 63.5, r"$\mathrm{PSNR} > 25.3\,\mathrm{dB}$, $\mathrm{SSIM} > 0.86$", fontsize=6.3, color='#334155')

tag_rx1 = patches.Rectangle((71.8, 56.0), 24.4, 4.8, facecolor='#f5f3ff', edgecolor='#c4b5fd', linewidth=0.6)
ax.add_patch(tag_rx1)
ax.text(84.0, 58.4, "Physical Residual: PASSED (Null-Space Blind)", ha='center', va='center',
        fontsize=5.8, fontstyle='italic', color='#7c3aed')

# Downward Arrow Recon -> Semantic Verifier
ax.annotate('', xy=(84.0, 49.0), xytext=(84.0, 54.0),
            arrowprops=dict(arrowstyle="-|>", color='#6d28d9', lw=1.3, mutation_scale=8))
ax.text(85.5, 51.5, r"Reconstructed $\hat{\mathbf{X}}$ + Token $\boldsymbol{\theta}$", ha='left', va='center',
        fontsize=5.8, fontweight='bold', color='#6d28d9')

# Sub-block: Layer 4 Semantic Audit & Decision Gate
# y: [18.0, 49.0] (height 31.0)
brx2_box = patches.Rectangle((70.7, 18.0), 26.6, 31.0, facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=0.8)
ax.add_patch(brx2_box)
brx2_hdr = patches.Rectangle((70.7, 45.0), 26.6, 4.0, facecolor='#ffe4e6', edgecolor='#fecdd3', linewidth=0.6)
ax.add_patch(brx2_hdr)
ax.text(84.0, 47.0, "LAYER 4: SEMANTIC AUDIT & DECISION GATE", ha='center', va='center',
        fontsize=6.3, fontweight='bold', color='#be123c')

ax.text(71.8, 40.5, "Task Verifier:", fontsize=6.3, fontweight='bold', color='#0f172a')
ax.text(79.0, 40.5, r"CHO Score $z_{\mathrm{recon}}$ (Computed in $< 12\,\mathrm{ms}$)", fontsize=6.3, color='#be123c')

# Structured decision cards
# Pass branch (top micro-card)
card_pass = patches.Rectangle((71.8, 30.5), 24.4, 7.5, facecolor='#f0fdf4', edgecolor='#86efac', linewidth=0.7)
ax.add_patch(card_pass)
ax.text(73.0, 35.0, r"$\mathbf{z \geq 1.5}$ (AUDIT PASSED)", fontsize=6.2, fontweight='bold', color='#15803d')
ax.text(73.0, 32.2, r"Certified Safe $\to$ PACS Workstation", fontsize=5.8, color='#166534')

# Fail branch (bottom micro-card)
card_fail = patches.Rectangle((71.8, 20.0), 24.4, 8.5, facecolor='#fef2f2', edgecolor='#fca5a5', linewidth=0.7)
ax.add_patch(card_fail)
ax.text(73.0, 25.8, r"$\mathbf{z < 1.5}$ (AUDIT FAILED)", fontsize=6.2, fontweight='bold', color='#b91c1c')
ax.text(73.0, 22.2, r"Erasure Trigger $\Rightarrow$ Targeted S-NACK", fontsize=5.8, fontweight='bold', color='#dc2626')

# =============================================================================
# FORWARD FLOW ARROWS (TX -> RAN -> RX)
# Gap 1: x in [30.5, 36.0] (width 5.5, center 33.25)
# Gap 2: x in [64.0, 69.5] (width 5.5, center 66.75)
# =============================================================================
# URLLC Flow (y = 69.5)
ax.annotate('', xy=(36.0, 69.5), xytext=(30.5, 69.5),
            arrowprops=dict(arrowstyle="-|>", color='#ea580c', lw=1.8, mutation_scale=10))
ax.text(33.25, 72.0, "URLLC", ha='center', va='bottom', fontsize=6.2, fontweight='bold', color='#c2410c')
ax.text(33.25, 67.2, r"$\mathcal{K}_{\mathrm{diag}}+\boldsymbol{\theta}$", ha='center', va='top', fontsize=5.6, color='#c2410c')

ax.annotate('', xy=(69.5, 69.5), xytext=(64.0, 69.5),
            arrowprops=dict(arrowstyle="-|>", color='#ea580c', lw=1.8, mutation_scale=10))
ax.text(66.75, 72.0, "URLLC", ha='center', va='bottom', fontsize=6.2, fontweight='bold', color='#c2410c')
ax.text(66.75, 67.2, r"$\mathcal{K}_{\mathrm{diag}}+\boldsymbol{\theta}$", ha='center', va='top', fontsize=5.6, color='#c2410c')

# eMBB Flow (y = 33.5)
ax.annotate('', xy=(36.0, 33.5), xytext=(30.5, 33.5),
            arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=1.8, mutation_scale=10))
ax.text(33.25, 36.0, "eMBB", ha='center', va='bottom', fontsize=6.2, fontweight='bold', color='#475569')
ax.text(33.25, 31.2, r"$\mathcal{K}_{\mathrm{bulk}}$", ha='center', va='top', fontsize=5.6, color='#475569')

ax.annotate('', xy=(69.5, 33.5), xytext=(64.0, 33.5),
            arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=1.8, mutation_scale=10))
ax.text(66.75, 36.0, "eMBB", ha='center', va='bottom', fontsize=6.2, fontweight='bold', color='#475569')
ax.text(66.75, 31.2, r"$\mathcal{K}_{\mathrm{bulk}}$", ha='center', va='top', fontsize=5.6, color='#475569')

# =============================================================================
# CLOSED-LOOP RETURN PATH: S-NACK RETRANSMISSION (BOTTOM CONTROL PLANE)
# =============================================================================
# Right-angle arrow from Receiver Fail branch (x=84.0, y=16.5) -> (x=76.5, y=7.0)
arrow_snack_down = patches.FancyArrowPatch((84.0, 16.5), (76.5, 7.0),
                                           connectionstyle="angle,angleA=-90,angleB=180,rad=3.0",
                                           arrowstyle='-|>,head_width=2.2,head_length=2.8',
                                           color='#dc2626', linestyle='--', linewidth=1.4)
ax.add_patch(arrow_snack_down)
ax.text(80.5, 9.8, "Audit Fail", ha='center', va='bottom', fontsize=5.6, fontweight='bold', color='#b91c1c')

# Central S-NACK Banner (x: 23.5 to 76.5, width 53.0, height 7.0)
snack_box = patches.Rectangle((23.5, 3.5), 53.0, 7.0, facecolor='#fef2f2', edgecolor='#fca5a5', linewidth=0.9)
ax.add_patch(snack_box)
ax.text(50.0, 7.7, "CLOSED-LOOP S-NACK RETRANSMISSION PROTOCOL", ha='center', va='center',
        fontsize=6.5, fontweight='bold', color='#991b1b')
ax.text(50.0, 5.0, r"Selective request for missing high-$\gamma_k$ trajectories ($\Delta k \approx 1.2\,\mathrm{MB}$, Round-Trip Latency $\Delta t \approx 15\,\mathrm{ms}$)",
        ha='center', va='center', fontsize=5.8, color='#7f1d1d')

# Right-angle arrow from S-NACK banner (x=23.5, y=7.0) -> Transmitter DARDO (x=16.0, y=16.5)
arrow_snack_up = patches.FancyArrowPatch((23.5, 7.0), (16.0, 16.5),
                                         connectionstyle="angle,angleA=180,angleB=90,rad=3.0",
                                         arrowstyle='-|>,head_width=2.2,head_length=2.8',
                                         color='#dc2626', linestyle='--', linewidth=1.4)
ax.add_patch(arrow_snack_up)
ax.text(19.5, 9.8, r"Resend $\Delta k$", ha='center', va='bottom', fontsize=5.6, fontweight='bold', color='#b91c1c')

# Save high-res PDF and PNG
fig_dir = os.path.dirname(os.path.abspath(__file__))
out_pdf = os.path.join(fig_dir, 'fig4_architecture.pdf')
out_png = os.path.join(fig_dir, 'fig4_architecture.png')

plt.savefig(out_pdf, format='pdf', dpi=300)
plt.savefig(out_png, format='png', dpi=300)
plt.close()

print("Successfully generated publication Figure 4:")
print(" -", out_pdf)
print(" -", out_png)
