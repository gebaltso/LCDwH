#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:08:03 2019

@author: georgiabaltsou

Convert txt file into csv.
From:
1    2
1    3
etc

To:
1;2
1;3
etc


"""

import csv
import os


csv_file = '/Users/georgiabaltsou/Desktop/communityFile.csv'
txt_file = '/Users/georgiabaltsou/Desktop/communityFile.txt'
                                
                
with open(txt_file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(" ") for line in stripped if line)  #change split to "\t" for tabbed txt file

    with open(csv_file, 'w') as out_file:
        writer = csv.writer(out_file, delimiter = ';')
        writer.writerows(lines)