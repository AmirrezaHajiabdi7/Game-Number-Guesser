class Score:

    def __init__(self, initial_score=100):
        self.score = initial_score

    def decrement_score(self, penalty=10):
        self.score -= penalty

        self.score = max(self.score, 0)

    def get_score(self):
        return self.score
