#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:49:14 2019

@author: georgiabaltsou
"""

import networkx as nx

#computation of all paths starting from s with length = d
def findPathsNoLC(G,s,d):  
    if d == 0:
        return [[s]]
    paths = []
    for neighbor in G[s].keys():
        for path in findPathsNoLC(G,neighbor,d-1):
            if s not in path:
                paths.append([s]+path)
    return paths



def propinquityD(seeds, G, Graph, newGraph, distance, a, b):

    C = nx.Graph()    
    for s in seeds: # for each seed constructing its subgraph till depth = distance
        tmp = nx.ego_graph(G, s, radius=distance)
        C = nx.compose(C, tmp)
        
        
    nodes = list(nx.nodes(C))
    for seed in seeds:
        neighbors_seed = [j for j in C.neighbors(seed)]
        for i in nodes:
            if C.has_edge(seed, i):
                s1 = 1
            else:
                s1 = 0
            neighbors_i = [j for j in C.neighbors(i)]
        
            common = set(neighbors_seed).intersection(set(neighbors_i))

            counter = 0 # find number of edges between the node's neighbors            
            for j in common:
                for k in common:
                    if j in Graph and k in Graph[j] :
                        counter += 1
            counter /= 2 
                
            prop = s1 + len(neighbors_i) + counter
            
            if prop >= b and not G.has_edge(seed, i):
                Graph[seed][i] = 1
                Graph[i][seed] = 1
                
            if prop <= a and G.has_edge(seed, i):
                del Graph[seed][i]
                del Graph[i][seed]


    G = nx.Graph(Graph)
    
    
    for source, target in G.edges():
        G[source][target]['weight'] = Graph[source][target]
    
          


    return G, Graph

