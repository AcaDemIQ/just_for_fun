import pytest

class AverageCalculator:
    def __init__(self):
        pass

    def calculate_average(self, l):
        return sum(l) / len(l)
    

def test_working():
    a = [1,2,3]
    calc = AverageCalculator()
    assert 2 == calc.calculate_average(a)


def test_wrong_case():
    a = []
    calc = AverageCalculator()
    assert 0 == calc.calculate_average(a) # ooooops!
