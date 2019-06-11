class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def scores(self):
        ''' returns list of scores '''
        return self.scores

    def latest(self):
        ''' returns last score '''
        return self.scores[-1]

    def personal_best(self):
        ''' returns highest score '''
        return max(self.scores)

    def personal_top(self):
        ''' returns top 3 scores '''
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        ''' returns difference between latest and top '''
        difference = self.personal_best() - self.latest()
        report_beginning = f"Your latest score was {self.latest()}. "
        report_diff = f"That's {difference} short of your personal best!"
        report_best = "That's your personal best!"
        if self.latest() == self.personal_best():
            return report_beginning + report_best
        return report_beginning + report_diff