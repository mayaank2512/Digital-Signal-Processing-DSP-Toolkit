import numpy as np

def compute_fft(signal, fs):
    n = len(signal)
    freq = np.fft.fftfreq(n, 1/fs)
    fft_vals = np.fft.fft(signal)
    return freq[:n//2], np.abs(fft_vals)[:n//2]
