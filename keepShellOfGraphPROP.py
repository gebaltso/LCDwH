#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:07:16 2020

@author: georgiabaltsou
"""

import networkx as nx
import csv
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


def call_method(method, seedSetFile, file, G, newGraph, l, d, a, b, hops, rewire):
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
            tmpGraph, tmpDict = simRank(seeds, copy.deepcopy(G), copy.deepcopy(newGraph), hops, rewire)
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


dataset = sys.argv[1]
arr = dataset.split('/')

myFile = dataset

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = arr[len(arr) - 1][:-4]

#community file
communityFile = sys.argv[2]
#seeds file
seedsetFile = sys.argv[3]

#seeds = read seed nodes from seedFile
seedFile = open(seedsetFile, 'r')
seeds = seedFile.readline().rstrip('\n').split(" ")



#keep as seed the 1st seed of seedFile
seed = seeds[0]

#Creation of the graph with the input file
G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')
Graph = defaultdict(dict)
with open(myFile, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
            Graph[row[0]][row[1]] = row[2] 
            Graph[row[1]][row[0]] = row[2]

newGraph = {k: {kk: float(vv) for kk, vv in v.items()}
         for k, v in Graph.items()}
    
G = nx.Graph(newGraph)

for source, target in G.edges():
    G[source][target]['weight'] = newGraph[source][target]
    
print("------------------------------")


d = 2 #distance in propinquity
a = 400 #threshold for popinquity
b = 1000 #threshold for popinquity
rewire = True #if True SimRank will rewire the G. Otherwise it will reweight it.
hops = 4 #hops for rewiring distance for SimRank
l = 108 #desired community size


if rewire: methods = ['SimRank']

else: methods = ['plain', 'propinquity', 'k-path', 'CNR', 'SimRank', 'MultiplyWeight', 'Triangles', 'Loop edge' ]


for method in methods:
    call_method(method, seedsetFile, file, G, newGraph, l, d, a, b, hops, rewire)



#Give ground truth community details for metrics computation
seedstr = ' ' +seed+ ' ' # without spaces eg if seed = 10 if is sees 101 firstly it will stop and take as community the one that 101 belongs to.

## !!!!!! if seed is the first item of a line it won't be read properly. SHOULD ADD SPACE IN FRONT OF EACH LINE OF COMMUNITYFILE!


with open(communityFile, 'r') as comm:
    for line in comm:
        if seedstr in line:
            GTC = [n for n in line.strip().split(' ')]
trueComm = len(GTC)



#create seperated metrics file for each algorithm in the communities dir
metrics(file, GTC, trueComm)

print("Computation of metrics completed.")
print("------------------------------")


