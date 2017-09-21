import numpy as np


class FrequencyFeature:

    def __init__(self, type):
        self.type = type
        self.error = False
        self.value = None

    def domain(self):
        return "frequency"

    @property
    def is_error(self):
        return self.error

    @property
    def feature_value(self):
        return self.value

    def calculate(self, freq_domain, sampling_rate):
        T = 1/sampling_rate
        freq_level = np.linspace(0.0, 1.0/(2.0*T), len(freq_domain))
        max_component = np.max(freq_domain)
        index_of_max = np.argwhere(freq_domain == max_component)

        if len(index_of_max) != 1:
            self.error = True
        else:
            [[max_freq]] = freq_level[index_of_max]

            self.value = max_freq
