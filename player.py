
import pyaudio
import numpy as np

p = pyaudio.PyAudio()

volume = 0.2  # range [0.0, 1.0]
bitRate = 8000  # sampling rate, Hz, must be integer

def play(song):
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=bitRate,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * song.astype(np.float32))

    stream.stop_stream()
    stream.close()

