"""
    Import a .wav file.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import scipy.io
from scipy.io.wavfile import write
translate_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


sample_rate, data = wavfile.read("decode_me.wav")
print("The sample rate is: " + str(sample_rate) + " Hz")
print("There are " + str(len(data)) + " samples.")
length = data.shape[0] / sample_rate
print(f"length = {length}s")

time = np.linspace(0., length, data.shape[0])
#plt.plot(time, data)           //Comment them out for the audio graph
#plt.plot(time, data)           //Comment them out for the audio graph
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
#plt.show()                     //Comment them out for the audio graph

