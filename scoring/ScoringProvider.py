from collections import Counter


class ScoringProvider:

    def __init__(self, frame_provider):
        self.frame_provider = frame_provider

    def get_by_position(self, position):
        for index, frame in self.frame_provider:
            if position == index:
                counter = Counter(frame)
                return max(counter, key=counter.get)
