import numpy as np

def am_modulate(carrier_freq, message_signal, fs=1000):
    t = np.linspace(0, len(message_signal)/fs, len(message_signal), endpoint=False)
    carrier = np.cos(2*np.pi*carrier_freq*t)
    return message_signal * carrier

def fm_modulate(carrier_freq, message_signal, freq_dev=50, fs=1000):
    t = np.linspace(0, len(message_signal)/fs, len(message_signal), endpoint=False)
    integral = np.cumsum(message_signal)/fs
    return np.cos(2*np.pi*carrier_freq*t + 2*np.pi*freq_dev*integral)
