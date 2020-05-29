#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:48:21 2020

@author: georgiabaltsou
"""


inputFile = open('/Users/georgiabaltsou/Desktop/Datasets/youTube/centralities/degree_geo.txt')



num_list = [int(num) for num in inputFile.read().split()]

# Your desired values
max_val = max(num_list)
min_val = min(num_list)

print(max_val)
print(num_list.index(max_val))