import Lab2
import pytest

def test_find_min_max():
    result = Lab2.calc_min_max_temperature([1, 2, 3, 4, 5])

    assert (result == [1, 5])

def test_calc_average():
    result = Lab2.calc_average_temperature([2, 4, 6, 8])

    assert (result == 5)

def test_calc_median_temperature():
    result = Lab2.calc_median_temperature([5, 1, 3])

    assert (result == 3)
