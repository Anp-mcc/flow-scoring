from collections import Counter


class ScoringProvider:

    def __init__(self, frame_provider):
        self.frame_provider = frame_provider
        self.cashed_results = dict()

    def get_by_position(self, position):
        if not self.cashed_results:
            for index, frame in self.frame_provider:
                self.cashed_results[index] = frame

        selected_frame = self.cashed_results[position]
        counter = Counter(selected_frame)
        return max(counter, key=counter.get)