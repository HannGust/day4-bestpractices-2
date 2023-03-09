""" Tests of the simple_math.py module using pytest, and the parametrization functionality """

import pytest
#from simple_math import *
from simple_math import (simple_add,
                         simple_sub,
                         simple_mult,
                         simple_div,
                         poly_first,
                         poly_second)

# TESTS: 0 + 0 = 0, 1 + 0 = 1, 0 + 1 = 1, 1 + 1 = 2, 0.5 + (-0.5) = 0.0, -1 + 1 = 0, 1000 + 5050 = 6050
#@pytest
@pytest.mark.parametrize("a, b, expected", [
                         (0, 0, 0),
                         (1, 0, 1),
                         (0, 1, 1),
                         (1, 1, 2),
                         (0.5, -0.5, 0),
                         (30, 100, 130),
                         (1000, 5050, 6050)
                         ])
def test_simple_add(a, b, expected):
    assert simple_add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
                         (0, 0, 0),
                         (1, 0, 1),
                         (0, 1, -1),
                         (1, 1, 0),
                         (0.5, -0.5, 1.0),
                         (30, 100, -70),
                         (1000, 5050, -4050)
                         ])
def test_simple_sub(a, b, expected):
    assert simple_sub(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
                         (0, 0, 0),
                         (1, 0, 0),
                         (0, 1, 0),
                         (1, 1, 1),
                         (0.5, -0.5, -0.25),
                         (30, 100, 3000),
                         (1000, 5050, 5050000)
                         ])
def test_simple_mult(a, b, expected):
    assert simple_mult(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
                         (1, 1, 1),
                         (0, 1, 0),
                         (50, 1, 50),
                         (1.0, 100.0, 0.01),
                         (0.5, -0.5, -1.0),
                         (30.0, 100.0, 0.3),
                         (1000, 50, 20)
                         ])
def test_simple_div(a, b, expected):
    assert simple_div(a, b) == expected



@pytest.mark.parametrize("x, a0, a1, expected", [
                         (0, 0, 0, 0),
                         (1, 0, 0, 0),
                         (0, 1, 0, 1),
                         (0, 0, 1, 0),
                         (1, 1, 1, 2),
                         (10, 1, 1, 11),
                         (30, 100, 3000, 90100),
                         (20.0, 5.0, 7.0, 145.0)
                         ])
def test_poly_first(x, a0, a1, expected):
    assert poly_first(x, a0, a1) == expected


@pytest.mark.parametrize("x, a0, a1, a2, expected", [
                         (0, 0, 0, 0, 0),
                         (1, 0, 0, 0, 0),
                         (0, 1, 0, 1, 1),
                         (0, 0, 1, 0, 0),
                         (0, 0, 0, 1, 0),
                         (1, 1, 1, 2, 4),
                         (10, 1, 1, 11, 1111),
                         (30, 100, 2, 2, 1960),
                         (2.0, 5.0, 7.0, 3.0, 31.0)
                         ])
def test_poly_second(x, a0, a1, a2, expected):
    assert poly_second(x, a0, a1, a2) == expected
