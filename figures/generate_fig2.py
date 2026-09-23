import os
import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_dir = os.path.dirname(script_dir)
csv_path = os.path.join(repo_dir, "data", "exp1_classical_R468.csv")

if not os.path.exists(csv_path):
    # Fallback to local path if data is in same folder
    csv_path = os.path.join("data", "exp1_classical_R468.csv")

df = pd.read_csv(csv_path)

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11.5,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'font.family': 'sans-serif'
})

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15.8, 4.5), dpi=300)

accels = [4, 6, 8]
x_tick_labels = ['R = 4\n(-75.0% payload)', 'R = 6\n(-83.3% payload)', 'R = 8\n(-87.5% payload)']

# ==================== Panel 1: Conventional Network QoE ====================
c_psnr = '#08519c'
c_ssim = '#238b45'

psnr_means = [df[df['acceleration'] == a]['psnr_cf'].mean() for a in accels]
ssim_means = [df[df['acceleration'] == a]['ssim_cf'].mean() for a in accels]

ax1.set_xlabel('Acceleration Factor R (Undersampling)', fontweight='bold')
ax1.set_ylabel('Reconstructed PSNR (dB)', color=c_psnr, fontweight='bold')
l1 = ax1.plot(accels, psnr_means, 'o-', color=c_psnr, linewidth=2.5, markersize=8, label='PSNR (dB)')
ax1.tick_params(axis='y', labelcolor=c_psnr)
ax1.set_ylim(21, 35)
ax1.set_xlim(3.3, 8.7)
ax1.set_xticks(accels)
ax1.set_xticklabels(x_tick_labels, fontweight='bold')

ax1_twin = ax1.twinx()
ax1_twin.set_ylabel('Structural Similarity (SSIM)', color=c_ssim, fontweight='bold')
l2 = ax1_twin.plot(accels, ssim_means, 's--', color=c_ssim, linewidth=2.5, markersize=8, label='SSIM')
ax1_twin.tick_params(axis='y', labelcolor=c_ssim)
ax1_twin.set_ylim(0.72, 0.94)

lines = l1 + l2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower left', framealpha=0.95)
ax1.set_title('(a) Conventional Network QoE\n(Global metrics suggest safe transmission)', fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.5)

# ==================== Panel 2: Task-Based Detectability ====================
palette = {'27.0': '#e377c2', '64.0': '#d62728', '100.0': '#ff7f0e'}

for vol in [27.0, 64.0, 100.0]:
    sub = df[df['volume_mm3'] == vol]
    z_means = [sub[sub['acceleration'] == a]['z_recon'].mean() for a in accels]
    lbl = f"{int(vol)} " + r"$\mathrm{mm}^3$" + (' (acute stroke)' if vol == 64.0 else '')
    lw = 3.0 if vol == 64.0 else 2.0
    m = 'D' if vol == 64.0 else 'o'
    ax2.plot(accels, z_means, marker=m, linewidth=lw, markersize=8 if vol==64.0 else 6,
             color=palette[str(vol)], label=lbl)

ax2.axhline(1.5, color='black', linestyle=':', linewidth=1.8, label=r'Clinical threshold ($z_{\mathrm{crit}} = 1.5$)')
ax2.set_xlabel('Acceleration Factor R (Undersampling)', fontweight='bold')
ax2.set_ylabel(r'Diagnostic Detectability Score ($z_{\mathrm{recon}}$)', fontweight='bold')
ax2.set_title('(b) Task-Based Detectability\n(Diagnostic confidence collapses)', fontweight='bold')
ax2.set_xlim(3.3, 8.7)
ax2.set_xticks(accels)
ax2.set_xticklabels(x_tick_labels, fontweight='bold')
ax2.set_ylim(0.6, 2.4)
ax2.legend(loc='upper right', framealpha=0.95, fontsize=8.5)
ax2.grid(True, linestyle=':', alpha=0.5)

# ==================== Panel 3: The Tele-Radiology Hazard ====================
volumes = [10.0, 27.0, 64.0, 100.0, 200.0]
all_colors = {'10.0': '#8c564b', '27.0': '#e377c2', '64.0': '#d62728', '100.0': '#ff7f0e', '200.0': '#2ca02c'}

for vol in volumes:
    sub = df[df['volume_mm3'] == vol]
    rates = [sub[sub['acceleration'] == a]['silently_erased'].mean() * 100 for a in accels]
    lbl = f"{int(vol)} " + r"$\mathrm{mm}^3$" + (' (acute stroke)' if vol == 64.0 else '')
    lw = 3.2 if vol == 64.0 else 1.8
    ls = '-' if vol == 64.0 else '--'
    m = 'D' if vol == 64.0 else 'o'
    ax3.plot(accels, rates, marker=m, linestyle=ls, linewidth=lw, markersize=8 if vol==64.0 else 5.5,
             color=all_colors[str(vol)], label=lbl)

ax3.set_xlabel('Acceleration Factor R (Undersampling)', fontweight='bold')
ax3.set_ylabel('Silent Erasure Rate (%)', fontweight='bold')
ax3.set_title('(c) The Tele-Radiology Hazard\n(Silent pathology omission escalates)', fontweight='bold')
ax3.set_xlim(3.3, 8.7)
ax3.set_xticks(accels)
ax3.set_xticklabels(x_tick_labels, fontweight='bold')
ax3.set_ylim(0, 38)
ax3.legend(loc='upper left', framealpha=0.95, fontsize=8.5)
ax3.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
out_pdf = os.path.join(script_dir, 'fig2_network_rate_distortion_erasure.pdf')
out_png = os.path.join(script_dir, 'fig2_network_rate_distortion_erasure.png')
plt.savefig(out_pdf, bbox_inches='tight')
plt.savefig(out_png, bbox_inches='tight', dpi=300)
print('Figure 2 generated successfully with clean formatting!')
