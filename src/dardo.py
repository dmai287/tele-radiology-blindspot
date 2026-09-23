"""
src/dardo.py
============
Diagnostic-Aware Rate-Distortion Optimization (DARDO) algorithm implementation.
IEEE ICOIN 2027
"""

import numpy as np

def compute_task_spectral_profile(matrix_size=(320, 320), lesion_radius_px=2.5):
    """
    Step 1: Compute task spectral density W(kx, ky) = |F{w}|^2
    for a focal acute stroke template.
    """
    ny, nx = matrix_size
    y, x = np.ogrid[-ny//2:ny//2, -nx//2:nx//2]
    r = np.sqrt(x**2 + y**2)
    w = np.exp(-0.5 * (r / lesion_radius_px)**2)
    W_2d = np.abs(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(w))))**2
    return W_2d / np.max(W_2d)

def compute_diagnostic_gradient_density(W_2d, num_coils=16):
    """
    Step 2: Channel utility scoring.
    Rank phase-encoding trajectories k by diagnostic gradient density:
    gamma_k = sum_y W(k, y) * ||F S_k||_2
    """
    num_ky = W_2d.shape[0]
    coil_profile = np.ones((num_ky, W_2d.shape[1])) * np.sqrt(num_coils)
    gamma_k = np.sum(W_2d * coil_profile, axis=1)
    return gamma_k / np.max(gamma_k)

def dardo_allocate_trajectories(gamma_k, acceleration=8, num_acs=16):
    """
    Step 3: Greedy trajectory selection under rate constraint.
    Budget M = num_ky // acceleration.
    """
    num_ky = len(gamma_k)
    budget = num_ky // acceleration
    mask = np.zeros(num_ky, dtype=bool)
    
    # Center autocalibration lines
    center = num_ky // 2
    acs_start = center - num_acs // 2
    acs_end = center + num_acs // 2
    mask[acs_start:acs_end] = True
    
    remaining = budget - np.sum(mask)
    if remaining > 0:
        unselected = np.where(~mask)[0]
        sorted_indices = unselected[np.argsort(-gamma_k[unselected])]
        mask[sorted_indices[:remaining]] = True
        
    return mask

def tag_5g_slices(mask, gamma_k, qci_threshold=0.20):
    """
    Step 4: 5G Network Slicing & QoS Tagging.
    Tag high-gamma_k packets with URLLC QCI 1/65 (BLER < 10^-5),
    and bulk anatomy with eMBB best-effort slice.
    """
    indices = np.where(mask)[0]
    urllc = [idx for idx in indices if gamma_k[idx] >= qci_threshold]
    embb = [idx for idx in indices if gamma_k[idx] < qci_threshold]
    return np.array(urllc), np.array(embb)
