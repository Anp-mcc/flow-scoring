class FeatureStrategy:

    def __init__(self, func, type):
        self.func = func
        self.type = type

    def calculate(self, frame):
        return self.func(frame)