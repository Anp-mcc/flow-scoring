from scoring.features.Feature import Feature


def get_feature(feature_type):
    if feature_type == "min":
        return Feature(func=min)
    if feature_type == "max":
        return Feature(func=max)


class FeatureSet:

    def __init__(self, frame_provider, features):
        self.frame_provider = frame_provider
        self.features = features

    def __iter__(self):
        for frame in self.frame_provider:
            for feature_type in self.features:
                feature = get_feature(feature_type)
                yield feature.calculate(frame)

