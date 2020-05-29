#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:09:11 2019

@author: georgiabaltsou
"""
import os
import csv
import numpy as np 


#for filename in os.listdir('dblp/test'):
#    
#    node1 = filename.split("<")[1].split("-")[0]
#    
#    node2 = filename.split("-")[1].split(">")[0]
#    
#    w = filename.split(">")[1].split(".")[0]
#    
#    print("node 1 =", node1, "node 2 =", node2, "weight =", w)
    
    
GTC = ['18323', '146590', '240098', '249900', '269383', '319507', '319508', '337203', '339699', '348984', '349177']
trueComm = len(GTC)

  
with open('lte/lte_communities.csv', 'r') as in_file:
    reader = csv.reader(in_file, delimiter=';')
    #skip 1st line as its the header line
    next(reader, None)
    
    with open('lte/precision-recall.csv', 'a') as out_file:
        writer = csv.writer(out_file, delimiter=';')
    
        for row in reader:
                inComm = 0
#                print(np.unique(row[3:]))
                for i in np.unique(row[3:]):
                    resultComm = len(np.unique(row[3:]))
                    if i in GTC:
                        inComm += 1
               
                recall = inComm/trueComm
                precision = inComm/resultComm
                print(precision)
                writer.writerow([recall]) 
                
                
                
                
                
                
                
                
                
                
                
                
                