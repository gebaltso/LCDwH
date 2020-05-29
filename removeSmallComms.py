#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:47:59 2020

@author: georgiabaltsou
"""

import csv
import os


txt_file = '/Users/georgiabaltsou/Desktop/Datasets/dblp/communityFile.csv'
out_txt_file = '/Users/georgiabaltsou/Desktop/Datasets/dblp/communityFile2.csv'


with open(txt_file, 'r') as in_file:
    
    reader = csv.reader(in_file, delimiter=';')
    
    for row in reader:
        
        if len(row) > 2 :
            
            
            with open(out_txt_file, 'a') as out_file:
                writer = csv.writer(out_file, delimiter = ';')
                writer.writerow(row)