from scoring.FrameProvider import FrameProvider
from scoring.ScoringProvider import ScoringProvider
from scoring.models import FeatureModel


def create_scoring_provider(frame_size, frequency, samples):
    frame_provider = FrameProvider(samples, frequency, frame_size)
    return ScoringProvider(frame_provider)


def create_feature(scoring_type, value, feature_type):
    return FeatureModel(feature_class=scoring_type, feature_value=value, feature_type=feature_type)