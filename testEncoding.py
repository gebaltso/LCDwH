#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:10:28 2019

@author: georgiabaltsou
"""

import sys
import time

start_time = time.time()

filename = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/experiments/datasets/communities/lte_communitieslfrEdgelistN1000MU0.1.csv'

try:
    # or codecs.open on Python <= 2.5
    # or io.open on Python > 2.5 and <= 2.7
    filedata = open(filename, encoding='UTF-8').read() 
except:
    print('hi')
    filedata = open(filename, encoding='other-single-byte-encoding').read() 
    
    
print("Execution time: %s seconds " % (time.time() - start_time))