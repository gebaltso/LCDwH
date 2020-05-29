#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:10:43 2020

@author: georgiabaltsou
"""

import networkx as nx
import csv
import os
import time
import shutil
import sys
import copy

#change dir
os.chdir('/Users/georgiabaltsou/Desktop/Datasets/LFRproducts/weighted/normal/LFR5')

with open('lfr5*NODES.csv', 'a') as file:
    
    writer = csv.writer(file, delimiter=';')
    
    for i in range(5000):
        writer.writerow([i])