#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:28:58 2020

@author: georgiabaltsou
"""




import csv
import os

os.chdir('seperatedExps/datasets/lfr/')


reader = csv.reader(open("YauGeneExpTest.csv", "rU"), delimiter='/t')
writer = csv.writer(open("output.csv", 'w'), delimiter=';')
writer.writerows(reader)