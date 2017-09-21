from scoring.helpers import load_samples
from scoring.helpers import fast_fourier_transform
from scoring.features.FeatureSet import get_feature_strategy
import numpy as np
import matplotlib.pyplot as plt


class SignalReport:

    def __init__(self, feature_dict):
        self.feature_dict = feature_dict

    def histogram(self):
        pass

    def percentile(self):
        petros = self.feature_dict["petros"]
        plt.plot(petros)
        plt.show()
        for key, values in self.feature_dict.items():

            p50 = np.percentile(values, 50)
            p75 = np.percentile(values, 75)
            p90 = np.percentile(values, 90)
            p95 = np.percentile(values, 95)
            p99 = np.percentile(values, 99)

            print("{0} 50% percentile = {1}".format(key, p50))
            print("{0} 75% percentile = {1}".format(key, p75))
            print("{0} 90% percentile = {1}".format(key, p90))
            print("{0} 95% percentile = {1}".format(key, p95))
            print("{0} 99% percentile = {1}".format(key, p99))

        return self


class SignalAnalysis:

    def __init__(self, sampling_rate, epoch_len):
        self.sampling_rate = sampling_rate
        self.epoch_len = epoch_len
        self.feature_dict = {}
        self.feature_list = ["petros", "hj_fractal", "katz_fractal", "hurts_fractal"]


    def execute(self, samples):
        epoch_size = self.sampling_rate * self.epoch_len
        start = 0
        offset = epoch_size

        def add_to_features(type, value):
            if type in self.feature_dict.keys():
                self.feature_dict[type].append(value)
            else:
                self.feature_dict[type] = [value]

        while True:
            epoch = samples[start: offset]
            if not epoch.size:
                break

            fourier_transform = fast_fourier_transform(epoch, normalized=True)
            fourier_abs = np.abs(fourier_transform)
            freq_domain = fourier_abs[:len(fourier_transform)//2]

            for feature_type in self.feature_list:
                feature_strategy = get_feature_strategy(feature_type)

                if feature_strategy.domain() is "frequency":
                    feature_strategy.calculate(freq_domain, self.sampling_rate)
                else:
                    feature_strategy.calculate(epoch)

                if not feature_strategy.is_error:
                    add_to_features(feature_type, feature_strategy.feature_value)
                else:
                    continue

            start += epoch_size
            offset += epoch_size

    def report(self):
        return SignalReport(self.feature_dict)


def main():
    samples = load_samples('Flow.csv')
    analysis = SignalAnalysis(32, 60)
    analysis.execute(samples)
    analysis.report().percentile()

if __name__ == "main":
    main()

main()