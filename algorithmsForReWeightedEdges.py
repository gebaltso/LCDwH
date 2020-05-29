#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:13:05 2019

@author: georgiabaltsou

Algorithms for re-weighted edges

"""

import csv
import numpy as np
import os
from lteForReWeightedEdges import lte
from tceForReWeightedEdges import tce 
from newLCDForReWeightedEdges import newLCD
from fileAdjacement import weightedFiles
from metricsForReWeightedEdges import metrics



#myFile = 'dblp/dblp.csv'
#myFile = 'lfr1Graph.csv'
myFile = 'lfrEdgelistExamplelfr1Graph.csv'
file = myFile.split(".")[0] #keep the name without the .csv


#ground truth community
#GTC = ['18323', '146590', '240098', '249900', '269383', '319507', '319508', '337203', '339699', '348984', '349177'] #for dblp
#GTC = ['320', '162', '35', '292', '38', '166', '841', '620', '973', '719', '656', '817', '346'] #for lfr1
GTC = ['873', '746', '237', '753', '882', '499', '115', '630', '127'] #for lfrEdgelistExamplelfr1Graph


trueComm = len(GTC)

 	
os.chdir('experiments/datasets/')
#print("Current Working Directory " , os.getcwd())
#weightedFiles(myFile, GTC)
#
#print("Weighted files created.")
#
for filename in os.listdir('weighted'):
    for seed in GTC:
        lte('weighted/'+str(filename), seed, file)

        tce('weighted/'+str(filename), seed, file)
       
        newLCD('weighted/'+str(filename), seed, file)


##Write the files with precision and recall for each community of the 3 algorithms
#os.chdir('/home/georgia/Documents/Local_exp/experiments/datasets/communities')
#print("Current Working Directory " , os.getcwd())
for filename in os.listdir('communities'):
    
    algorithm = filename.split("_")[0]
    
    metrics(str(filename), GTC, trueComm, algorithm)
    

    
 