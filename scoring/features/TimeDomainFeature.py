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
