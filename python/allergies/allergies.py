from enum import Flag, auto


class Allergies(Flag):

    EGGS = 2
    PEANUTS = 6

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self):
        return self.EGGS & self.PEANUTS




"""
class Allergies(object):

    allergy_scores = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return self.allergy_scores.get(item, 0) & self.score != 0

    @property
    def lst(self):
        return list(filter(self.is_allergic_to, self.allergy_scores))
"""
