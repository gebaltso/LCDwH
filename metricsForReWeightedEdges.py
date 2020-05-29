#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:16:45 2019

@author: georgiabaltsou
"""


import os
import csv
import numpy as np
import editdistance
 


def metrics(myFile, GTC, trueComm, algorithm):
    
    with open('communities/'+str(myFile), 'r') as in_file:
        reader = csv.reader(in_file, delimiter=';')
        #skip 1st line as its the header line
        next(reader, None)
        
        
        with open('communities/metrics'+'.'+str(myFile), 'a') as out_file:
            writer = csv.writer(out_file, delimiter=';')
            
            if os.stat('communities/metrics'+'.'+str(myFile)).st_size == 0:
                writer.writerow(["ALGORITHM", "PRECISION", "RECALL", "F1", "JaccardIndex", "EDIT DISTANCE"])
        
            for row in reader:
                
#                node1 = row[0]
#                node2 = row[1]
#                weight = row[2]
                
                
                inComm = 0
#                obtainedComm = np.unique(row[3:])
                obtainedComm = np.unique(row[0:])
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
                
                JI = len(np.intersect1d(GTC, obtainedComm))/len(np.union1d(GTC, obtainedComm))
                
                ed = editdistance.eval(GTC, obtainedComm)
                
                writer.writerow([algorithm, precision, recall, F1, JI ,ed]) 
                

    
    
                    
                