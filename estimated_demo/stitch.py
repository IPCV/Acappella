import scipy.io.wavfile as wav
import numpy as np
fs,a1=wav.read('llcp1.wav')
fs,a2=wav.read('llcp2.wav')
fs,a3=wav.read('llcp3.wav')
b=np.hstack([a1,a2,a3])
wav.write('llcp.wav',fs, b)
