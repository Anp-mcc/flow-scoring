import numpy as np
import math


def mobility(epoch):
    return np.divide(np.std(np.diff(epoch, axis=0)),
                     np.std(epoch, axis=0))


class TimeDomainFeature:

    def __init__(self, type):
        self.type = type
        self.value = np.nan

    def domain(self):
        return "time"

    @property
    def is_error(self):
        return False

    @property
    def feature_value(self):
        return self.value


class KatzFdFeature(TimeDomainFeature):

    def total_length(srlf, epoch):
        acc_length = 0
        for i in range(len(epoch)-1):
            distance = np.sqrt(1 + (epoch[i] - epoch[i+1])**2)
            acc_length += distance
        return acc_length

    def calc_distance(self, epoch):
        dist = [0]
        for i in range(1, len(epoch)):
            dist_val = np.sqrt((0-i) ** 2 + (epoch[0] - epoch[i])**2)
            dist.append(dist_val)

        return np.max(dist)

    def calculate(self, epoch):
        L = self.total_length(epoch)
        d = self.calc_distance(epoch)

        self.value = (np.log(L)/np.log(d))


class HurtsFdFeature(TimeDomainFeature):

    def calculate(self, epoch):

        lags = range(2, 100)
        tau = [np.sqrt(np.nanstd(np.subtract(epoch[lag:], epoch[:-lag]))) for lag in lags]
        poly = np.polyfit(np.log(lags), np.log(tau), 1)

        self.value = poly[0]*2.0


class EnergyFeature(TimeDomainFeature):

    def calculate(self, epoch):
        self.value = np.sum([sample**2 for sample in epoch])


class PetrosianFDFeature(TimeDomainFeature):

    def calculate(self, epoch):
        signal_change = 0
        points_diff = np.diff(epoch)

        for i in range(1, len(points_diff)):
            if points_diff[i] *points_diff[i-1] < 0:
                signal_change += 1

        n = len(epoch)

        self.value = np.log10(n)/(np.log10(n) + np.log10(n/n+0.4*signal_change))


class HjorthFdFeature(TimeDomainFeature):

    def calculate(self, epoch):
        k_max = 3
        L = []
        x = []
        N = len(epoch)
        for k in range(1,k_max):
            Lk = []

            for m in range(k):
                Lmk = 0
                for i in range(1, int(np.floor((N-m)/k))):
                    Lmk += np.abs(epoch[m+i*k] - epoch[m+i*k-k])

                Lmk = Lmk*(N - 1)/np.floor((N - m) / k) / k
                Lk.append(Lmk)

            L.append(np.log(np.nanmean(Lk)))   # Using the mean value in this window to compare similarity to other windows
            x.append([np.log(float(1) / k), 1])

        (p, r1, r2, s)= np.linalg.lstsq(x, L)  # Numpy least squares solution

        self.value = p[0]


class HjorthActivityFeature(TimeDomainFeature):

    @property
    def is_error(self):
        return math.isnan(self.value)

    def calculate(self, epoch):
        self.value = np.var(epoch, axis=0)


class HjorthMobilityFeature(TimeDomainFeature):

    @property
    def is_error(self):
        return math.isnan(self.value)

    def calculate(self, epoch):
        self.value = mobility(epoch)


class HjorthComplexityFeature(TimeDomainFeature):

    @property
    def is_error(self):
        return math.isnan(self.value)

    def calculate(self, epoch):
        self.value = np.divide(mobility(np.diff(epoch, axis=0)),
                               mobility(epoch))


class ZeroCrossingFeature(TimeDomainFeature):

    def calculate(self, epoch):
        self.value = (np.diff(np.sign(epoch)) != 0).sum()
