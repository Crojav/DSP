#A1Part1.py

import numpy as np
from scipy.io.wavfile import read
import sys
sys.path.append('software/models')

import utilFunctions as UF

def readAudio(inputFile='../../sounds/piano.wav'):
    print("Input File: ", inputFile)
    (fs, x) = UF.wavread(inputFile)	
    # The function should return a numpy array that contains 10 samples of the audio.
    y = x[50000:50010]
    print(y, "dtype=", y.dtype)
    print("SampleRate :", fs)

print(readAudio())
