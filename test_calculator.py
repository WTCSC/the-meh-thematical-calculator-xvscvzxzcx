# test_calculator.py
""" Pytest tests for calculator.py """

import pytest 
from calculator import add, subtract, multiply, divide

#ADD TESTS

def test_add_positive_numbers():
"""Test adding"""
  assert add(5, 3) == 8

def test_add_negative_numbers():
"""Test adding two negative"""
  assert add(-5, -3) == -8

#SUBTRACT TESTS

def test_subtract_large_numbers():
"""Test subtracting two numbers that are large plus seeing if they subtract to a zero"""
  assert subtract(1000, 1000) == 0

def test_subtract_negative_numbers():
"""Test subtracting two negative numbers"""
  assert subtract(-44, -50) == 6

#MULTIPLY TESTS

def test_multiply_numbers():
"""Test multiply two large numbers that or also negative"""
  assert multiply(-44, -50) == 2200

def test_multiply_by_zero():
"""Test multiply a number that equals to 0"""
  assert multiply(0, 1124) == 0

#DIVIDE TESTS

def test_divide_by_zero():
"""test dividing a number by 0"""
  assert divide(124, 0) is None

def test_division_of_large_numbers():
"""Test dividing large numbers that equals to a decimal"""
  assert divide(2343165, 3247647) == 0.7214962094
