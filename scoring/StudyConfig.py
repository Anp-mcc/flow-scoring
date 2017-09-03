from constants import SCORING_MODEL_SECTION
from constants import FEATURE_TYPES_SECTION
from constants import SIGNAL_MODEL_SECTION
from constants import MATH_MODEL_SECTION
from constants import WINDOW_SIZE
from constants import FREQUENCY
from constants import STUDY_NAME
import yaml


class StudyConfig:

    @classmethod
    def load_config(cls, config_path):
        study_name = ""
        feature_types = []
        frequency = 0
        window_size = 0
        scoring_frequency = 0
        with open(config_path, 'r') as yml_file:
            raw_cfg = yaml.load(yml_file)
            math_model = raw_cfg[MATH_MODEL_SECTION]
            signal_model = raw_cfg[SIGNAL_MODEL_SECTION]
            scoring_model = raw_cfg[SCORING_MODEL_SECTION]
            study_name = raw_cfg[STUDY_NAME]
            for key in math_model:
                if key == FEATURE_TYPES_SECTION:
                    feature_types = math_model[key]
            for key in signal_model:
                if key == FREQUENCY:
                    frequency = signal_model[key]
                if key == WINDOW_SIZE:
                    window_size = signal_model[key]
            for key in scoring_model:
                if key == FREQUENCY:
                    scoring_frequency = scoring_model[key]


            return StudyConfig(study_name, feature_types, scoring_frequency, frequency, window_size)

    @property
    def signal_config(self):
        return self.frequency, self.window_size

    def __init__(self, study_name, feature_types, scoring_frequency, frequency, window_size):
        self.study_name = study_name
        self.scoring_frequency = scoring_frequency
        self.feature_types = feature_types
        self.window_size = window_size
        self.frequency = frequency


