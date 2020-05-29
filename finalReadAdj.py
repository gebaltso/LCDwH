#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 14:27:28 2018

@author: georgiabaltsou
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import csv
import collections


SourceFile = '/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv'
TestFile = '/Users/georgiabaltsou/Desktop/test.csv'
TestFile2 = '/Users/georgiabaltsou/Desktop/test 2.csv'
TestFile5 = '/Users/georgiabaltsou/Desktop/test5.csv'

sourceNodes = []
nodes = []
weights = []

nodesTmp = []
weightsTmp = []

with open(TestFile2) as csvfile:
    dataFile = csv.reader(csvfile,skipinitialspace=True, delimiter = ',')
        
    for row in dataFile:
         sourceNodes.append(row[0])
         
         for y in range(len(row)):
             if(y%2 != 0):
                 nodesTmp.append(row[y])
             else:
                 if(y != 0):
                     weightsTmp.append(row[y])
         nodes.append(nodesTmp)
         nodesTmp = []
         weights.append(weightsTmp)
         weightsTmp = []
    
#gia na afairesw ta ' ' apo ta weights  
weights = [list(map(float, grp)) for grp in weights]

#print('nodes = ', nodes)
print('weights = ', weights)
#print('Source Nodes = ', sourceNodes)

graph = collections.defaultdict(list)
edges = {}

for i in range (0,len(sourceNodes)):
    for j in range (0, len(nodes[i])):
            graph[sourceNodes[i]].append(nodes[i][j])
            edges[sourceNodes[i], nodes[i][j]] = weights[i][j]


#print("Edges with their weights: ", edges)
#print(dict(graph))

G = nx.Graph(graph)

#print("Nodes of the graph: ", G.nodes())
#print("Edges of the graph: ", G.edges)


#na mh sxediazontai oi aksones    
plt.axis('off')         

#sxediasmos grafou
nx.draw(G)




















