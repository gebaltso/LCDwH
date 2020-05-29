#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:07:45 2020

@author: georgiabaltsou
"""


import csv
import os

oldfile = '/Users/georgiabaltsou/Desktop/Datasets/dblp/communityFile.txt'
newfile = '/Users/georgiabaltsou/Desktop/Datasets/dblp/communityFileSymbol.txt'


newf=""
with open(oldfile,'r') as f:
    for line in f:
        newf+=line.strip()+" p\n"
    f.close()
with open(newfile,'w') as f:
    f.write(newf)
    f.close()