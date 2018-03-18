
import pyaudio
import gen
import screen
import seq
import player


p = pyaudio.PyAudio()

volume = 0.2  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = 10.0  # in seconds, may be float
f1 = 440.0  # sine frequency, Hz, may be float
f2 = 20.0  # sine frequency, Hz, may be float
f3 = 10  # sine frequency, Hz, may be float



def test1():
    # generate samples, note conversion to float32 array
    s1 = gen.squ(f1, fs, duration, 1/2)
#    s2 = gen.sin(f2, fs, duration)
#    s3 = gen.squ(f3, fs, duration)

#    samples = np.nan_to_num(s1*(s2))/2
#    samples = s1 * gen.rah(s2) * gen.rah(s3)
    samples = s1

    screen.init()
    screen.draw(samples, fs / f1)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

def test2():
    a = seq.build(seq.track1, player.bitRate)

    screen.init()
    screen.draw(a, player.bitRate / seq.track1[0]["frequency"])

    b = gen.sin(440, player.bitRate, 10, 0)
    player.play(a)
    player.play(b)

