#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:39:16 2018

@author: georgiabaltsou
"""

import numpy as np
import csv
from itertools import islice
from scipy import spatial

def euclDist(a, b):

    a = list(map(float, a))
    b = list(map(float, b))
    
    a = np.array(a)
    b = np.array(b)
    
    dist = np.linalg.norm(a-b)
    return dist


def cosineSim(a, b):
    
    a = list(map(float, a))
    b = list(map(float, b))
    
    sim = 1 - spatial.distance.cosine(a, b) #similarity = 1 - distance
    
    return sim


def pearsonCor(a, b):
    
    a = list(map(float, a))
    b = list(map(float, b))
    
    pearson = np.corrcoef(a, b)[0, 1]
    
    return pearson

#x = [3,4,5]
#y = [4,5,6]

#print(euclDist(x,y))

d = []
counter = 0


with open('toy.csv') as data_file: 
    reader = csv.reader(data_file, delimiter=';')
    with open('toy.csv') as data_file2: 
        readerCompare = csv.reader(data_file2, delimiter=';')
        for row in reader:
            for rowCompare in readerCompare:
                if row == rowCompare:
                    continue;
                else:
                    d.append(pearsonCor(row[1:], rowCompare[1:]))
            data_file2.seek(0)
#
#            
#
#
##print('Number of genes= ', genes)
##
print('d =', d)
print('length of d = ', len(d))




















