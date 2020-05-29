#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:05:16 2019

@author: georgiabaltsou
"""

import networkx as nx
import os
import time
import shutil
import sys
from lemonW import lemon
from lte import lte
from tce import tce 
from newLCD import newLCD
from metrics import metrics
from fileWeightAdjacement import FilesAdjAll
from ReWeighting import reWeighting
from csvToText import csvToText

os.chdir('seperatedExps/datasets/lfr/')

#myFile is the input csv file with the LFR parameters in its name
#myFile = 'lfrEdgelistN1000MU0.1*.csv'
#myFile = 'NetColUn.csv'
myFile = 'youTube.csv'

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = myFile[:-4]

#community file for Lemon algorithm
communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'

#seeds = read seed nodes from seedFile
seedFile = open('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', 'r')
seeds = seedFile.readline().split(" ")
seedsetFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt'

#keep as seed the 1st seed of seedFile
seed = seeds[0]

#Creation of the graph with the input file
G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')

#calculate the number of edges and the number of nodes of the input graph
numberOfEdges = G.number_of_edges()
numberOfNodes = G.number_of_nodes()   
print("The network has", numberOfNodes, "nodes with", numberOfEdges, "edges.")
print("------------------------------")

os.chdir('../')

##call reWeighting for find new weights for the graph's edges. ReWeigthedFile will be stored in weighted folder.
#ReWeigthedFile, graph = reWeighting(myFile, file, seeds, G)   
#print("Re-Weighting of edges done.")
#print("------------------------------")
#
#
##adjacement of all neighbors' of a node weight (x3)
#MultWeightedFile = FilesAdjAll(myFile,file, seeds, G)
#print("Weighted file created.")
#print("------------------------------")
#
##convert each file in weighted folder to plain text file and move them to weightedForLemon dir
#for filename in os.listdir('weighted'):        
#    if not filename.startswith('.'):
#        filenameSplit = filename.split('csv')[0]
#        shutil.move(csvToText('weighted/'+filename, 'weighted/'+str(filenameSplit)), 'weightedForLemon/'+filenameSplit)
#print("Convertion and move of files for Lemon algorithm completed.")
#print("------------------------------")

#run the experiments with all thw files in weighted dir, and with Lemon algorithm
for filename in os.listdir('weightedForLemon'):        
    if not filename.startswith('.'):           
            lemon('weightedForLemon/'+str(filename), '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', str(filename), communityFile, str(file))
print("Lemon  algorithm completed.")
print("------------------------------")








