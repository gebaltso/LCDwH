#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:23:39 2019

@author: georgiabaltsou

Script for producing LFR graphs and take as output the final communities from eac method and the corresponding metrics

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

#myFile = lfrEdgelistN1000MU0.1*.csv  #just to remember the form of file name
myFile = LFR(1000, 3, 1.1, 0.1)
file = myFile.split("*")[0] #keep the name without the .csv

#sys.exit()

#find a random community of the corresponding graph and store it in GTC
commFile = file.split("N")[1]
GTCline = random.choice(open('lfrCommN'+str(commFile)+'*.txt').readlines())
GTC = list(GTCline.split(" "))
GTC[-1] = GTC[-1].strip()

#find the length of the community stored in GTC
trueComm = len(GTC)

#call reWeighting for find new weights for the graph's edges
ReWeigthedFile, graph = reWeighting(myFile)

print("Re-Weighting of edges done.")
print("------------------------------")

#till now working dir = /Users/georgiabaltsou/Desktop/PhD/Local_exp/experiments/datasets/lfr
#print("Current Working Directory " , os.getcwd())

os.chdir('../')

weightedFiles(ReWeigthedFile, GTC, graph)

print("Weighted files created.")
print("------------------------------")

#sys.exit()

for filename in os.listdir('weighted'):
    for seed in GTC:
        
        lemon('weighted/'+str(filename), seed, file)
        
        
#        lte('weighted/'+str(filename), seed, file)
#
#        tce('weighted/'+str(filename), seed, file)
#       
#        newLCD('weighted/'+str(filename), seed, file)
        
print("Algorithms completed.")
print("------------------------------")


##Write the files with precision and recall for each community of the 3 algorithms
#print("Current Working Directory " , os.getcwd())
os.chdir('../Local_exp/experiments/datasets/communities')


#GTC = ["714", "330", "334", "721", "339", "149", "987", "220", "285", "414", "476", "96", "417", "936", "237", "622", "111", "61", "755", "627", "253", "764", "189"]
#trueComm = len(GTC)

for filename in os.listdir(os.getcwd()):
    
    
    if not filename.startswith('.'):
    
        algorithm = filename.split("_")[0]
        
        metrics(str(filename), GTC, trueComm, algorithm)
        
    
print("Metrics files created.")
print("------------------------------")

print("Execution time: %s seconds " % (time.time() - start_time))
print("------------------------------")   






