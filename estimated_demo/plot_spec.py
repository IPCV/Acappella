import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import librosa
import librosa.display
import os
import pydub

from pathlib import Path

NFFT = 1022
HOP_LENGTH = 256
TARGET_SAMPLING_RATE = 16384
wav_files = Path('.').rglob('*.wav')
for file in wav_files:
    file_path = file.as_posix()
    if ('llcp_910' in file_path):
        file_name = os.path.basename(file_path)
        folder_path = os.path.dirname(file_path)
        output_path = os.path.join(folder_path, file_name[:-4] + '.png')
        y, sr = librosa.load(file_path, sr=16384)
        sound = pydub.AudioSegment.from_wav(file_path)
        sound.export(file_path[:-4]+'.mp3', format="mp3")

        stft = librosa.stft(y, n_fft=NFFT, hop_length=HOP_LENGTH)
        D = librosa.amplitude_to_db(np.absolute(stft),
                                    ref=np.max)
        librosa.display.specshow(D, sr=sr, hop_length=HOP_LENGTH, x_axis='time', cmap='Reds', y_axis='linear')
        plt.ylabel(None)
        plt.xlabel(None)
        plt.savefig(output_path, bbox_inches='tight')
        #plt.show()
