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



#method = 'plain'
#
#lte(seedsetFile, file, 1, copy.deepcopy(G), copy.deepcopy(newGraph), method,l)
#lte(seedsetFile, file, 3, copy.deepcopy(G), copy.deepcopy(newGraph), method,l)
#newLCD(seedsetFile, file, copy.deepcopy(G), copy.deepcopy(newGraph), method,l)
#tce(copy.deepcopy(G), seedsetFile, file, copy.deepcopy(newGraph), myFile, copy.deepcopy(newGraph), method,l)
#print("Initial method completed.")
#print("------------------------------")
#
#
#graphProp, graphPropdict = propinquityD(seeds, copy.deepcopy(G), copy.deepcopy(newGraph), copy.deepcopy(newGraph), 2, 3, 11)
#
#method = 'propinquity'
##print(graphPropdict)
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict), method,l)
#tce(copy.deepcopy(graphProp), seedsetFile, file, copy.deepcopy(graphPropdict), myFile, copy.deepcopy(graphPropdict), method,l)
#newLCD(seedsetFile, file, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict), method,l)
#print("Propinquity method completed.")
#print("------------------------------")
#
#del graphProp
#del graphPropdict
#
##graphKpath, graphKpathdict = KpathAlg(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphKpath, graphKpathdict = KpathAlg(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))
#####print(graphKpathdict)
#
#method = 'k-path'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphKpath), copy.deepcopy(graphKpathdict), method,l)
#tce(copy.deepcopy(graphKpath), seedsetFile, file, copy.deepcopy(graphKpathdict), myFile, copy.deepcopy(graphKpathdict), method,l)
#newLCD(seedsetFile, file, copy.deepcopy(graphKpath), copy.deepcopy(graphKpathdict), method,l)
#print("k-path method completed.")
#print("------------------------------")
#
#del graphKpath
#del graphKpathdict
#
##graphCNR, graphCNRdict = cnr(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphCNR, graphCNRdict = cnr(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))
#
###print(graphCNRdict)
#
#method = 'CNR'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphCNR), copy.deepcopy(graphCNRdict), method,l)
#tce(copy.deepcopy(graphCNR), seedsetFile, file, copy.deepcopy(graphCNRdict), myFile, copy.deepcopy(graphCNRdict), method,l)
#newLCD(seedsetFile, file, copy.deepcopy(graphCNR), copy.deepcopy(graphCNRdict), method,l)
#print("CNR weighted graph created.")
#print("------------------------------")
#
#del graphCNR
#del graphCNRdict

##graphSR, graphSRdict = simRank(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
graphSR, graphSRdict = simRank(seeds, copy.deepcopy(G), copy.deepcopy(newGraph), hops)

#print(graphSRdict)

method = 'SimRank'

lte(seedsetFile, file, 1, copy.deepcopy(graphSR), copy.deepcopy(graphSRdict), method,l)
tce(copy.deepcopy(graphSR), seedsetFile, file, copy.deepcopy(graphSRdict), myFile, copy.deepcopy(graphSRdict), method,l)
newLCD(seedsetFile, file, copy.deepcopy(graphSR), copy.deepcopy(graphSRdict), method,l)
print("SimRank weighted graph completed.")
print("------------------------------")

#del graphSR!
#del graphSRdict

#
##graphM, graphMdict = FilesAdjAll(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphM, graphMdict = FilesAdjAll(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))
#
#method = 'MultiplyWeight'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphM), copy.deepcopy(graphMdict), method,l)
#tce(copy.deepcopy(graphM), seedsetFile, file, copy.deepcopy(graphMdict), myFile, copy.deepcopy(graphMdict), method,l)
#newLCD(seedsetFile, file, copy.deepcopy(graphM), copy.deepcopy(graphMdict), method,l)
#print("Weighted graph completed.")
#print("------------------------------")
#
#del graphM
#del graphMdict
#
##graphRW, graphRWdict = reWeighting(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphRW, graphRWdict = reWeighting(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))   
#
#method = 'Triangles'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphRW), copy.deepcopy(graphRWdict), method,l)
#tce(copy.deepcopy(graphRW), seedsetFile, file, copy.deepcopy(graphRWdict), myFile, copy.deepcopy(graphRWdict), method,l)
#newLCD(seedsetFile, file, copy.deepcopy(graphRW), copy.deepcopy(graphRWdict), method,l)
#print("Re-Weighting of edges done.")
#print("------------------------------")
#
#del graphRW
#del graphRWdict
#
##graphLoop, graphLoopdict = addLoopEdge(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphLoop, graphLoopdict = addLoopEdge(seeds, copy.deepcopy(G), copy.deepcopy(newGraph))
#
#method = 'Loop edge'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphLoop), copy.deepcopy(graphLoopdict), method,l)
#tce(copy.deepcopy(graphLoop), seedsetFile, file, copy.deepcopy(graphLoopdict), myFile, copy.deepcopy(graphLoopdict), method,l)
#newLCD(seedsetFile, file, copy.deepcopy(graphLoop), copy.deepcopy(graphLoopdict), method,l)
#print("Loop edges added.")
#print("------------------------------")
#
#del graphLoop
#del graphLoopdict

#Give ground truth community details for metrics computation
seedstr = ' ' +seed+ ' ' # without spaces eg if seed = 10 if is sees 101 firstly it will stop and take as community the one that 101 belongs to.

## !!!!!! if seed is the first item of a line it won't be read properly. SHOULD ADD SPACE IN FRONT OF EACH LINE OF COMMUNITYFILE!


with open(communityFile, 'r') as comm:
    for line in comm:
        if seedstr in line:
            GTC = [n for n in line.strip().split(' ')]
trueComm = len(GTC)
print(trueComm)


#create seperated metrics file for each algorithm in the communities dir
#os.chdir('communities')

metrics(file, GTC, trueComm)

print("Computation of metrics completed.")
print("------------------------------")


















