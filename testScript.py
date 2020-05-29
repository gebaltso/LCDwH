#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:26:40 2019

@author: georgiabaltsou
"""

import csv
import numpy as np
import os
import random
import time
import sys
import shutil
from lemon import lemon
from lte import lte
from tce import tce 
from newLCD import newLCD
from metrics import metrics
from fileWeightAdjacement import weightedFiles
from LFR import LFR
from ReWeighting import reWeighting

start_time = time.time()

os.chdir('testExperiments/datasets/lfr/')

myFile = 'lfrEdgelistN1000MU0.1*.csv'
file = 'lfrEdgelistN1000MU0.1*'

#shutil.copy2(myFile, 'lfrEdgelistN1000MU0.1*.csv<111-111>1.csv')
#shutil.copy2('lfrEdgelistN1000MU0.1*.csv<111-111>1.csv','../weighted/lfrEdgelistN1000MU0.1*.csv<111-111>1.csv' )
#shutil.copy2(myFile, '../weighted/lfrEdgelistN1000MU0.1*.csv<000-000>1.csv')

GTC = ['327', '210', '352', '485', '616', '236', '371', '501', '246', '638', '639']

#find the length of the community stored in GTC
trueComm = len(GTC)

#call reWeighting for find new weights for the graph's edges
#ReWeigthedFile, graph = reWeighting(myFile)
#
#print("Re-Weighting of edges done.")
#print("------------------------------")

#till now working dir = /Users/georgiabaltsou/Desktop/PhD/Local_exp/experiments/datasets/lfr
#print("Current Working Directory " , os.getcwd())


os.chdir('../')

#weightedFiles(ReWeigthedFile, GTC, graph)
#
#print("Weighted files created.")
#print("------------------------------")

#sys.exit()

#for filename in os.listdir('weighted'):
#    for seed in GTC:
#        
##        lemon('weighted/'+str(filename), seed, file)
#        
#        lte('weighted/'+str(filename), seed, file)
#
#        tce('weighted/'+str(filename), seed, file)
#       
#        newLCD('weighted/'+str(filename), seed, file)
#        
#print("Algorithms completed.")
#print("------------------------------")


##Write the files with precision and recall for each community of the 3 algorithms

os.chdir('communities')


for filename in os.listdir(os.getcwd()):
    
    
    if not filename.startswith('.'):
    
        algorithm = filename.split("_")[0]
        
        metrics(str(filename), GTC, trueComm, algorithm)
        
    
print("Metrics files created.")
print("------------------------------")

print("Execution time: %s seconds " % (time.time() - start_time))
print("------------------------------")   