#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:35:22 2019

@author: swilson5
"""
import pytest
from math_functions import Calculator

data1 = [2, 20, 45, 15, 10, 55, 80]

instance = Calculator(data1)


def test_stats():    
    assert instance.mean == pytest.approx(32.43)
