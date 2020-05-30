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
#            maxWeight = float(Gdict[s][u])
            neighbors = commonNeighbors
            neighbors.append(s)
            neighbors.append(u)
            node = u
            
        elif (len(commonNeighbors) == maxNumber):
            wcur = G.get_edge_data(s, u)
            curWeight = wcur['weight']
#            curWeight = float(Gdict[s][u])
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
#    cut = nx.cut_size(G, LC,weight=Gdict.values())
    
    #volume
    vol = nx.cuts.volume(G, LC, weight='weight')
#    vol = nx.cuts.volume(G, LC, weight=Gdict.values())
        

    M = (vol - cut) / (2*cut)
    
    return M


    ###### main program #######
def newLCD(seedsetFile, myFile, G, Gdict, method,l):
    
    
    start_time = time.time()
    
    alg = 'newLCD'
    
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().rstrip('\n').split(" ")
    lenS = len(seeds)
    
#    node1 = file.split("<")[1].split("-")[0]
#    
#    node2 = file.split("-")[1].split(">")[0]
#    
#    wName = file.split(">")[1].split(".")[0]
    
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
         LC = minimalCluster(G, seeds[0], Gdict)
         
    else:

        LC = LCInitial

#    print(LC)
    
    #find the neighbors of minimal cluster LC
#    NLC = findNeighboorOfC(G, LC)
    NLC = {}
    NLCkeys = findNeighboorOfC(G, LC)
    for i in NLCkeys:
        NLC[i] = 0
        
    #calculation of initial local modularity M
#    initialM = findM(G, LC, Gdict)

    
#    previousNLC = []
    previousNLC = {}
    
#    while (list(NLC) != list(previousNLC) and len(LC)<100):
    while (NLC != previousNLC and len(LC)<l):
#    while (len(NLC) > 0 and len(LC)<100):
        
#        print("while: ",(str(time.time() - start_time)))
        
        
#        print("LC:", (LC))
#        print("NLC:", len(NLC))
#        print("previousNLC:", len(previousNLC))
        
        tmpLC = list(LC)
#        tmpLC = LC
#        tmpM = 0
#        DM = 0
#        maxDM = 0
        previousNLC = NLC
        curmax = 0
        NLCscores = {}

        for u in NLC:
            
            tmpLC.append(u)
#            tmpLC.add(u)
#            tmpM = findM(G, tmpLC, Gdict)
#            DM = tmpM - initialM
            curM = findM(G, tmpLC, Gdict)
            if curM > curmax:
                NLCscores.clear()
                NLCscores[u] = findM(G, tmpLC, Gdict)
                curmax = curM
                #print("u=", u, "M=", findM(G, tmpLC, Gdict),  "score=", NLCscores[u])
                
            tmpLC.remove(u)

        maximum = max(NLCscores, key=NLCscores.get)
        

#            if (DM > maxDM):
#                #if (u not in LC):
#                    maxDM = DM
#                    node = u 
#             
#                
#            tmpLC = list(LC)  
#        
#        
        if (type(LC) != list):
            LC = LC.tolist()
#            
#        if(node not in LC):
#            LC.append(node)
        if(maximum not in LC):
            LC.append(maximum)
#            LC.add(maximum)
       
           
        ΝLCtmp = findNeighboorOfC(G, LC)
        
        NLCNew = np.setdiff1d(ΝLCtmp, LC)
         
#        NLCNewkeys = findNeighboorOfC(G, LC)
        for j in NLCNew:
            NLC[j] = 0
           
#        initialM = findM(G, LC, Gdict)
        
#    print("LC= ", LC)
        
        
       
    with open('./communities/'+str(myFile)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('./communities/'+str(myFile)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm", "Seed node", "Method", "Community"])
        
#        row = [alg]+[node1]+[node2]+[wName]+[s]+LC
#        row = [wName]+[s]+LC
        row = [alg] + ["\n".join(seeds)]+[method] + list(LC)
        
        writer.writerow(row)
        
        

        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:42:53 2019

@author: georgiabaltsou
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:13:46 2019

@author: georgiabaltsou

2016-Zhou-Local Community Detection Algorithm Based on Minimal Cluster
Edited for weighted graphs
keep the closer node but if there are more than 1 I look for the max weighted edge.
"""

#import networkx as nx
#import numpy as np 
#import csv
#import os
#import time
#import sys
#import itertools
#
##find the neighbors of node u
#def findNeighboorOfu(G,u):
#    neighbors = set()
#    for i in G.neighbors(u):
#        neighbors.add(i)
#    return neighbors
#
##find the neighbors of community C
#def findNeighboorOfC(G, C):
#    neighborsOfC = set()
#    for j in C:
#        for i in G.neighbors(j):
#            neighborsOfC.add(i)           
#    return neighborsOfC
#
##find the minimal cluster containing the initial node and the closer neighbors of it
#def minimalCluster(G, s, Gdict):
#    
#    commons = {}
#    global node
#    
#    for u in findNeighboorOfu(G,s):
#        commonNeighbors = sorted(nx.common_neighbors(G, s, u))
#        commons[u] = len(commonNeighbors)
#                  
#    node = max(commons, key=commons.get)
#    
#    minCluster = findNeighboorOfu(G,node).intersection(findNeighboorOfu(G,s))
#    minCluster.add(node)
#    minCluster.add(s)
#
# 
#    return minCluster
#
##calculation of local modularity M
#def findM(G, LC, Gdict):
#    
#    #cut
##    cut = nx.cut_size(G, LC, weight='weight')
#    cut = nx.cut_size(G, LC, weight=Gdict.values())
#    
#    #volume
##    vol = nx.cuts.volume(G, LC, weight='weight')
#    vol = nx.cuts.volume(G, LC, weight=Gdict.values())
#
#    M = (vol - cut) / (2*cut)
#    
#    return M
#
#
#    ###### main program #######
#def newLCD(seedsetFile, myFile, G, Gdict):
#    
#    start_time = time.time()
#    
#    alg = 'newLCD'
#    
#    seedFile = open(seedsetFile, 'r')
#    seeds = seedFile.readline().split(" ")
#    lenS = len(seeds)
#    
##    node1 = file.split("<")[1].split("-")[0]
##    
##    node2 = file.split("-")[1].split(">")[0]
##    
##    wName = file.split(">")[1].split(".")[0]
#    
#    #find the minimal cluster containing the initial node s and the closer neighbors of it
#
#    LCInitial = set()
#    
#    # arxikopoihsh ths seed list
#    global s
#    s = []
#    
#    for i in range(lenS):
#        LCInitial.add(seeds[i])
#        s.append(seeds[i])       
#        
#    if lenS == 1:
#         LC = minimalCluster(G, seeds[0], Gdict)        
#    else:
#        LC = LCInitial
#        
#    
#    
#    #find the neighbors of minimal cluster LC
#    NLC = findNeighboorOfC(G, LC)
#
#    DMscores = {}
#
#        
#    #calculation of initial local modularity M
#    M = findM(G, LC, Gdict)
#
#
#    for u in NLC:
#        LC.add(u)
#        DMscores[u] = findM(G, LC, Gdict) - M
#        print("u=", u, "M=", findM(G, LC, Gdict), "InitM=", M, "DM=", DMscores[u])
#        LC.remove(u)
#
#    previousNLC = {}
#    
##    while (NLC != previousNLC and len(LC)<100):
#    while (len(NLC) > 0 and len(LC)<100):
#        
#   
#        node  = max(DMscores, key=DMscores.get)
#        
#
#        
#        LC.add(node)
#        
#        DMscores.pop(node)
#         
#        #allazw to grafhma wste na pros8esw ton node me tis geitniaseis tou
##        Gdict[node] = G[node]
##        G = nx.Graph(Gdict)       
#        
#        previousNLC = NLC
#        
#        #update N(LC)
#        NLC = findNeighboorOfC(G, LC)
#        
#        #update M
#        M = findM(G, LC, Gdict)
#        
#        diff = NLC.difference(previousNLC)
#        
#        for u in diff:
#            LC.add(u)
#            DMscores[u] = findM(G, LC, Gdict) - M
#            LC.remove(u)              
#        
#        
##    print("LC=", LC)
#                
#       
#    with open('communities/'+str(myFile)+'_communities.csv', 'a') as out_file:
#              
#        writer = csv.writer(out_file, delimiter=';')
#        
#        if os.stat('communities/'+str(myFile)+'_communities.csv').st_size == 0:
#            writer.writerow(["Algorithm", "Node 1", "Node 2", "Multiplied Weight", "Seed node", "Community"])
#        
##        row = [alg]+[node1]+[node2]+[wName]+[s]+LC
##        row = [wName]+[s]+LC
#        row = LC
#        
#        writer.writerow(row)
#        
#        
#    with open('time/time.txt', 'a') as time_file:
#        time_file.write('newLCD execution time is:')
#        time_file.write(str(time.time() - start_time))
#        time_file.write('\n')
        
