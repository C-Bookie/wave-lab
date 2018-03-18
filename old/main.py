
import pyaudio
import numpy as np

import screen

#raise and half
def rah(a):
    return (a+1)/2

def sin(f, b, d):
    return (np.sin(2*np.pi*np.arange(b*d)*f/b)).astype(np.float32)

def saw(f, b, d):
    return (((np.arange(b*d)/(b/f)*2)%2)-1).astype(np.float32)

def tri(f, b, d):
    return (np.absolute(((np.arange(b*d)/(b/f)*2)%4)-2)-1).astype(np.float32)

def squ(f, b, d):
    return (np.floor((np.arange(b*d)/(b/f)*2)%2)*2-1).astype(np.float32)

if __name__ == '__main__':

    p = pyaudio.PyAudio()

    volume = 0.2     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 10.0   # in seconds, may be float
    f1 = 440.0        # sine frequency, Hz, may be float
    f2 = 20.0        # sine frequency, Hz, may be float
    f3 = 11        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    s1 = sin(f1, fs, duration)
    s2 = sin(f2, fs, duration)
    s3 = squ(f3, fs, duration)

#    samples = np.nan_to_num(s1*(s2))/2
    samples = s1*rah(s2)*rah(s3)



    screen.init()
    screen.draw(samples, fs/f2)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

