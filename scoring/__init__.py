from scoring.DefaultConfig import DefaultConfig
from scoring.Study import Study


def create_study(config):
    return Study(config)


def load_config(config_path):
    if not config_path:
        return DefaultConfig()


def run_study(input_file, config_file):
    config = load_config(config_file)
    study = create_study(config)
    study.perform_with(input_file)