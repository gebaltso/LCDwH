#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:13:46 2019

@author: georgiabaltsou

2016-Zhou-Local Community Detection Algorithm Based on Minimal Cluster
Edited for weighted graphs
keep the closer node but if there are more than 1 I look for the max weighted edge.
"""

import networkx as nx
import numpy as np 
import csv
import os
import time

#find the neighbors of node u
def findNeighboorOfu(G,u):

    return list((G.neighbors(u)))

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
def minimalCluster(G, s, Gdict):
       
    neighbors = []    
    maxNumber = 0
    maxWeight = 0
    global node
    
    for u in findNeighboorOfu(G,s):
        commonNeighbors = sorted(nx.common_neighbors(G, s, u))
                    
        if (len(commonNeighbors) > maxNumber):
            maxNumber = len(commonNeighbors)
            wmax = G.get_edge_data(s, u)
            maxWeight = wmax['weight']
            neighbors = commonNeighbors
            neighbors.append(s)
            neighbors.append(u)
            node = u
            
        elif (len(commonNeighbors) == maxNumber):
            wcur = G.get_edge_data(s, u)
            curWeight = wcur['weight']
            if(curWeight > maxWeight):
                maxNumber = len(commonNeighbors)
                maxWeight = curWeight
                neighbors = commonNeighbors
                neighbors.append(s)
                neighbors.append(u)
                node = u
    
    minCluster = np.unique(neighbors)
    
    return minCluster

#calculation of local modularity M
def findM(G, LC, Gdict):
    
    #cut
    cut = nx.cut_size(G, LC, weight='weight')
    
    #volume
    vol = nx.cuts.volume(G, LC, weight='weight')
       
#    if cut == 0: return vol

    M = (vol - cut) / (2*cut)
    
    return M


    ###### main program #######
def newLCD(seedsetFile, myFile, G, Gdict, method,l):
    
    
    start_time = time.time()
    
    alg = 'newLCD'
    
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().rstrip('\n').split(" ")
    lenS = len(seeds)

    LCInitial = []

    
    # arxikopoihsh ths seed list
    global s
    s = []
    
    for i in range(lenS):
        LCInitial.append(seeds[i])
        s.append(seeds[i])       
      
    # ws LC pairnw tous kontinous komvous tou seed alla an oi seeds den einai 1 pairnw autous ws LC. 
    if lenS == 1:
         LC = minimalCluster(G, seeds[0], Gdict)
         
    else:
        LC = LCInitial

    NLC = {}
    NLCkeys = findNeighboorOfC(G, LC)
    for i in NLCkeys:
        NLC[i] = 0

    previousNLC = {}
    
    while (NLC != previousNLC and len(LC)<l):
        
        tmpLC = list(LC)

        previousNLC = NLC
        curmax = 0
        NLCscores = {}

        for u in NLC:
            
            tmpLC.append(u)

            curM = findM(G, tmpLC, Gdict)
            if curM > curmax:
                NLCscores.clear()
                NLCscores[u] = findM(G, tmpLC, Gdict)
                curmax = curM
            
                
            tmpLC.remove(u)

        maximum = max(NLCscores, key=NLCscores.get)
               
        if (type(LC) != list):
            LC = LC.tolist()

        if(maximum not in LC):
            LC.append(maximum)
       
           
        ΝLCtmp = findNeighboorOfC(G, LC)
        
        NLCNew = np.setdiff1d(ΝLCtmp, LC)
         
        for j in NLCNew:
            NLC[j] = 0
                   
    print("NewLCD time: ", time.time() - start_time)    
       
    with open('./communities/'+str(myFile)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('./communities/'+str(myFile)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm", "Seed node", "Method", "Community"])
        
        row = [alg] + ["\n".join(seeds)]+[method] + list(LC)
        
        writer.writerow(row)