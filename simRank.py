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



def simRank(seeds, G, newGraph, hops, reWire):
    C = nx.Graph() #creation of an empty graph
    
    for s in seeds: # for each seed I create its subgraph till depth = hops
        tmp = nx.ego_graph(G, s, radius=hops if reWire else 1)
        C = nx.compose(C, tmp) #merge the individual graphs. e.g. if |seed| = 2 I merge the 2 subgraphs in one such that I don't have doubles.



    if reWire:
        
        for n in seeds: #run simrank for all nodes in C. Change all the node weights in C.
            sim = nx.simrank_similarity(C, n, target=None, importance_factor=0.8, max_iterations=10, tolerance=0.0001)
            avg_sim = sum(sim.values()) / len(sim.values())
            for m in sim.keys():
                if n == m or avg_sim > sim[m]: continue
                newGraph[n][m] = 1 #change the weights of original graph!
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
