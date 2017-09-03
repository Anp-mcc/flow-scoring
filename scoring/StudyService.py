from scoring.StudyConfig import StudyConfig
from scoring.FrameProvider import FrameProvider
from scoring.features.FeatureSet import FeatureSet
from scoring.factories import create_scoring_provider
from scoring.models import StudyModel
from mongoengine import connect


def fluent(fn):
    def wrap(*args, **kwargs):
        fn(*args, **kwargs)
        return args[0]
    return wrap


class StudyBuilder:

    @classmethod
    def create_study(cls):
        return StudyBuilder()

    @classmethod
    def __load_samples(self, file_path):
        with open(file_path, 'r') as signal_file:
            samples = signal_file.readline().split(',')
            return [int(raw_sample) for raw_sample in samples]

    @fluent
    def with_signal(self, signal_path):
        self.signal_samples = self.__load_samples(signal_path)

    @fluent
    def with_scoring(self, signal_path):
        self.scoring_samples = self.__load_samples(signal_path)

    @fluent
    def with_config(self, config_path):
        self.config = StudyConfig.load_config(config_path)

    def build(self):
        feature_types = self.config.feature_types
        scoring_frequency = self.config.scoring_frequency
        (frequency, frame_size) = self.config.signal_config
        scoring_frame_size = int(frame_size/frequency)*scoring_frequency
        frame_provider = FrameProvider(self.signal_samples, frequency, frame_size)
        scoring_provider = create_scoring_provider(scoring_frame_size, scoring_frequency, self.scoring_samples)
        feature_set = FeatureSet(frame_provider, scoring_provider, feature_types)
        return StudyService(self.config.study_name, feature_set)


class StudyService:

    def __init__(self, name, feature_set):
        self.name = name
        self.feature_set = feature_set

    def create_study(self):
        feature_set = []
        for feature in self.feature_set:
            feature_set.append(feature)

        return StudyModel(name=self.name, features=feature_set)

    @classmethod
    def run_study(cls, signal_path, scoring_path, config_path):
        study_service = StudyBuilder.create_study().with_signal(signal_path).with_config(config_path).with_scoring(scoring_path).build()
        study = study_service.create_study()
        connect(db="default", host='mongodb://localhost')
        study.save()

