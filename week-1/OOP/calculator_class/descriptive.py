#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:11:17 2019

@author: JacquesPierre
"""

import math

class Calculator:

    def __init__(self, data):
        self.data = data
        
    def __calc_metrics__(self)    
        self.length = self.__getLength__()
        self.mean = self.__getMean__()
        self.median = self.__getMedian__()
        self.variance = self.__getVariance__()
        self.stand_dev = self.__getStand_Dev__()
    
    def __getLength__(self):
        return len(self.data)
    
    def __getMean__(self):
        return sum(self.data)/self.length
    
    def __getMedian__(self):
        if self.length % 2:
            return self.data[self.length//2]
        else:
            return (self.data[self.length//2] + 
                              self.data[self.length//2]-1)/2
    
    def __getVariance__(self):
        numerator = 0
        for i in self.data:
            numerator += (i - self.mean)**2
            return numerator/self.length
    
    def __getStand_Dev__(self):
        return math.sqrt(self.variance)
    
    def add_data(self, new_data):
        self.data.extend(new_data)
        __calc_metrics__(self)
    
    def remove_data(self, new_data):
        for i in new_data:
            if i in self.data:
                self.data.remove(i)
        __calc_metrics__(self)