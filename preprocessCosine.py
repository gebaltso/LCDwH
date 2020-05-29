#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:14:25 2018

@author: georgiabaltsou
"""

import numpy as np
from scipy import spatial
import csv

#import xenaPython as xena 
#
#hub = "https://toil.xenahubs.net"
#dataset = "Caldas2007/naderi2007Exp_genomicMatrix"


def euclDist(a, b):
    
    a = list(map(float, a))
    b = list(map(float, b))
    
    a = np.array(a)
    b = np.array(b)
    
    dist = np.linalg.norm(a-b)
    return dist

def cosineSim(a, b):
    
    a = list(map(float, a))
    b = list(map(float, b))
    
    sim = 1 - spatial.distance.cosine(a, b) #similarity = 1 - distance
    
    return sim


def pearsonCor(a, b):
    
    a = list(map(float, a))
    b = list(map(float, b))
    
    pearson = np.corrcoef(a, b)[0, 1]
    
    return pearson

######## MAIN ###############


#with open('naderi2007Final2.csv') as data_file: 
#    reader = csv.reader(data_file, delimiter=';')
#    with open('naderi2007Final2.csv') as data_file2: 
#        readerCompare = csv.reader(data_file2, delimiter=';')
#        with open('outputEucl.csv', 'w') as out_file:
#            out = csv.writer(out_file, delimiter=';')
#            for row in reader:
#                for rowCompare in readerCompare:
#                    if row == rowCompare:
#                        continue;
#                    else:
#                        out.writerow([row[0],rowCompare[0], euclDist(row[1:], rowCompare[1:])])
##                        out.writerow([row[0],rowCompare[0], cosineSim(row[1:], rowCompare[1:])])
##                        d.append(euclDist(row[1:], rowCompare[1:]))
#                        
#                data_file2.seek(0)




#print('Number of genes= ', genes)
#
#print('length of d = ', len(d))


#
#with open('YauGeneExp_genomicMatrix.csv') as data_file: 
#    reader = csv.reader(data_file, delimiter=' ')
#    with open('YauGeneExp_genomicMatrix.csv') as data_file2: 
#        readerCompare = csv.reader(data_file2, delimiter=' ')
#        with open('newoutput.csv', 'w') as out_file:
#            out = csv.writer(out_file, delimiter=';')
#            for row in reader:
#                for rowCompare in readerCompare:
#                    if row == rowCompare:
#                        continue;
#                    else:
##                        out.writerow([row[0],rowCompare[0], euclDist(row[1:], rowCompare[1:])])
#                        out.writerow([row[0],rowCompare[0], cosineSim(row[1:], rowCompare[1:])])
##                        d.append(euclDist(row[1:], rowCompare[1:]))
#                        
#                data_file2.seek(0)


with open('naderi2007Final2.csv') as data_file: 
    reader = csv.reader(data_file, delimiter=';')
    with open('naderi2007Final2.csv') as data_file2: 
        readerCompare = csv.reader(data_file2, delimiter=';')
        with open('outputPearson.csv', 'w') as out_file:
            out = csv.writer(out_file, delimiter=';')
            for row in reader:
                for rowCompare in readerCompare:
                    if row == rowCompare:
                        continue;
                    else:
                        out.writerow([row[0],rowCompare[0], pearsonCor(row[1:], rowCompare[1:])])
#                        out.writerow([row[0],rowCompare[0], cosineSim(row[1:], rowCompare[1:])])
#                        d.append(euclDist(row[1:], rowCompare[1:]))
                        
                data_file2.seek(0)



