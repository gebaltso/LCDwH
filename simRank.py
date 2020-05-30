#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:58:38 2020

@author: georgiabaltsou
"""



import sys
import copy
import networkx as nx
import csv
import os
import time
import shutil
from collections import defaultdict
from numpy import array
import matplotlib.pyplot as plt


##change dir
#os.chdir('seperatedExps/datasets/lfr/')
#
##myFile is the input csv file
##myFile = 'lfrEdgelistN1000MU0.1*.csv'
##myFile = 'lfrEdgelistN5000MU0.40*.csv'
##myFile = 'karate.csv'
#myFile = 'lfr1.csv'
##myFile = 'youTube.csv'
##myFile = 'dblp.csv'
##myFile = 'NetCol.csv'
##myFile = 'agilentPearson6.csv'
##myFile = 'Physical_Interactions.IREF-BIOGRID.csv'
#
##file is the input file with the LFR parameters in its name, in string format(without .csv)
#file = myFile[:-4]
#
#l = 10
#
##copy input csv file to the weighted folder in order to run the experiments with the initial file too
##shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )
#
##community file
#communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'
#
##seeds = read seed nodes from seedFile
#seedFile = open('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', 'r')
#seeds = seedFile.readline().split(" ")
#seedsetFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt'
#
##keep as seed the 1st seed of seedFile
#seed = seeds[0]




#Creation of the graph with the input file
#G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')
#Graph = defaultdict(dict)
#with open(myFile, 'r') as read_file: 
#    reader = csv.reader(read_file, delimiter=';')
#    for row in reader:
##        if row[0] in seeds or row[1] in seeds:
#            Graph[row[0]][row[1]] = row[2] 
#            Graph[row[1]][row[0]] = row[2]
##G = nx.Graph(Graph)
#
#newGraph = {k: {kk: float(vv) for kk, vv in v.items()}
#         for k, v in Graph.items()}
#
#
#    
#G = nx.Graph(newGraph)
#
#
#for source, target in G.edges():
#    G[source][target]['weight'] = newGraph[source][target]
#    
#print("------------------------------")

def simRank(seeds, G, newGraph, hops, reWire):
    C = nx.Graph() #dimiourgw arxika keno grafo
    
    for s in seeds: # gia ka8e seed kataskeuazw ton ypografo tou ws kai depth=hops
        tmp = nx.ego_graph(G, s, radius=hops if reWire else 1)
        C = nx.compose(C, tmp) #enwnw ta epimerous grafhmata. px an oi seed einai 2 enwnw tous 2 ypografous se enan eniaio wste na mhn exw 2typa. Ton C

    print("Nodes=", len(C.nodes()), "Edges=", len(C.edges()))

    if reWire:
        
        for n in seeds: #trexw ton simrank gia olous tous komvous tou C. Allazw ola ta barh metaksu olwn twn komvwn tou C
            sim = nx.simrank_similarity(C, n, target=None, importance_factor=0.8, max_iterations=10, tolerance=0.0001)
            avg_sim = sum(sim.values()) / len(sim.values())
            for m in sim.keys():
                if n == m or avg_sim > sim[m]: continue
                newGraph[n][m] = 1 #allazw ta barh sto original grafo!!!!
                newGraph[m][n] = 1
                
        G = nx.Graph(newGraph) # rewiring
        
        for source, target in G.edges():
            G[source][target]['weight'] = newGraph[source][target]
    else:
        for n in seeds:
            for t in list(newGraph[n].keys()):
                sim = nx.simrank_similarity(C, n, t, importance_factor=0.8, max_iterations=2, tolerance=0.0001)
                newGraph[n][t] += sim
                G[n][t]['weight'] = newGraph[n][t]    
        
    
    return G, newGraph


#nx.draw(C, with_labels=True)
#plt.show()