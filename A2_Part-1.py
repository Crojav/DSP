
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

def genCos(A, f, phi, fs, t):

    T = t/fs  
    samples = 100
    n = np.arange(samples)
    x = A*np.cos(2*np.pi*f*n*T + phi)
    x_slice = x[:45:10]
    print('x :', x_slice)
    # [ 0.54030231, -0.63332387, -0.93171798, 0.05749049, 0.96724906]


A=1.0       # A (float) = amplitude of the sinusoid
f=10.0      # f (float) = frequency of the sinusoid in Hz
phi = 1.0   # phi (float) = initial phase of the sinusoid in radians
fs = 50.0   # fs (float) = sampling frequency of the sinusoid in Hz
t = 0.1     # t (float) = duration of the sinusoid (is second)
    
genCos(A, f, phi, fs, t)
