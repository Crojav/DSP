# A1-Part-4.py
"""! PYTHON 3 !"""

import numpy as np
from scipy.io.wavfile import read
import os, sys
import utilFunctions as UF
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '/models/'))

def downsampleAudio(inputFile,M):
    print("Input File: ", inputFile)
    (fs, x) = UF.wavread(inputFile)	
    print("x :", x)
    print("==========")
    print("SampleRate :", fs)
    print("==========")
    a_array = np.array(x)
    print(a_array)
    print("==========")
    print("a_array.size :",  a_array.size)
    print("==========")
    print("a_array.dtype :", a_array.dtype)
    print("==========")
    print("a_array[::16] :", a_array[::16])
    print("==========")
    Downsampled_16 = a_array[::16]


    outputFileDownsampled =  '../../sounds/output_sounds/' 'downsampled_' + os.path.basename(inputFile)[:-4] + '.wav'

    UF.wavwrite(outputFileDownsampled, 144000, Downsampled_16 )


    print("outputFileDownsampled :", outputFileDownsampled)


#the function from Part3 can be used to perform the downsampling of a signal contained in an array. To create a wav audio file from an array, you can use the wavwrite function from the utilFunctions module.

#downsampled_file = inputFile, "_downsampled.wav"
# print(inputFile, "_downsampled.wav")
#             =    UF.wavwrite(a_array[::16])
# create a wav audio file <input_name>_downsampled.wav

inputFile='../../sounds/vibraphone-C6.wav'
print(downsampleAudio(inputFile,16))


import re
s = inputFile
replaced1 = re.sub('../../sounds/', '', s)
replaced2 = re.sub('.wav', '', replaced1)
print("{}_downsampled.wav".format(replaced2))


#    y = x[50000:50010]

