from scoring.Study import Study
from scoring.Study import StudyConfig
from scoring.SignalFrameProvider import FrameProvider
from scoring.features.FeatureSet import FeatureSet

def fluent(fn):
    def wrap(*args,**kwargs):
        fn(*args,**kwargs)
        return args[0]
    return wrap


class StudyBuilder:

    @classmethod
    def create_study(cls):
        return StudyBuilder()

    @fluent
    def with_signal(self, signal_path):
        with open(signal_path, 'r') as signal_file:
            samples = signal_file.readline().split(',')
            self.samples = [int(raw_sample) for raw_sample in samples]

    @fluent
    def with_config(self, config_path):
        self.config = StudyConfig.load_config(config_path)

    def build(self):
        feature_types = self.config.feature_types
        (frequency, frame_size) = self.config.signal_config
        frame_provider = FrameProvider(self.samples, frequency, frame_size)
        feature_set = FeatureSet(frame_provider, feature_types)
        return Study(feature_set)


class StudyService:

    @classmethod
    def run_study(cls, signal_path, config_path):
        study = StudyBuilder.create_study().with_signal(signal_path).with_config(config_path).build()
        study.run()

