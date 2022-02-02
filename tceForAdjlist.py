#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:21:33 2019

@author: georgiabaltsou

2017-Michael Hamann,Eike Röhrs and Dorothea Wagner- 
Local Community Detection Based on Small Cliques
"""

import networkx as nx
import numpy as np 
import csv
import os
import time


def findNeighboorOfu(G,u):
    
    return set(G.neighbors(u))

def CONDUCTANCE(G, C, Gdict):  
    
    cut = nx.cut_size(G,C, weight='weight')    
    
    vol = nx.cuts.volume(G, C, weight='weight')
    
    if(vol==0): return 0
      
    conductance = cut/vol

    return conductance


#upologismos tou deg ston paronomasth tou edge score
def deg(u, N, G, Gdict):
    deg = 0
    
    
    for i in N:
        w = G.get_edge_data(u, i)
#        wei = float(Gdict[u][i])
        
        deg += w['weight']
#        deg += wei
          
    return deg


#calculation of edge score
def SCORE(u, C, G, Gdict):
        
    #neighbours Nu
    Nu = findNeighboorOfu(G,u)
    
    #find the interection to which node v belong   
    V = Nu.intersection(set(C))

    
    #keep the edgeScores of each node in V        
    sumOfEdgeScore = 0

    #weight between u and v
    wuv = 0

    for v in V:
                
        #w(u,v)       
        w = G.get_edge_data(u, v)
        wuv = w['weight']

        #neighbours of v
        Nv = findNeighboorOfu(G,v)
        
        #X is the intersection of node u with neighbours of node v
        X = Nv.intersection(Nu)


        sumOfMin = 0
        for x in X:
            w1 = G.get_edge_data(u, x)
            ux = w1['weight']
            w2 = G.get_edge_data(v, x)
            vx = w2['weight']
  
            sumOfMin += (min(ux, vx))
           
        
        #the nominator of edge score
        nominator = wuv + sumOfMin
        
        degu = deg(u, Nu, G, Gdict)
        degv = deg(v, Nv, G, Gdict)
        
        denominator = min(degu, degv)
        
        sumOfEdgeScore += (nominator/denominator)
    
    
    score = ((1/len(Nu))*(sumOfEdgeScore))
        
    return score

def tce(G, seedsetFile, file, Gdict, myFile, bdict, method,l):
    # main program
    
    start_time = time.time()
    
    alg = 'tce'
    
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().rstrip('\n').split(" ")
    lenS = len(seeds)
    
    
    # initialize community C to 0
    C = []  
    
    
    # initialize Neighoorhood outside C to 0
    SInitial = []

    
    # initialize seed list
    global s
    s = []
    
    for i in range(lenS):
        C.append(seeds[i])
        s.append(seeds[i])
        SInitial.append(findNeighboorOfu(G, seeds[i]))
      
    #conductance of C
    conOfC = CONDUCTANCE(G, C, Gdict)
    
    # Make list of lists one list    
    S = [val for sublist in SInitial for val in sublist]
 
    score_array = {}

    
    for u in S:
        score_array[u] = SCORE(u, C, G, Gdict)

     
    while len(score_array)>0  and len(C)<l:
    
        
        umax = max(score_array, key=score_array.get)

        score_array.pop(umax)
        
        CWithU = []
        for i in C:
            CWithU.append(i)
        CWithU.append(umax)
            
        #conductance of C with umax
        conOfCWithUmax = CONDUCTANCE(G, CWithU, Gdict)
        
        #if true add umax in C  and also add in S the neighbours of umax that do not belong in C
        if (conOfCWithUmax<conOfC):
            C.append(umax)
            conOfC = conOfCWithUmax
            
            
            #change the graph in order to add umax with it's adjacencies
            Gdict[umax] = bdict[umax]
                  
            #find neighbours of umax
            Numax = findNeighboorOfu(G, umax)

        
            #find neighbours of umax that do not belong in C, and add them in S
            diffC = Numax - set(C)
            diff = diffC - set(score_array.keys())


            for j in diff:
                score_array[j] = SCORE(j, C, G, Gdict)
   
        C = list(np.unique(C))
        
    print("TCE time: ", time.time() - start_time)
    
    with open('./communities/'+str(file)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('./communities/'+str(file)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm", "Seed node", "Method", "Community"])
        
        row = [alg] + ["\n".join(seeds)] + [method] + list(C)
        
        writer.writerow(row)


