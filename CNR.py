#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:21:14 2019

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


def cnr(seeds, G, Graph): 
    

    for node in seeds:
        node_nei = len(list(Graph[node].keys()))
        for i in G[node]:
            i_nei = len(list(Graph[i].keys()))
            if G.has_edge(node, i):
                A = 1
            else:
                A = 0
            Ac = len(sorted(nx.common_neighbors(G, node, i)))
            
            c = (2*(A+Ac))/(node_nei+i_nei)
            
            Graph[node][i] = c + 1 #add 1 because c is between 0 and 1
            Graph[i][node] = c + 1
            
           
        
    for source, target in G.edges():
        G[source][target]['weight'] = Graph[source][target]
            
                
    return G, Graph
