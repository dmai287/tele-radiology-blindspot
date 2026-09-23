"""
src/observer.py
===============
Channelised Hotelling Observer (CHO) implementation.
IEEE ICOIN 2027
"""

import numpy as np

class ChannelisedHotellingObserver:
    """
    Channelised Hotelling Observer (CHO) modeling human visual cortex
    frequency decomposition and pre-whitened matched-filter detection.
    """
    def __init__(self, matrix_size=64, bandwidths=(2.0, 4.0, 8.0, 16.0)):
        self.matrix_size = matrix_size
        self.bandwidths = bandwidths
        self.channels = self._build_gabor_channels()
        
    def _build_gabor_channels(self):
        y, x = np.ogrid[-self.matrix_size//2:self.matrix_size//2, -self.matrix_size//2:self.matrix_size//2]
        r = np.sqrt(x**2 + y**2)
        channels = []
        for b in self.bandwidths:
            g = np.exp(-0.5 * ((r - b) / (b * 0.4))**2)
            g /= np.linalg.norm(g)
            channels.append(g.flatten())
        return np.array(channels)
        
    def extract_features(self, images):
        """Extract Gabor channel responses for an array of images."""
        flat_images = images.reshape(len(images), -1)
        return flat_images @ self.channels.T
        
    def fit_and_evaluate(self, present_features, absent_features):
        """Compute matched-filter SNR d' and template weights w."""
        delta_v = np.mean(present_features, axis=0) - np.mean(absent_features, axis=0)
        cov_p = np.cov(present_features, rowvar=False)
        cov_a = np.cov(absent_features, rowvar=False)
        cov_matrix = 0.5 * (cov_p + cov_a) + 1e-6 * np.eye(len(delta_v))
        
        w = np.linalg.solve(cov_matrix, delta_v)
        d_prime = np.sqrt(np.dot(delta_v, w))
        return d_prime, w
