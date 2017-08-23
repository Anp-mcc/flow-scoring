from pandas import read_csv


def load_signal_frames(signal_file, signal_config):
    signals = read_csv(signal_file)

    for index, signal in signals.iterrows():
        config = signal_config[index]
        (frequency, frame_width) = config
        frame_samples = frequency*frame_width
        frame_number = len(signal)/frame_samples
        signal.values.reshape(frame_samples, frame_number)

    return signals


class Study:

    def __init__(self, config):
        self.config = config

    def perform_with(self, signal_file):
        signal_config = self.config.signal_config
        frames = load_signal_frames(signal_file, signal_config)
        print(frames)