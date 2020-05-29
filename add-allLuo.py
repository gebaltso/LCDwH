#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:58:53 2019

@author: georgiabaltsou
"""

#2008-F. Luo et al. / Exploring local community structures in large networks
# Add-all addition

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

#v = 'A_23_P251480' #ΝΒΝ gene
#v = 'supera'
#v = 'amputation'
#v = 'smoking'
#v = 'E'
v = '34'

print("Graph created")

#create a new sub-graph S with v
S = []
S.append(v)

#find the initial Modularity
initialM = findM(G, S)


#do 1
while True:
    
    #create a new neighbor set N with adjacent vertices of v
    N = findNeighboorOfu(G,v)
    
    #addition step
    #add all vertex in N to subgraph S
    for node in N:
        S.append(node)
    
    
    #deletion step
    #do 2
    while True:
    
        #create a new list deleteQ
        deleteQ = []
        
        #for the computation of DM
        tmpNewC = S
        
        #for each vertex ui in Vs
        for ui in S:
            tmpNewC.append(ui)
            tmpM = findM(G, tmpNewC)
            DM = tmpM - initialM
            
            if(DM>0):
                
        
        #end of do 2
        if(len(deleteQ) !=0):
            break




    #end of do 1
    if(newN != N):
        break







