from scoring.features.FeatureStrategy import FeatureStrategy


def get_feature(feature_type):
    if feature_type == "min":
        return FeatureStrategy(func=min)
    if feature_type == "max":
        return FeatureStrategy(func=max)


class FeatureSet:

    def __init__(self, frame_provider, scoring_provider, features):
        self.scoring_provider = scoring_provider
        self.frame_provider = frame_provider
        self.features = features

    def __iter__(self):
        for index, frame in self.frame_provider:
            scoring_type = self.scoring_provider.get_by_position(index)
            for feature_type in self.features:
                feature = get_feature(feature_type)
                yield scoring_type, index, feature.calculate(frame)


