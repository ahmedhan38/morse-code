import time
from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

import scipy.io
from scipy.io.wavfile import write

translate_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-'}

message = "Ahmedhan"
message = " ".join(translate_dict[c] for c in message.upper())

def play_morse_code(message):
    for c in message:
        if c == ".":
            playsound("short.mp3")
            time.sleep(0.3)
        elif c == "-":
            playsound("long.mp3")
            time.sleep(0.3)
        elif c == "/" or c == " ":
            time.sleep(0.5)
        else:
            print("Invalid")


print(message)
play_morse_code(message)  # plays the sound of the encoded string

# Write kann keine strings auslesen dafuer habe ich den Ton direkt ausgegeben ohen die Datei
# wavfile.write("myName1.wav", 7119, message)


## Nachricht rueckwaerts
# reverse_dict = {v: k for k, v in translate_dict.items()}
# reverse_message = "".join(reverse_dict[c] for c in message.split(" "))
# print(reverse_message)


