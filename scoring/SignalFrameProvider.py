import numpy as np


class FrameProvider:

    def __init__(self, samples, frequency, frame_size):
        self.samples = samples
        self.frequency = frequency
        self.frame_size = frame_size

    def __iter__(self):
        samples_count = len(self.samples)
        frames = np.reshape(self.samples, (self.frame_size, int(samples_count/self.frame_size)))

        for frame in frames:
            yield frame


