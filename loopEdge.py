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



def addLoopEdge(seeds, G, Graph):

    for node in seeds:
        Graph[node][node] = 1
        for i in Graph[node]:
            Graph[i][i] = 1
         
            
    G = nx.Graph(Graph)
        
    for source, target in G.edges():
        G[source][target]['weight'] = Graph[source][target]
            
                
    return G, Graph

