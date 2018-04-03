# A1-Part-4.py

import sys, os
import numpy as np
import utilFunctions as UF


def downsampleAudio(inputFile,M):
   (fs, x) = UF.wavread(inputFile)
   x.astype(int)
   x_array = np.array(x)
   x_array_slice = x_array[::M] # equivalent to: x_array_slice[0:x_array.size:M]

   outputFile_name =   'downsampled_' + inputFile[13:]
   outputFile_path = '../../sounds/output_sounds/'
   name_and_path = outputFile_path + outputFile_name

   UF.wavwrite(x_array_slice, fs, name_and_path )


downsampleAudio('../../sounds/vibraphone-C6.wav', 16)
