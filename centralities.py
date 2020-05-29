#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:53:16 2020

@author: georgiabaltsou
"""

import networkx as nx
import csv
import os
import time
import shutil
import sys
import copy
from collections import defaultdict

#change dir
os.chdir('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/')

#myFile is the input csv file with the LFR parameters in its name
#myFile = 'lfrEdgelistN5000MU0.40*.csv'
#finalReadFile = 'lfrEdgelistN5000MU0.40*NODES.csv'
#finalFile = 'lfrEdgelistN5000MU0.40*NODESFinal.csv'
myFile = 'NetCol.csv'
finalFile = 'NetBetCloseCentra.csv'
#finalFile = 'NetColCloseCentra.csv'
#finalFile = 'NetColEigenCentra.csv'
#finalReadFile = 'dblpNODES.csv'
#finalFile = 'dblpNODESFinal.csv'
#myFile = 'lfrEdgelistN200MU0.10*.csv'
#finalReadFile = 'lfrEdgelistN200MU0.10*NODES.csv'
#finalFile = 'lfrEdgelistN200MU0.10*NODESFinal.csv'
#myFile = 'football.csv'
#myFile = 'youTube.csv'
#myFile = 'karate.csv'
#finalReadFile = 'karateNODES.csv'
#finalFile = 'karateEigenCentra.csv'
#finalFile = 'karateCloseCentra.csv'
#finalFile = 'karateBetCentra.csv'

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = myFile[:-4]

#copy input csv file to the weighted folder in order to run the experiments with the initial file too
#shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )

#community file for Lemon algorithm
#communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'

Graph = defaultdict(dict)
with open(myFile, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
#        if row[0] in seeds or row[1] in seeds:
            Graph[row[0]][row[1]] = row[2] 
            Graph[row[1]][row[0]] = row[2]
G = nx.Graph(Graph)


#eigen_centrality = nx.eigenvector_centrality(G, weight=Graph.values())
#(sorted((v, '{:0.2f}'.format(c)) for v, c in eigen_centrality.items()))
#
#
#with open(finalFile, 'a') as out_file:
#    writer = csv.writer(out_file, delimiter=';')
#    
#    for v, c in eigen_centrality.items():
#    
#    
#        writer.writerow([v, '{:0.2f}'.format(c)])

#close_centrality = nx.closeness_centrality(G)
#(sorted((v, '{:0.2f}'.format(c)) for v, c in close_centrality.items()))
#
#
#with open(finalFile, 'a') as out_file:
#    writer = csv.writer(out_file, delimiter=';')
#    
#    for v, c in close_centrality.items():
#    
#    
#        writer.writerow([v, '{:0.2f}'.format(c)])
        
        
print(Graph.values())



bet_centrality = nx.betweenness_centrality(G,k=500, weight=Graph.values())
(sorted((v, '{:0.2f}'.format(c)) for v, c in bet_centrality.items()))


with open(finalFile, 'a') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    
    for v, c in bet_centrality.items():
    
    
        writer.writerow([v, '{:0.2f}'.format(c)])



























