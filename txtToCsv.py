#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:11:18 2019

@author: georgiabaltsou
"""

#convert edge txt file to csv file appending also weight 1 to all edges

import csv
import os


os.chdir('/Users/georgiabaltsou/Desktop/')

with open('wiki.txt') as data_file: 
            reader = csv.reader(data_file, delimiter='\t')        
            with open('wiki.csv', 'w') as out_file:
                writer = csv.writer(out_file, delimiter=';')  
                for row in reader:
                    writer.writerow([row[0],row[1]], 1)



#with open('wiki.txt', 'r') as in_file:
#    stripped = (line.strip() for line in in_file)
#    lines = (line.split(",") for line in stripped if line)
#    with open('wiki.csv', 'w') as out_file:
#        writer = csv.writer(out_file, delimiter=';')
#        writer.writerows(lines)


#with open('wiki.txt') as infile, open('wiki.csv','w') as outfile: 
#    for line in infile: 
#        outfile.write(line.replace(' ',';'))