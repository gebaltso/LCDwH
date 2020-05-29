#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:24:15 2019

@author: georgiabaltsou
"""



import csv
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os
import random
import time
import sys
import shutil
from lemonW import lemon
from lte import lte
from testTCE import tce 
from newLCD import newLCD
from metrics import metrics
from fileWeightAdjacement import FilesAdj, FilesAdjAll, ReduceW
from LFR import LFR
from ReWeighting import reWeighting
from csvToText import csvToText




#os.chdir('seperatedExps/datasets/lfr/')

#file = 'lfr.csv'

#myFile = 'lfrEdgelistN1000MU0.1*.csv'
#file = 'lfrEdgelistN1000MU0.1*'
#seed = '433'

#lemonFile = "lemonDatasets/lfr/new"
#seedsetFile = "lemonDatasets/lfr/seed"

lemonFile = "seperatedExps/datasets/weighted/lfrEdgelistN1000MU0.1*<1111-1111>1"
seedsetFile = "seperatedExps/datasets/lfr/seedSetFile"

lemon(lemonFile, seedsetFile)
#shutil.copy2(myFile, '../weighted/'+str(file)+'<1111-1111>1.csv' )

#tce(myFile, seed, file)


#reWeighting(file, seed)

#n = csvToText(myFile, 'newFile')
#
#print(n)


