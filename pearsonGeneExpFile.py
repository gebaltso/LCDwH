#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:19:59 2020

@author: georgiabaltsou
"""

import os
import csv
from scipy.stats.stats import pearsonr
import numpy
import sys






os.chdir('seperatedExps/datasets/lfr')
infile = 'agilent.csv'
outfile = 'agilentPearsonAll.csv'



with open(infile, 'r') as in_file:
    reader = csv.reader(in_file, delimiter=';')
    
    with open(outfile, 'a') as out_file:
        writer = csv.writer(out_file, delimiter=';')
    
#    x = []
 
        count = 1
        for row in reader:
    #        print(row)
            x = []
            
            for counter in range (1,len(row)):
                x.append(float(row[counter]))              
    
            with open(infile, 'r') as in_file2:
                reader2 = csv.reader(in_file2, delimiter=';')
    
                for i in range(count):
                    next(reader2)
                  
                for line in reader2:
                    y = []
                    for counter2 in range (1,len(line)):
                    
                        y.append(float(line[counter2]))
                        if x == y: continue
                        
                    p = pearsonr(x, y)
#                    if (abs(p[0] > 0.6)):
#                    if ((p[1] < 0.05)):
#                        writer.writerow([row[0], line[0], abs(p[0]), p[1]]) #"Gene1","Gene2","Pearson Cor","p-value"
                    writer.writerow([row[0], line[0], abs(p[0])]) #"Gene1","Gene2","Pearson Cor"

                    
                        
            count += 1
                
            
            

            
            

    
    