#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:14:09 2018

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
import itertools

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
    
    return minCluster

#calculation of local modularity M
def findM(G, LC):
    
    #cut
    cut = nx.cut_size(G, LC, weight='weight')
    
    #volume
    vol = nx.cuts.volume(G, LC, weight='weight')

    M = (vol - cut) / (2*cut)
    
    return M


    ###### main program #######
def newLCD(file, seedsetFile, myFile, G):
    
    start_time = time.time()
    
    alg = 'newLCD'
    
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().split(" ")
    lenS = len(seeds)
    
    node1 = file.split("<")[1].split("-")[0]
    
    node2 = file.split("-")[1].split(">")[0]
    
    wName = file.split(">")[1].split(".")[0]
    
    #find the minimal cluster containing the initial node s and the closer neighbors of it
#    LC = minimalCluster(G, s)
    LCInitial = []
#    LC.append(s)
    
    # arxikopoihsh ths seed list
    global s
    s = []
    
    for i in range(lenS):
        LCInitial.append(seeds[i])
        s.append(seeds[i])       
        
    if lenS == 1:
         LC = minimalCluster(G, seeds[0])
    else:

        LC = LCInitial

    
    #find the neighbors of minimal cluster LC
    NLC = findNeighboorOfC(G, LC)
    
    #calculation of initial local modularity M
    initialM = findM(G, LC)
    
    previousNLC = []
    
    while (list(NLC) != list(previousNLC) and len(LC)<100):
        
#        print("LC:", len(LC))
#        print("NLC:", len(NLC))
#        print("previousNLC:", len(previousNLC))
        
        tmpLC = list(LC)
        tmpM = 0
        DM = 0
        maxDM = 0
        previousNLC = list(NLC)
             
           
        for u in NLC: 
#            print("u =", u)                  
            tmpLC.append(u)
            tmpM = findM(G, tmpLC)
            DM = tmpM - initialM
              
            
            if (DM > maxDM):
                #if (u not in LC):
                    maxDM = DM
                    node = u 
             
                
            tmpLC = list(LC)  
        
        
        if (type(LC) != list):
            LC = LC.tolist()
            
        if(node not in LC):
            LC.append(node)
    
               
        ΝLCtmp = findNeighboorOfC(G, LC)
        
        NLC = np.setdiff1d(ΝLCtmp, LC)
        
        initialM = findM(G, LC)     
        
       
    with open('communities/'+str(myFile)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('communities/'+str(myFile)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm", "Node 1", "Node 2", "Multiplied Weight", "Seed node", "Community"])
        
        row = [alg]+[node1]+[node2]+[wName]+[s]+LC
#        row = [wName]+[s]+LC
        
        writer.writerow(row)
        
        
    with open('time/time.txt', 'a') as time_file:
        time_file.write('newLCD execution time is:')
        time_file.write(str(time.time() - start_time))
        time_file.write('\n')
        
