""" Tests of simple_math.py module """

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

def test_simple_add():
    #assert simple_add(a,b) == expected
    assert simple_add(0,0) == 0
    assert simple_add(1,0) == 1
    assert simple_add(0,1) == 1    
    assert simple_add(1,1) == 2    

def test_simple_sub():
    #assert simple_mult(a,b) == expected
    assert simple_sub(0,0) == 0
    assert simple_sub(1,0) == 1
    assert simple_sub(0,1) == -1
    assert simple_sub(1,1) == 0


def test_simple_mult():
    #assert simple_mult(a,b) == expected
    assert simple_mult(0,0) == 0
    assert simple_mult(1,0) == 0
    assert simple_mult(0,1) == 0
    assert simple_mult(1,1) == 1


def test_simple_div():
    #assert simple_div(a,b) == expected
    assert simple_div(1,1) == 1
    assert simple_div(2,2) == 1
    assert simple_div(4,2) == 2
    assert simple_div(2.0, 4.0) == 0.5

def test_poly_first():
    #assert poly_first(x,a0,a1) == expected
    assert poly_first(1,1,0) == 1
    assert poly_first(10,0,3) == 30

def test_poly_second():
    #assert poly_second(x,a0,a1,a2) == expected
    assert poly_second(10,0,0,1) == 100
    assert poly_second(-1,1,2,1) == 0
