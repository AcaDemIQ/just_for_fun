import pytest

class GradeCalculator:
    def __init__(self, _min, _max):
        self.min = _min
        self.max = _max

    def calculate_average(self, l):
        if l is None or len(l) == 0:
            raise ValueError
        filtered = list(filter(lambda l: self.min <= l and l <= self.max, l))
        if len(l) != len(filtered):
            raise ValueError

        return sum(l) / len(l)

@pytest.fixture
def calc():
    return GradeCalculator(1,5)

def test_working(calc):
    assert 2 == calc.calculate_average([1,2,3])

def test_none_obj(calc):
    with pytest.raises(ValueError):
        calc.calculate_average(None)

def test_empty_list(calc):
    with pytest.raises(ValueError):
        calc.calculate_average([])

def test_less_than_min(calc):
    with pytest.raises(ValueError):
        calc.calculate_average([4, -2])

def test_more_than_max(calc):
    with pytest.raises(ValueError):
        calc.calculate_average([2, 10])






