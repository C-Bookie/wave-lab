
import numpy as np

#raise and half
def rah(a):
    return (a+1)/2

#frequency, bitRate, dueration, phase
def sin(f, b, d, p=0.):
    s = f/b*2*np.pi     #step
    n = p*2*np.pi       #nudge
    return np.sin(np.arange(n, n+b*d*s, s))


def saw(f, b, d, p=0.):
    s = f/b*2
    n = p*2
    return (np.arange(n, n+b*d*s, s)%2)-1
def tri(f, b, d, p=0.):
    s = f/b*4
    n = p*4
    return np.absolute(np.arange(n, n+b*d*s, s)%4-2)-1

def squ(f, b, d, p=0.):
    s = f/b*2
    n = p*2
    return np.floor(np.arange(n, n+b*d*s, s)%2)*2-1
