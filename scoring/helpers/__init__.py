import numpy as np


def load_samples(file_path):
    with open(file_path, 'r') as signal_file:
        samples = signal_file.readline().split(',')
        return np.array([float(raw_sample) for raw_sample in samples])


def fast_fourier_transform(epoch, normalized=False):
    transform = np.fft.fft(epoch)
    transform[0] = 0 #Remove DC component

    if normalized:
        return transform/transform.sum()

    return transform
