#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:32:29 2019

@author: georgiabaltsou
"""

import os
import csv
import numpy as np



def metrics(myFile, GTC, trueComm):
    with open('./communities/' + myFile + '_communities.csv', 'r') as in_file:
        reader = csv.reader(in_file, delimiter=';')
        #skip 1st line as its the header line
        next(reader, None)
    
            
        with open('./communities/metrics_'+str(myFile) + '.csv', 'a') as out_file:
            writer = csv.writer(out_file, delimiter=';')
            
            if os.stat('./communities/metrics_'+str(myFile) + '.csv').st_size == 0:
                writer.writerow(["ALGORITHM","Seed node","Method", "PRECISION", "RECALL", "F1"])
            for row in reader:
                
                alg = str(row[0])

                seed = str(row[1])
                weight = str(row[2])

                
                inComm = 0
                obtainedComm = np.unique(row[3:])
                                
                for i in obtainedComm:
                    resultComm = len(obtainedComm)
                    if i in GTC:
                        inComm += 1
                   
                precision = inComm/resultComm
                recall = inComm/trueComm
                if (precision+recall)==0:
                    F1=0
                else:  
                    F1 = 2 * (precision * recall) / (precision + recall)
                
#                JI = len(np.intersect1d(GTC, obtainedComm))/len(np.union1d(GTC, obtainedComm))
                
#                writer.writerow([alg, node1, node2, seed, weight, precision, recall, F1, JI]) 
                writer.writerow([alg, seed, weight, precision, recall, F1]) 
                

    
    
                    
                