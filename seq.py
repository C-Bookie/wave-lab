
import gen
import numpy as np


track1 = [{
    "wave":"sin",
    "duration":10.,
    "frequency":440.,
    "phase":0.5
},{
    "wave":"squ",
    "duration":10.,
    "frequency":440.,
    "phase":0.5
}]

def build(track, bitRate):
    print(track)
    a = np.empty([0], np.float32)
    for b in track:
        c = getattr(gen,b["wave"])(b["frequency"], bitRate, b["duration"], b["phase"])
        a = np.concatenate([a, c])
    return a

