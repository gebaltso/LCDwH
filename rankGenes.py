#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:23:31 2020

@author: georgiabaltsou
"""


import os
import csv
import numpy
import sys


os.chdir('seperatedExps/datasets/lfr')
infile = 'toy.csv'


with open(infile, 'r') as in_file:
    reader = csv.reader(in_file, delimiter=';')
    
    for row in reader:
        