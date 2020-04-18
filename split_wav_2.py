import os
import librosa
import zipfile
import soundfile as sf
import io
import numpy as np
import math


WAV_PATH = '/home/PATH/.../AUDIO.wav'
SPLIT_PATH = '/home/PATH/.../AUDIO.wav'
final_wav = []

def read_n_split_wav(wavpath, splitPath, start_time, stop_time):
    signal, sample_rate = librosa.load(wavpath)  # not resampled at 22050 Hz it is in original sample rate
    check1 = int(float(start_time * sample_rate))
    check2 = int(float(stop_time * sample_rate))
    for t, samples in enumerate(signal):
        if (t >= check1) and (t <= check2):
            final_wav.append(samples)

    sf.write((splitPath), final_wav, sample_rate)
    # sf.write((SPLIT_PATH + myWav.name), signal[int(start_time):int(stop_time)], sample_rate)

if __name__ == "__main__":
    read_n_split_wav(WAV_PATH, SPLIT_PATH, start_in_seconds, end_in_seconds)
    print('Done')
