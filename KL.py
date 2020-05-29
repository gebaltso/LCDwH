#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:31:36 2019

@author: georgiabaltsou
"""
#2008-F. Luo et al. / Exploring local community structures in large networks
#The KL-like local community discovery algorithm

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

#s = 'A_23_P251480' #ΝΒΝ gene
#s = 'supera'
#s = 'amputation'
#s = 'smoking'
#s = 'E'
s = '34'


print("Graph created")

S = [] #community

S.append(s)


BC = S #current best community

while True:
    
    CC = BC #current community CC = current best community
    
    prBC = BC #previous best community prBC = current best community

    moved = [] #the marked as "moved" nodes
    
    gain = []
    
    N = findNeighboorOfC(G, S) #neighbors of community S

        
    for node in np.union1d(N,CC): #for every node in current community CC and its neighbor
        for node2 in np.union1d(N,CC):
            if node not in moved:
                
#                gain.append(findM())
    
    
    if(McBC<MprBC):
        break
    



















