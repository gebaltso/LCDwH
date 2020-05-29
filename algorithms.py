#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:46:10 2019

@author: georgiabaltsou
"""

import csv
import numpy as np
import os
from lte import lte
from tce import tce 
from newLCD import newLCD
from fileAdjacement import weightedFiles
from metrics import metrics



#myFile = 'dblp/dblp.csv'
myFile = 'lfr1Graph.csv'
file = 'lfr1Graph'

#ground truth community
#GTC = ['18323', '146590', '240098', '249900', '269383', '319507', '319508', '337203', '339699', '348984', '349177']
GTC = ['320', '162', '35', '292', '38', '166', '841', '620', '973', '719', '656', '817', '346']
trueComm = len(GTC)

 	
os.chdir('experiments/datasets/')
#print("Current Working Directory " , os.getcwd())
#weightedFiles(myFile, GTC)
#
#print("Weighted files created.")
#
#for filename in os.listdir('weighted'):
#    for seed in GTC:
#        lte('weighted/'+str(filename), seed, file)
#
#        tce('weighted/'+str(filename), seed, file)
#       
#        newLCD('weighted/'+str(filename), seed, file)
#
#
##Write the files with precision and recall for each community of the 3 algorithms
#os.chdir('/home/georgia/Documents/Local_exp/experiments/datasets/communities')
#print("Current Working Directory " , os.getcwd())
for filename in os.listdir('communities'):
    
    algorithm = filename.split("_")[0]
    
    metrics(str(filename), GTC, trueComm, algorithm)
    

    
 