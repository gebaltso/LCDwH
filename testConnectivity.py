#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:50:03 2019

@author: georgiabaltsou
"""

import networkx as nx
import numpy as np

def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors

def findNeighboorOfC(G, C):
    neighbors = []
    neighborsOfC = []
    for j in C:
        for i in G.neighbors(j):
            neighbors.append(i)
        
    neighborsOfC = np.unique(neighbors)
    
    return neighborsOfC

#calculation of local modularity M
def findM(G, S):
    
    #cut
    cut = nx.cut_size(G,S, weight='weight')
    #print("cut =", cut)
    
    #volume
    vol = nx.cuts.volume(G, S, weight='weight')
    #print("vol =", vol)

    M = (vol - cut) / (2*cut)
    
    return M
    
def deg(u):
    deg = G.degree(u)
      
    return deg

###### main program #######
G = nx.Graph()
#G = nx.read_weighted_edgelist("myFile.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("testFile2.csv",encoding='utf-8-sig', create_using=nx.Graph(), delimiter=";")
G = nx.read_weighted_edgelist("karate.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("filteredOutputCos.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("filteredOutputEucl.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("filteredOutputPearson.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFilePearson.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFileCosine.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFileEuclidean.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("pearsonSupera.csv", create_using=nx.Graph(), delimiter=";")

#print("Edges: ", G.number_of_edges()) # 2671753
#print("Nodes: ", G.number_of_nodes())  # 16943

#v = 'A_23_P251480' #ΝΒΝ gene
#v = 'supera'
#v = 'amputation'
#v = 'smoking'
#v = 'E'
v = '10'

print("Graph created")

#create a new sub-graph S with v
S = []
S.append(v)


N = findNeighboorOfu(G,v)

print(nx.is_connected(G))


print(deg(v))












