class FeatureStrategy:

    def __init__(self, func):
        self.func = func

    def calculate(self, frame):
        return self.func(frame)