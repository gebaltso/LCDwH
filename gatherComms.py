#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:26:11 2020

@author: georgiabaltsou
"""

import csv
import os


csv_Infile = '/Users/georgiabaltsou/Desktop/Datasets/dblp/dblpDegrees.csv'
csv_Outfile = '/Users/georgiabaltsou/Desktop/Datasets/dblp/dblpGatheredComms.csv'
txt_file = '/Users/georgiabaltsou/Desktop/Datasets/dblp/communityFileSymbol.txt'
                                
                
with open(txt_file, 'r') as in_file:
    lines = in_file.readlines()
    
lines = [x.strip() for x in lines]   
lines = [line.split(" ") for line in lines if line]

flat_lines = [item for sublist in lines for item in sublist]


with open(csv_Outfile, 'a') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    
    for node in flat_lines: 

        with open(csv_Infile, 'r') as csvInfile:
            reader = csv.reader(csvInfile, delimiter=';')

            for row in reader: 

                if (node == row[0]):
                    writer.writerow([row[0],row[1], row[2], row[3]])
                elif (node == "p"):
                    writer.writerow(["&", "&", "&", "&"])
                    break

    
    

    
    
    
    
    
    
   