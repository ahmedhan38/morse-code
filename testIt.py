import numpy as np
from scipy.io import wavfile
from scipy import signal

sample_rate = 7119
fs = 600

t = np.linspace(0, 1, 137614, False)
# amplitude = 1/sample_rate
amplitude = np.finfo(np.float32).max
data = amplitude * np.sin(2. * np.pi * sample_rate * t)

# #filtering with bandpass
# sos = signal.butter(7119,7119, 'bp', fs=600, output='sos')
# filtered = signal.sosfilt(sos, sig)


# Write the data to 'newname.wav'
wavfile.write("decoded_file.wav", sample_rate, data.astype(np.float32))