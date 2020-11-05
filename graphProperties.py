#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:36:33 2020

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

# Degree of seed node
seed_degree = G.degree(seed)

# Degrees of all nodes in G
degrees = G.degree()
degree_values = [v for k, v in degrees]

# Compute sum of node degrees in G
sum_of_edges = sum(degree_values)

# Compute average degree of G
average_degree = sum_of_edges/G.number_of_nodes()

seedstr = ' ' +seed+ ' '
## !!!!!! if seed is the first item of a line it won't be read properly. SHOULD ADD SPACE IN FRONT OF EACH LINE OF COMMUNITYFILE!

with open(communityFile, 'r') as comm:
    for line in comm:
        if seedstr in line:
            community = [n for n in line.strip().split(' ')]
            
# Find the size of community that seed belongs            
community_size = len(community)

# Find the degree of n inside C
degInCofSeed = 0
for i in community:
    if G.has_edge(seed, i):
        degInCofSeed +=1

