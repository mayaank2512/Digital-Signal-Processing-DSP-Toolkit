from scipy.signal import butter, lfilter

def low_pass(signal, cutoff, fs, order=5):
    b, a = butter(order, cutoff/(0.5*fs), btype='low')
    return lfilter(b, a, signal)

def high_pass(signal, cutoff, fs, order=5):
    b, a = butter(order, cutoff/(0.5*fs), btype='high')
    return lfilter(b, a, signal)

def band_pass(signal, lowcut, highcut, fs, order=5):
    b, a = butter(order, [lowcut/(0.5*fs), highcut/(0.5*fs)], btype='band')
    return lfilter(b, a, signal)
