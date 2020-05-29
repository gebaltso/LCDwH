#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:33:00 2019

@author: georgiabaltsou
"""

import networkx as nx
import csv
import os
import time
import shutil
import sys
from collections import defaultdict

os.chdir('/Users/georgiabaltsou/Desktop/Datasets/wiki/')

#myFile is the input csv file with the LFR parameters in its name
#myFile = 'lfrEdgelistN1000000MU0.10*.csv'
myFile = 'wikiW.csv'
#commFile = 'communityFile.txt'
#myFile = 'youtubeNewFinal.csv'
#commFile = 'youtubeCommunityNewFinal.txt'
#myFile = 'youTube.csv'
#myFile = 'Co-expression.Ramaswamy-Golub-2001.csv'
#commFile = 'communityFile.txt'
#myFile = 'test.csv'
#commFile = 'communityTest.txt'


Graph = defaultdict(dict)
with open(myFile, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
        Graph[row[0]][row[1]] = row[2] 
        Graph[row[1]][row[0]] = row[2]
G = nx.Graph(Graph)



#calculate the number of edges and the number of nodes of the input graph
numberOfEdges = G.number_of_edges()
numberOfNodes = G.number_of_nodes()   
print("The network has", numberOfNodes, "nodes with", numberOfEdges, "edges.")

G.remove_edges_from(nx.selfloop_edges(G))

numberOfEdges = G.number_of_edges()
numberOfNodes = G.number_of_nodes()   
print("The network has", numberOfNodes, "nodes with", numberOfEdges, "edges.")


#count lines in txt file
#with open(commFile) as f:
#    for i, l in enumerate(f):
#        pass
#print(i + 1)




