#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:35:22 2019

@author: swilson5
"""
import pytest
from descriptive import Calculator


def test_mean():
    data = [2, 10, 15, 20, 45, 55, 80]
    instance = Calculator(data)
    actual_mean = instance.mean
    expected_mean = 32.42857
    message = "Expected value: {0}, Actual value: {1}".format(expected_mean,
                                                              actual_mean)
    assert instance.mean == pytest.approx(expected_mean), message


def test_std():
    data = [2, 10, 15, 20, 45, 55, 80]
    instance = Calculator(data)
    actual_std = instance.mean
    expected_std = 28.33641
    message = "Expected STD: {0}, Actual value: {1}".format(expected_std,
                                                              actual_std)
    assert instance.stand_dev == pytest.approx(28.33641)

def test_order():
    data = [2, 20, 45, 15, 10, 55, 80]
    instance = Calculator(data)
    expected_median =20
    actual_median = instance.median
    message = "Expected value: {0}, Actual value: {1}, did you order the ".format(expected_median, actual_median)
    assert instance.median == 20, message
    
def test_add_data():
    data = [2, 20, 45, 15, 10, 55, 80]
    instance = Calculator(data)
    instance.add_data([60])
    actual_mean = instance.mean
    expected_mean = 35.875
    message = "called add_data() and expected mean: {0}, but got value: {1}".format(expected_mean,
                                                              actual_mean)
    assert instance.mean == pytest.approx(expected_mean), message

def test_remove_data():
    data = [2, 20, 45, 15, 10, 55, 80]
    instance = Calculator(data)
    instance.remove_data([80])
    actual_mean = instance.mean
    expected_mean = 24.5
    message = "called remove_data() and expected mean: {0}, but got value: {1}".format(expected_mean,
                                                              actual_mean)
    assert instance.mean == pytest.approx(expected_mean), message