#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:48:32 2019

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

##simrank from networkx. Too slow.

    
def simRank(seeds, G, Graph): 
    

    for n in seeds:
        for t in list(Graph[n].keys()):

            sim = nx.simrank_similarity(G, n, t, importance_factor=0.8, max_iterations=2, tolerance=0.0001)
            Graph[n][t] = sim + 1
            Graph[t][n] = sim + 1


    G = nx.Graph(Graph)
        
    for source, target in G.edges():
        G[source][target]['weight'] = Graph[source][target]


                
    return G, Graph

