#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:47:48 2019

@author: georgiabaltsou
"""

#2016-Zhou-Local Community Detection Algorithm Based on Minimal Cluster
#For unweighted graphs
#keep the closer node but if there are more than 1 I look for the max weighted edge.


import networkx as nx
import numpy as np 

#find the neighbors of node u
def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors

#find the neighbors of community C
def findNeighboorOfC(G, C):
    neighbors = []
    neighborsOfC = []
    for j in C:
        for i in G.neighbors(j):
            neighbors.append(i)
        
    neighborsOfC = np.unique(neighbors)
    
    return neighborsOfC

#find the minimal cluster containing the initial node and the closer neighbors of it
def minimalCluster(G, s):
    
    neighbors = []    
    maxNumber = 0
    global node
    
    for u in findNeighboorOfu(G,s):
        commonNeighbors = sorted(nx.common_neighbors(G, s, u))
        
#        print("common ",s, "with",u, "=",commonNeighbors )       
        
        if (len(commonNeighbors) > maxNumber):
            maxNumber = len(commonNeighbors)
#            wmax = G.get_edge_data(s, u, default=0)
#            maxWeight = wmax['weight']
            neighbors = commonNeighbors
            neighbors.append(s)
            neighbors.append(u)
            node = u
            
#        elif (len(commonNeighbors) == maxNumber):
#            wcur = G.get_edge_data(s, u, default=0)
#            curWeight = wcur['weight']
#            if(curWeight > maxWeight):
#                maxNumber = len(commonNeighbors)
#                maxWeight = curWeight
#                neighbors = commonNeighbors
#                neighbors.append(s)
#                neighbors.append(u)
#                node = u
                
                
        elif (len(commonNeighbors) == maxNumber):
#            wcur = G.get_edge_data(s, u, default=0)
#            curWeight = wcur['weight']
#            if(curWeight > maxWeight):
            maxNumber = len(commonNeighbors)
#                maxWeight = curWeight
            neighbors = commonNeighbors
            neighbors.append(s)
            neighbors.append(u)
            node = u
                
    
    minCluster = np.unique(neighbors)
    print("closer node to", s, "is:", node)
    
    return minCluster

#calculation of local modularity M
def findM(G, LC):
    
    #cut
#    cut = nx.cut_size(G, LC, weight='weight')
    cut = nx.cut_size(G, LC)
    
#    if (cut == 0):
#        cut = 0.0000000000000000000001
    
    #print("cut =", cut)
    
    #volume
#    vol = nx.cuts.volume(G, LC, weight='weight')
    vol = nx.cuts.volume(G, LC)
    #print("vol =", vol)

    M = (vol - cut) / (2*cut)
    
    return M


###### main program #######

G = nx.Graph()
#G = nx.read_weighted_edgelist("myFile.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("testFile2.csv",encoding='utf-8-sig', create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("karate.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("karateUnw.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("karateChanged.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("filteredOutputCos.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("filteredOutputEucl.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("filteredOutputPearson.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFilePearson.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFileCosine.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFileEuclidean.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("pearsonSupera.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("adjnoun.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("email/email.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("football/football.csv", create_using=nx.Graph(), delimiter=";")
G = nx.read_edgelist("dblp/dblp.csv", create_using=nx.Graph(), delimiter=";")

#print("Edges: ", G.number_of_edges()) # 2671753
#print("Nodes: ", G.number_of_nodes())  # 16943

#s = 'A_23_P251480' #ΝΒΝ gene
#s = 'supera'
#s = 'amputation'
#s = 'smoking'
#s = 'E'
#s = '274042'
s = '319507'

#GTC = ['2', '3', '4', '56', '57', '58', '59', '63', '137', '138', '192', '193', '194', '195', '281', '286', '305', '408', '412', '456', '520', '532', '571', '586', '587', '606', '622', '625', '633', '634', '635', '636', '648', '670', '685', '691', '711', '718', '755', '762', '774', '803', '815', '826', '832', '845', '849', '863','865', '880', '882', '884', '899', '901', '921', '928', '982', '990', '993', '994', '1001' ]
GTC = ['183323', '146590', '240098', '249900', '269383', '319507', '319508', '337203', '339699', '348984', '349177']
       
       
#print(GTC)
print("Graph created")

#find the minimal cluster containing the initial node s and the closer neighbors of it
LC = minimalCluster(G, s)
#print("LC=", LC)

#find the neighbors of minimal cluster LC
NLC = findNeighboorOfC(G, LC)
#print("NLC =", NLC)

#calculation of initial local modularity M
initialM = findM(G, LC)
#print("Initial M=", initialM)

previousNLC = []

while (list(NLC) != list(previousNLC)):
    
    tmpLC = list(LC)
    tmpM = 0
    DM = 0
    maxDM = 0
    previousNLC = list(NLC)
                    
    for u in NLC:                   
        tmpLC.append(u)
        tmpM = findM(G, tmpLC)
        
        #######enisxush komvwn tis koinothtas pou anhkei o seed komvos
        if(u in GTC):
            tmpM = 100*tmpM        
    
        DM = tmpM - initialM
          
        
        if (DM > maxDM):
            if (u not in LC):
                maxDM = DM
                node = u 
                          
        tmpLC = list(LC)  
    
    if (type(LC) != list):
        LC = LC.tolist()
        
    if(node not in LC):
        LC.append(node)
    
    print("LC = ", sorted(LC))
           
    ΝLCtmp = findNeighboorOfC(G, LC)
#    print("NLCtmp =", ΝLCtmp)
    
    NLC = np.setdiff1d(ΝLCtmp, LC)
#    print(NLC)
    
    initialM = findM(G, LC) 
          
        
print("Local Community is:", sorted(LC))        
        

