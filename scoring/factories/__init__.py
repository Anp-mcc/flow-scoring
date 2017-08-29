from scoring.FrameProvider import FrameProvider
from scoring.ScoringProvider import ScoringProvider


def create_scoring_provider(frame_size, frequency, samples):
    frame_provider = FrameProvider(samples, frequency, frame_size)
    return ScoringProvider(frame_provider)
