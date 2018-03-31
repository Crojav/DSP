# DSP

### Digital representation of sound

digital converter (ADC) receives the discrete voltages from the sample and hold device, and ascribes a numerical value to each amplitude. This process of converting voltages to numbers is known as quantization. Those numbers are expressed in the computer as a string of binary digits (1 or 0). To play the sound back, we read the numbers from memory, and deliver those numbers to a digital-to-analog converter (DAC) at the same rate at which they were recorded. The DAC converts each number to a voltage, and communicates those voltages to an amplifier to increase the amplitude of the voltage.

 In order for a computer to represent sound accurately, many samples must be taken per second— many more than are necessary for filming a visual image. In fact, we need to take more than twice as many samples as the highest frequency we wish to record. (For an explanation of why this is so, see Limitations of Digital Audio on the next page.) If we want to record frequencies as high as 20,000 Hz, we need to sample the sound at least 40,000 times per second. The standard for compact disc recordings (and for ‘CD-quality’ computer audio) is to take 44,100 samples per second for each channel of audio. The number of samples taken per second is known as the sampling rate.

This means the computer can only accurately represent frequencies up to half the sampling rate. Any frequencies in the sound that exceed half the sampling rate must be filtered out before the sampling process takes place. This is accomplished by sending the electrical signal through a low-pass filter which removes any frequencies above a certain threshold. Also, when the digital signal (the stream of binary digits representing the quantized samples) is sent to the DAC to be re-converted into a continuous electrical signal, the sound coming out of the DAC will contain spurious high frequencies that were created by the sample and hold process itself. (These are due to the ‘sharp edges’ created by the discrete samples, as seen in the above example.) Therefore, we need to send the output signal through a low-pass filter, as well.

[https://docs.cycling74.com/max5/tutorials/msp-tut/mspdigitalaudio.html](https://docs.cycling74.com/max5/tutorials/msp-tut/mspdigitalaudio.html)


### Numpy

NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a [tuple](https://www.tutorialspoint.com/python/python_tuples.htm) of positive integers. In NumPy dimensions are called axes. The number of axes is rank.

For example, the coordinates of a point in 3D space [1, 2, 1] is an array of rank 1, because it has one axis. That axis has a length of 3. In the example pictured below, the array has rank 2 (it is 2-dimensional). The first dimension (axis) has a length of 2, the second dimension has a length of 3.



[https://docs.scipy.org/doc/numpy-1.12.0/user/quickstart.html](https://docs.scipy.org/doc/numpy-1.12.0/user/quickstart.html)

---

![https://www.youtube.com/watch?v=L06xKB6l7Ao](https://www.youtube.com/watch?v=L06xKB6l7Ao)


### A1-Part-1: Reading a wav audio file

Complete the function readAudio(inputFile) in the file A1Part1.py so that it
reads an audio file and returns 10 consecutive samples of the file starting from
the 50001th sample. This means that the output should exactly contain the
50001th sample to the 50010th sample (10 samples).
The input to the function is the file name (including the path) and the output
should be a numpy array containing 10 samples.

If you use the wavread function from the utilFunctions module the input
samples will be automatically converted to floating point numbers with a range
from -1 to 1, which is what we want.
Remember that in python, the index of the first sample of an array is 0 and
not 1.

If you run your code using piano.wav as the input, the function should return
the following numpy array with 10 samples: array([-0.06213569, -0.04541154, -
0.02734458, -0.0093997 , 0.00769066, 0.02319407, 0.03503525, 0.04309214, 0.04626606,
0.0441908], dtype=float32).

    def readAudio(inputFile):
    """
    Input:
    inputFile: the path to the wav file
    Output:
    The function should return a numpy array that
    contains 10 samples of the audio.
    """
    ## Your code here

---
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

---

    $ python3 A1Part1.py 
    Input File:  ../../sounds/piano.wav
    [-0.06213569 -0.04541154 -0.02734458 -0.0093997   0.00769066  0.02319407
      0.03503525  0.04309214  0.04626606  0.0441908 ] dtype= float32
    SampleRate : 44100

---

### A1-Part-2: Basic operations with audio

Complete the function minMaxAudio(inputFile) in the file A1Part2.py so that
it reads an audio file and returns the minimum and the maximum values of the
audio samples in that file.

The input to the function is the wav file name (including the path) and the
output should be two floating point values returned as a tuple.
If you run your code using oboe-A4.wav as the input, the function should
return the following output: (-0.83486432, 0.56501967)
def minMaxAudio(inputFile):

    """
    Input:
    inputFile: file path to the wav file
    Output:
    A tuple of the minimum and the maximum value of the audio
    samples, like: (min_val, max_val)
    """
    ## Your code here

---

    # A1Part2.py
    # python3 les1-hulp.py 
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
        min_val = np.min(x)
        max_val = np.max(x)	
        # Output: A tuple of the minimum and the maximum value of the audio samples, like: (min_val, max_val)
        print( "min_val max val:", min_val, max_val)

    print(readAudio())
    print(minMaxAudio())

---

    $ python3 A1Part2.py 
    Input File:  ../../sounds/oboe-A4.wav
    min_val: -0.834864
    max val: 0.56502

---

The basic slice syntax is i:j:k where i is the starting index, j is the stopping index, and k is the step (k\neq0). This selects the m elements (in the corresponding dimension) with index values i, i + k, ..., i + (m - 1) k where m = q + (r\neq0) and q and r are the quotient and remainder obtained by dividing j - i by k: j - i = q k + r, so that i + (m - 1) k < j.

    Example

    >>> x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> x[1:7:2]
    array([1, 3, 5])

[https://docs.scipy.org/doc/numpy-1.14.0/reference/arrays.indexing.html](https://docs.scipy.org/doc/numpy-1.14.0/reference/arrays.indexing.html)



---

[http://essentia.upf.edu/documentation/index.html](http://essentia.upf.edu/documentation/index.html)

