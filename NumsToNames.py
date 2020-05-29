#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:55:45 2020

@author: georgiabaltsou
"""

import csv

## For community file to names
#csv_Infile = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/results/EdgesNetCol_communities318Newman.csv'
#csv_Outfile = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/results/NamesInComms.csv'
#csvNames = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/NodesLabelsNetCol.csv'
#
#
#with open(csv_Infile, 'r') as inNames:
#    readerNames = csv.reader(inNames, delimiter=';')
#    
#    for rowName in readerNames:
#        line = []
#        for node in rowName:
#
#        
#            with open(csvNames, 'r') as csvInfile:
#                reader = csv.reader(csvInfile, delimiter=';')
#                
#                
#                for row in reader:
#                    
#                    if node == row[0]:
#                        
#                        line.append(row[1])
#                        
#        with open(csv_Outfile, 'a') as out_file:
#            writer = csv.writer(out_file, delimiter=';')
#            
#            writer.writerow([line])
#    

## For infomap file to names
csv_Infile = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/infomap/finanewman.csv'
csv_Outfile = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/infomap/newman.csv'
finalNames_txt = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/infomap/newman.txt'
csvNames = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/NodesLabelsNetCol.csv'


with open(csv_Infile, 'r') as inNames:
    readerNames = csv.reader(inNames, delimiter=';')
    
    for rowName in readerNames:
        line = []
        for node in rowName:

        
            with open(csvNames, 'r') as csvInfile:
                reader = csv.reader(csvInfile, delimiter=';')
                
                
                for row in reader:
                    
                    if node == row[0]:
                        
                        line.append(row[1])
                        
        with open(csv_Outfile, 'a') as out_file:
            writer = csv.writer(out_file, delimiter=';')
            
            writer.writerow([line])                           
                            
                            
with open(csv_Outfile, 'r') as infile, \
     open(finalNames_txt, 'a') as outfile:
    data = infile.read()
    data = data.replace("'", "")
    data = data.replace("[", "")
    data = data.replace("]", "")
    outfile.write(data)
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            