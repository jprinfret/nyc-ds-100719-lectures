#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator:

    def __init__(self, data):
        self.data = sorted(data)
        self.__calc_stats()

    def __calc_mean(self):
        return self.total/self.length

    def __calc_median(self):
        n = self.length
        if n % 2 == 1:
            return self.data[(n-1)//2]
        else:
            return (self.data[n//2-1]+self.data[n//2])/2

    def __calc_variance(self):
        sum_value = 0
        for item in self.data:
            sum_value += (item - (self.mean))**2
        return sum_value/(self.length-1)

    def __calc_stddev(self):
        return math.sqrt(self.variance)

    def __calc_stats(self):
        self.length = len(self.data)
        self.total = sum(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_variance()
        self.stand_dev = self.__calc_stddev()

    def add_data(self, new_data):
        self.data.extend(new_data)
        self.data = sorted(self.data)
        #self.__calc_stats()
        return

    def remove_data(self, new_data):

        self.data = [x for x in self.data if x not in new_data]
        #self.__calc_stats()
        return

    def __calc_covariance(self, d2):
        df = (self.length-1)
        m2 = self.__calc_mean(d2)
        return sum([(i-self.mean)*(j-m2) for i, j in zip(self.data, d2)])/ df
