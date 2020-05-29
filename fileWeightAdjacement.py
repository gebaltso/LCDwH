#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:56:49 2019

@author: georgiabaltsou
"""

import networkx as nx
                
 
               
def FilesAdjAll(seeds, G, Graph): 
            
    
    for node in Graph:
        if node in seeds:
            for i in Graph[node]:
                Graph[node][i] = float(Graph[node][i])*3 
                Graph[i][node] = float(Graph[i][node])*3 
                
                
                
    G = nx.Graph(Graph)
        
    for source, target in G.edges():
        G[source][target]['weight'] = Graph[source][target]
            
                
    return G, Graph





            
                        