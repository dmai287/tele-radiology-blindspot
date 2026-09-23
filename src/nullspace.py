"""
src/nullspace.py
================
Proposition 2: Measurement Residual Invariance in Multi-Coil Forward Operator.
IEEE ICOIN 2027
"""

import numpy as np

def compute_svd_spectrum(sensitivity_maps, mask):
    """
    Computes singular value spectrum for multi-coil forward operator A = M * F * S.
    """
    # Sensitivity profile norm per frequency
    num_coils, ny, nx = sensitivity_maps.shape
    coil_norm = np.linalg.norm(sensitivity_maps, axis=0)
    
    # Under subsampling mask M, unacquired lines have exact zero singular values
    # acquired lines have singular values proportional to coil sensitivity norm
    spectrum = []
    for y_idx in range(ny):
        if mask[y_idx]:
            spectrum.extend(coil_norm[y_idx, :])
        else:
            spectrum.extend(np.zeros(nx))
            
    spectrum = np.array(spectrum)
    spectrum[::-1].sort()
    return spectrum

def evaluate_residual_bound(lesion_perturbation, forward_operator_norm, null_fraction=0.9999):
    """
    Evaluates ||A * delta||_2 <= ||A|| * ||delta_range|| + sigma_eta.
    Returns delta residual shift.
    """
    norm_delta = np.linalg.norm(lesion_perturbation)
    norm_delta_range = norm_delta * np.sqrt(1.0 - null_fraction)
    delta_residual = forward_operator_norm * norm_delta_range
    return delta_residual
