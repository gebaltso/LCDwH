#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:48:15 2019

@author: georgiabaltsou
"""


import csv

      
             
with open('/Users/georgiabaltsou/Desktop/Datasets/wiki/wiki.csv','r') as csvinput:
    with open('/Users/georgiabaltsou/Desktop/Datasets/wiki/wikiW.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, delimiter=';')
        for row in csv.reader(csvinput, delimiter=';'):
            writer.writerow(row+[1])