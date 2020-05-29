#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:08:26 2020

@author: georgiabaltsou
"""

import networkx as nx
import csv
import os
import time
import shutil
import sys
import igraph
import copy
from collections import defaultdict



#change dir
os.chdir('/Users/georgiabaltsou/Desktop/Datasets/LFRproducts/weighted/normal/LFR8')

#myFile is the input csv file with the LFR parameters in its name
#myFile = 'lfr1.txt'
myFile = 'lfrEdgelistN1000000MU0.80*.csv' #csv for voterank

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = myFile[:-4]

#EigenFile = str(file) + 'EigenCentra.csv'
#CloseFile = str(file) + 'CloseCentra.csv'
#BetFile = str(file) + 'BetCentra.csv'

#copy input csv file to the weighted folder in order to run the experiments with the initial file too
#shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )

#community file for Lemon algorithm
#communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'



#####################################################################################################
# VoteRank for networkX graph (csv input file)
Graph = defaultdict(dict)
with open(myFile, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
#        if row[0] in seeds or row[1] in seeds:
            Graph[row[0]][row[1]] = row[2] 
            Graph[row[1]][row[0]] = row[2]
G = nx.Graph(Graph)


vt = nx.voterank(G,number_of_nodes=100, max_iter= 2)

print(vt)




#####################################################################################################
### For betweenness, cloceseness and eigenvector centrality of igraph
##Needs .txt format input file!!!!!
#Gix = igraph.Graph.Read_Ncol(myFile, weights=True, directed=False)
#
#weight = []
#
#for e in Gix.es():
#  weight.append( e['weight'])
#
#
#bet = Gix.betweenness(weights = weight)
#
#with open(BetFile, "w") as bet_output_file:
#    writer = csv.writer(bet_output_file, delimiter=';')    
#    for v in Gix.vs:    
#        row = [v["name"]] + [bet[v.index]]        
#        writer.writerow(row)
#
#cl = Gix.closeness(weights = weight)
#    
#with open(CloseFile, "w") as close_output_file:
#    writer = csv.writer(close_output_file, delimiter=';')    
#    for v in Gix.vs:    
#        row = [v["name"]] + [cl[v.index]]        
#        writer.writerow(row)
# 
#eig = Gix.eigenvector_centrality(weights = weight)
#       
#with open(EigenFile, "w") as eigen_output_file:
#    writer = csv.writer(eigen_output_file, delimiter=';')    
#    for v in Gix.vs:    
#        row = [v["name"]] + [eig[v.index]]        
#        writer.writerow(row)








