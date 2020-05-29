#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:50:59 2019

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
from numpy import array
from testSimRank import simrank

#
##change dir
#os.chdir('seperatedExps/datasets/lfr/')
#
##myFile is the input csv file with the LFR parameters in its name
##myFile = 'lfrEdgelistN1000MU0.1*.csv'
##myFile = 'lfrEdgelistN5000MU0.40*.csv'
#myFile = 'football.csv'
##myFile = 'youTube.csv'
##myFile = 'dblp.csv'
#
##file is the input file with the LFR parameters in its name, in string format(without .csv)
#file = myFile[:-4]
#
##copy input csv file to the weighted folder in order to run the experiments with the initial file too
##shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )
#
##community file for Lemon algorithm
#communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'
#
##seeds = read seed nodes from seedFile
#seedFile = open('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', 'r')
#seeds = seedFile.readline().split(" ")
#seedsetFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt'
#
##keep as seed the 1st seed of seedFile
#seed = seeds[0]
#
##Creation of the graph with the input file
##G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')
#Graph = defaultdict(dict)
#with open(myFile, 'r') as read_file: 
#    reader = csv.reader(read_file, delimiter=';')
#    for row in reader:
##        if row[0] in seeds or row[1] in seeds:
#            Graph[row[0]][row[1]] = row[2] 
#            Graph[row[1]][row[0]] = row[2]
#G = nx.Graph(Graph)
#
#newG = copy.deepcopy(G) #graph
#newGraph = copy.deepcopy(Graph)  #dictionary


def addLoopEdge(seeds, G, Graph):

    for node in seeds:
        Graph[node][node] = 1
        for i in Graph[node]:
            Graph[i][i] = 1
         
            
    G = nx.Graph(Graph)
        
    for source, target in G.edges():
        G[source][target]['weight'] = Graph[source][target]
            
                
    return G, Graph

       








