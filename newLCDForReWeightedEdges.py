#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:38:46 2019

@author: georgiabaltsou
"""

#2016-Zhou-Local Community Detection Algorithm Based on Minimal Cluster
#Edited for weighted graphs
#keep the closer node but if there are more than 1 I look for the max weighted edge.


import networkx as nx
import numpy as np 
import csv
import os

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
    maxWeight = 0
    global node
    
    for u in findNeighboorOfu(G,s):
        commonNeighbors = sorted(nx.common_neighbors(G, s, u))
        
#        print("common ",s, "with",u, "=",commonNeighbors )       
        
        if (len(commonNeighbors) > maxNumber):
            maxNumber = len(commonNeighbors)
            wmax = G.get_edge_data(s, u, default=0)
            maxWeight = wmax['weight']
            neighbors = commonNeighbors
            neighbors.append(s)
            neighbors.append(u)
            node = u
            
        elif (len(commonNeighbors) == maxNumber):
            wcur = G.get_edge_data(s, u, default=0)
            curWeight = wcur['weight']
            if(curWeight > maxWeight):
                maxNumber = len(commonNeighbors)
                maxWeight = curWeight
                neighbors = commonNeighbors
                neighbors.append(s)
                neighbors.append(u)
                node = u
    
    minCluster = np.unique(neighbors)
    #print("closer node to", s, "is:", node, ", and the weight between them is=", maxWeight)
    
    return minCluster

#calculation of local modularity M
def findM(G, LC):
    
    #cut
    cut = nx.cut_size(G,LC, weight='weight')
    #print("cut =", cut)
    
    #volume
    vol = nx.cuts.volume(G, LC, weight='weight')
    #print("vol =", vol)

    M = (vol - cut) / (2*cut)
    
    return M


    ###### main program #######
def newLCD(file, s, myFile):
    
#    node1 = file.split("<")[1].split("-")[0]
#    
#    node2 = file.split("-")[1].split(">")[0]
#    
#    wName = file.split(">")[1].split(".")[0]
    
    G = nx.Graph()
    #G = nx.read_weighted_edgelist("myFile.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("testFile2.csv",encoding='utf-8-sig', create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("karate.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("karateChanged.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("filteredOutputCos.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("filteredOutputEucl.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("filteredOutputPearson.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("finalGeneFilePearson.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("finalGeneFileCosine.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("finalGeneFileEuclidean.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("pearsonSupera.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("netCol/netColMultiply100.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("netColAll.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("dblp/dblpWeighted.csv", create_using=nx.Graph(), delimiter=";")
    G = nx.read_weighted_edgelist(file, create_using=nx.Graph(), delimiter=";")
    
    #print("Edges: ", G.number_of_edges()) # 2671753
    #print("Nodes: ", G.number_of_nodes())  # 16943
    
    #s = 'A_23_P251480' #ΝΒΝ gene
    #s = 'supera'
    #s = 'amputation'
    #s = 'smoking'
    #s = 'E'
    #s = '78' #Newman
    #s = '281' #Sole
    #s = '18323' #dblp
    #s = '269383'
    
    
    #print("Graph created")
    
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
        
    #    print("LC = ", LC)
               
        ΝLCtmp = findNeighboorOfC(G, LC)
    #    print("NLCtmp =", ΝLCtmp)
        
        NLC = np.setdiff1d(ΝLCtmp, LC)
    #    print(NLC)
        
        initialM = findM(G, LC) 
              
#    print("-----------------------------------")
#    print("Number of nodes in C: ", len(LC))       
#    print("Local Community is:", LC)    
        
       
    with open('communities/newLCD_communities'+str(myFile)+'.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('communities/newLCD_communities'+str(myFile)+'.csv').st_size == 0:
            writer.writerow(["Seed Node", "Community"])
        
#        row = [node1]+[node2]+[wName]+[s]+LC
        row = [s]+LC
        
        writer.writerow(row)
        
#counter = 0
#
#comm = ['18323', '146590', '240098', '249900', '269383', '319507', '319508', '337203', '339699', '348984', '349177']
#
#for i in LC:
#    if i in comm:
#        counter += 1
#
#print("nodes of ground truth in C: ", counter)
