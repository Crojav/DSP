
import numpy as np
import sys


def genSine(A, f, phi, fs, t):
    """
    Inputs:
    A (float) = amplitude of the sinusoid
    f (float) = frequency of the sinusoid in Hz
    phi (float) = initial phase of the sinusoid in radians
    fs (float) = sampling frequency of the sinusoid in Hz
    t (float) = duration of the sinusoid (is second)
    Output:
    The function should return a numpy array
    x (numpy array) = The generated sinusoid (use np.cos())
    """
## Your code here

import numpy as np
import math
     
#    in_array = [0, math.pi / 2, np.pi / 3, np.pi]
#    print ("Input array : \n", in_array)
     
#    cos_Values = np.cos(in_array)
#    print ("\nCosine values : \n", cos_Values)


import math

def genCos(A, f, phi, fs, t):
    in_array = [A, f, phi, fs, t]
    # fs > 2*f

    print ("Input array : \n", in_array)

    cos_Values = np.cos(in_array)
    print ("\nCosine values : \n", cos_Values)

    # [ 0.54030231, -0.63332387, -0.93171798, 0.05749049, 0.96724906]

    a = np.cos(np.array([A, f]))
    print('a = ', a)

A=1.0     # A (float) = amplitude of the sinusoid
f=10.0    # f (float) = frequency of the sinusoid in Hz
phi=1.0   # phi (float) = initial phase of the sinusoid in radians
fs=50.0   # fs (float) = sampling frequency of the sinusoid in Hz
t=0.1     # t (float) = duration of the sinusoid (is second)








print(genCos(A, f, phi, fs, t))
