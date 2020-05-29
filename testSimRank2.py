#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:47:56 2020

@author: georgiabaltsou
"""

import networkx as nx
from numpy import array
import os
import csv
from collections import defaultdict

#change dir
os.chdir('seperatedExps/datasets/lfr/')

#myFile is the input csv file
#myFile = 'lfrEdgelistN1000MU0.1*.csv'
#myFile = 'lfrEdgelistN5000MU0.40*.csv'
#myFile = 'lfrEdgelistN200MU0.10*.csv'
#myFile = 'football.csv'
#myFile = 'youTube.csv'
#myFile = 'dblp.csv'
#myFile = 'karate.csv'
myFile = 'NetCol.csv'

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = myFile[:-4]

Graph = defaultdict(dict)
with open(myFile, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
#        if row[0] in seeds or row[1] in seeds:
            Graph[row[0]][row[1]] = row[2] 
            Graph[row[1]][row[0]] = row[2]
G = nx.Graph(Graph)



sim = nx.simrank_similarity(G)
print("SimRank done")
lol = [[sim[u][v] for v in sorted(sim[u])] for u in sorted(sim)]
sim_array = array(lol)

print(sim_array)