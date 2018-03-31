# A1Part2.py

""" LET OP PYTHON 3 """


import numpy as np
from scipy.io.wavfile import read
import sys
sys.path.append('software/models')

import utilFunctions as UF


def minMaxAudio(inputFile='../../sounds/oboe-A4.wav'):
    # Input: inputFile: file path to the wav file Output: 
    print("Input File: ", inputFile)
    (fs, x) = UF.wavread(inputFile)
    min_val = np.min(abs(x))
    max_val = np.max(abs(x))	
    # Output: A tuple of the minimum and the maximum value of the audio samples, like: (min_val, max_val)
    print( "min_val:", min_val)
    print( "max val:", max_val)

print(minMaxAudio())

