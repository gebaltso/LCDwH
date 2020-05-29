#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:50:34 2020

@author: georgiabaltsou
"""

import csv


csv_Infile = '/Users/georgiabaltsou/Desktop/Datasets/dblp/dblpDegrees.csv'
csv_Outfile = '/Users/georgiabaltsou/Desktop/Datasets/dblp/dblpWeakComms.csv'
csvComms = '/Users/georgiabaltsou/Desktop/Datasets/dblp/communityFile.csv'
                                
                
with open(csvComms, 'r') as inComms:
    readerComm = csv.reader(inComms, delimiter=';')
    
    
    for rowComm in readerComm:
        sum = 0
        denominator = len(rowComm)

        for node in rowComm:
        
            with open(csv_Infile, 'r') as csvInfile:
                reader = csv.reader(csvInfile, delimiter=';')
            
            
                for row in reader:
                    
                    if node == row[0]:
                        sum = sum + float(row[3])
                        
        with open(csv_Outfile, 'a') as out_file:
            writer = csv.writer(out_file, delimiter=';')
            
            writer.writerow([node, sum/denominator])
            
    
