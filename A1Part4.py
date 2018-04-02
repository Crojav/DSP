# A1-Part-4.py
"""! PYTHON 3 !"""

import numpy as np
from scipy.io.wavfile import read
import sys
import utilFunctions as UF


def downsampleAudio(inputFile,M):
    print("Input File: ", inputFile)
    (fs, x) = UF.wavread(inputFile)	
    print("x :", x)
    print("SampleRate :", fs)
    ara = np.array(x)
    print(ara)
    print("dtype :", ara.dtype)

    a = np.arange(0,44100,16)
    print("a :", a)
    print("ara[::16] :", ara[::16])
    print("a.dtype :", a.dtype)
# dtype=int16

#the function from Part3 can be used to perform the downsampling of a signal contained in an array. To create a wav audio file from an array, you can use the wavwrite function from the utilFunctions module.

#downsampled_file = inputFile, "_downsampled.wav"
# print(inputFile, "_downsampled.wav")
#             =    UF.wavwrite()
# create a wav audio file <input_name>_downsampled.wav

inputFile='../../sounds/vibraphone-C6.wav'
print(downsampleAudio(inputFile,16))


import re
s = inputFile
replaced1 = re.sub('../../sounds/', '', s)
replaced2 = re.sub('.wav', '', replaced1)
print("{}_downsampled.wav".format(replaced2))


#    y = x[50000:50010]

