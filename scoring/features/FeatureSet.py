from scoring.features.FeatureStrategy import FeatureStrategy
from scoring.factories import create_feature


def get_feature_strategy(feature_type):
    if feature_type == "min":
        return FeatureStrategy(func=min, type=feature_type)
    if feature_type == "max":
        return FeatureStrategy(func=max, type=feature_type)


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


