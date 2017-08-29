import numpy as np


class FrameProvider:

    def __init__(self, samples, frequency, frame_size):
        self.samples = samples
        self.frequency = frequency
        self.frame_size = frame_size

    def __len__(self):
        return int(len(self.samples)/self.frame_size)

    def next_position(self, index):
        return (1+index)*int(self.frame_size/self.frequency)

    def __iter__(self):
        samples_count = len(self.samples)
        frames = np.reshape(self.samples, (int(samples_count/self.frame_size), self.frame_size))

        for value, frame in enumerate(frames):
            yield self.next_position(value), frame


