#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:07:16 2020

@author: georgiabaltsou
"""

import networkx as nx
import csv
import os
import time
import shutil
import sys
import copy
from metrics import metrics
from collections import defaultdict
from fileWeightAdjacement import FilesAdjAll
from ReWeighting import reWeighting
from tceForAdjlist import tce 
from lteForAdjlist import lte
from newLCDForAdjlist import newLCD
from simRank import simRank
from loopEdge import addLoopEdge
from CNR import cnr
from WERWKpath import KpathAlg
from propinquity import propinquityD


def call_method(method, seedSetFile, file, G, newGraph, l, d, a, b, hops):
    if method == 'plain':
        lte(seedsetFile, file, 1, copy.deepcopy(G), copy.deepcopy(newGraph), method,l)
        lte(seedsetFile, file, 3, copy.deepcopy(G), copy.deepcopy(newGraph), method,l)
        newLCD(seedsetFile, file, copy.deepcopy(G), copy.deepcopy(newGraph), method,l)
        tce(copy.deepcopy(G), seedsetFile, file, copy.deepcopy(newGraph), myFile, copy.deepcopy(newGraph), method,l)
    else:
        if method == 'propinquity':
            tmpGraph, tmpDict = propinquityD(seeds, copy.deepcopy(G), copy.deepcopy(newGraph), copy.deepcopy(newGraph), d, a, b)
        elif method == 'k-path':
            tmpGraph, tmpDict = KpathAlg(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))
        elif method == 'CNR':
            tmpGraph, tmpDict = cnr(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))
        elif method == 'SimRank':
            tmpGraph, tmpDict = simRank(seeds, copy.deepcopy(G), copy.deepcopy(newGraph), hops)
        elif method == 'MultiplyWeight':
            tmpGraph, tmpDict = FilesAdjAll(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))
        elif method == 'Triangles':
            tmpGraph, tmpDict = reWeighting(seeds, copy.deepcopy(G), copy.deepcopy(newGraph)) 
        elif method == 'Loop edge':
            tmpGraph, tmpDict = addLoopEdge(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))
                    
        lte(seedsetFile, file, 1, copy.deepcopy(tmpGraph), copy.deepcopy(tmpDict), method,l)
        tce(copy.deepcopy(tmpGraph), seedsetFile, file, copy.deepcopy(tmpDict), myFile, copy.deepcopy(tmpDict), method,l)
        newLCD(seedsetFile, file, copy.deepcopy(tmpGraph), copy.deepcopy(tmpDict), method,l)
            
            
        del tmpGraph
        del tmpDict
    print("{} method completed.".format(method))
    print("------------------------------")


dataset_path = './seperatedExps/datasets/lfr/'
file = 'test1.csv'

#myFile is the input csv file
#myFile = 'lfrEdgelistN1000MU0.1*.csv'
#myFile = 'lfrEdgelistN5000MU0.40*.csv'
#myFile = 'lfr3.csv'
#myFile = 'youTube.csv'
#myFile = 'dblp.csv'
#myFile = 'NetCol.csv'
myFile = dataset_path + file
#myFile = 'Physical_Interactions.IREF-BIOGRID.csv'

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = file[:-4]

l = 11
hops = 2

#copy input csv file to the weighted folder in order to run the experiments with the initial file too
#shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )

#community file
communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'

#seeds = read seed nodes from seedFile
seedFile = open('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', 'r')
seeds = seedFile.readline().split(" ")
seedsetFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt'

#keep as seed the 1st seed of seedFile
seed = seeds[0]

#Creation of the graph with the input file
G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')
Graph = defaultdict(dict)
with open(myFile, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
#        if row[0] in seeds or row[1] in seeds:
            Graph[row[0]][row[1]] = row[2] 
            Graph[row[1]][row[0]] = row[2]
#G = nx.Graph(Graph)

newGraph = {k: {kk: float(vv) for kk, vv in v.items()}
         for k, v in Graph.items()}


    
G = nx.Graph(newGraph)


for source, target in G.edges():
    G[source][target]['weight'] = newGraph[source][target]
    
print("------------------------------")

methods = ['plain', 'propinquity', 'k-path', 'CNR', 'SimRank', 'MultiplyWeight', 'Triangles', 'Loop edge' ]

d = 2
a = 3
b = 11

for method in methods:
    call_method(method, seedsetFile, file, G, newGraph, l, d, a, b, hops)



#Give ground truth community details for metrics computation
seedstr = ' ' +seed+ ' ' # without spaces eg if seed = 10 if is sees 101 firstly it will stop and take as community the one that 101 belongs to.

## !!!!!! if seed is the first item of a line it won't be read properly. SHOULD ADD SPACE IN FRONT OF EACH LINE OF COMMUNITYFILE!


with open(communityFile, 'r') as comm:
    for line in comm:
        if seedstr in line:
            GTC = [n for n in line.strip().split(' ')]
trueComm = len(GTC)



#create seperated metrics file for each algorithm in the communities dir
#os.chdir('communities')

metrics(file, GTC, trueComm)

print("Computation of metrics completed.")
print("------------------------------")


















