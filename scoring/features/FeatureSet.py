from scoring.features.FeatureStrategy import FeatureStrategy
from scoring.features.FreqDomainFeature import FrequencyFeature
from scoring.features.TimeDomainFeature import HjorthActivityFeature
from scoring.features.TimeDomainFeature import HjorthMobilityFeature
from scoring.features.TimeDomainFeature import HjorthComplexityFeature
from scoring.features.TimeDomainFeature import ZeroCrossingFeature
from scoring.features.TimeDomainFeature import PetrosianFDFeature
from scoring.features.TimeDomainFeature import HjorthFdFeature
from scoring.features.TimeDomainFeature import EnergyFeature
from scoring.features.TimeDomainFeature import KatzFdFeature
from scoring.features.TimeDomainFeature import HurtsFdFeature
from scoring.factories import create_feature


def get_feature_strategy(feature_type):
    if feature_type == "min":
        return FeatureStrategy(func=min, type=feature_type)
    if feature_type == "max":
        return FeatureStrategy(func=max, type=feature_type)
    if feature_type == "freq":
        return FrequencyFeature(type=feature_type)
    if feature_type == "zero_c":
        return ZeroCrossingFeature(type=feature_type)
    if feature_type == "hj_activity":
        return HjorthActivityFeature(type=feature_type)
    if feature_type == "hj_mobility":
        return HjorthMobilityFeature(type=feature_type)
    if feature_type == "hj_complexity":
        return HjorthComplexityFeature(type=feature_type)
    if feature_type == "petros":
        return PetrosianFDFeature(type=feature_type)
    if feature_type == "hj_fractal":
        return HjorthFdFeature(type=feature_type)
    if feature_type == "katz_fractal":
        return KatzFdFeature(type=feature_type)
    if feature_type == "hurts_fractal":
        return HurtsFdFeature(type=feature_type)
    if feature_type == "energy":
        return EnergyFeature(type=feature_type)


class FeatureSet:

    def __init__(self, frame_provider, scoring_provider, features):
        self.scoring_provider = scoring_provider
        self.frame_provider = frame_provider
        self.features = features

    def __iter__(self):
        for index, frame in self.frame_provider:
            scoring_type = self.scoring_provider.get_by_position(index)
            for feature_type in self.features:
                feature_strategy = get_feature_strategy(feature_type)
                feature_value = feature_strategy.calculate(frame)
                yield create_feature(scoring_type, feature_value, feature_strategy.type)


