import numpy as np

def sine_wave(freq, duration, fs=1000):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    return t, np.sin(2 * np.pi * freq * t)

def square_wave(freq, duration, fs=1000):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    return t, np.sign(np.sin(2 * np.pi * freq * t))

def sawtooth_wave(freq, duration, fs=1000):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    return t, 2*(t*freq - np.floor(0.5 + t*freq))
