#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:15:24 2019

@author: georgiabaltsou

2011 Towards Online Multiresolution Community Detection in Large-Scale Networks
Jianbin Huang
"""


import networkx as nx
import numpy as np 
import csv
import os
import time
import math


# definition 1: (Neighborhood) Γ(u) = geitones  + u
def findNeighboorOfu(G,u):
    
    return set(G.neighbors(u))

def findGamma(G, u):
    
    Gamma = findNeighboorOfu(G,u)
    Gamma.add(u)
    
    return Gamma

#find the neighbors of community C
def findNeighboorOfC(G, C):
    neighbors = []
    neighborsOfC = []
    for j in C:
        for i in G.neighbors(j):
            neighbors.append(i)        
    neighborsOfC = np.unique(neighbors)
    
    return neighborsOfC
    
# definition 2 :(Structural Similarity)network G~(V ,E,w),
# between two adjacent vertices u and v is:
def structuralSimilarity(G, u, v, Gdict):
    nominator = 0
    denominator1 = 0
    denominator2 = 0

    n = findGamma(G, u).intersection(findGamma(G, v))
#    print("u=", u, "v=", v, "n=", n)

    # an h tomh tous einai keno sunolo, epestrepse 0
    if not n:
        return 0
    
#    weightForuv = G.get_edge_data(u, v, default=0)
#    tempUV = weightForuv['weight']
    
#    tempUV = int(Gdict[u][v])
#    nominatorWeight = 2*tempUV
        
    for x in n:      
        #pass the calculation for self-loops
        if(x==u or x==v):
            continue        
#        weightForux = G.get_edge_data(u, x, default=0)
#        temp1 = weightForux['weight']
        temp1 = int(Gdict[u][x])
#        weightForvx = G.get_edge_data(v, x, default=0)
#        temp2 =weightForvx['weight']
        temp2 = int(Gdict[v][x])
        nominator = nominator + temp1*temp2

    set1 = findGamma(G, u)

    for x in set1:

        if(x==u):
            continue
#        weightForux = G.get_edge_data(u, x)
#        temp1 = weightForux['weight']
        d1 = int(Gdict[u][x])
        denominator1 = denominator1 + d1**2
        
    set2 = findGamma(G, v)

    for x in set2:
        if(x==v):
            continue
#        weightForvx = G.get_edge_data(v, x)
#        temp1 = weightForvx['weight']
        d2 = int(Gdict[v][x])
        denominator2 = denominator2 + d2**2

    
    
    if simFlag == 1:
#        print("nom=", nominator)
#        print("d1=", denominator1)
#        print("d2=", denominator2)
        return nominator/math.sqrt(denominator1)*math.sqrt(denominator2)
    
    else:
    
        if u in s:
                    
            return 3*(nominator/math.sqrt(denominator1)*math.sqrt(denominator2))
        
        else:
    
            return nominator/math.sqrt(denominator1)*math.sqrt(denominator2)

    # 8eloume na mas gurisei pisw enas ari8mos me to structural gia 2 geitones


def SinC(C, G, similarityStore, Gdict):
    sinC = 0
#    print("C=", C)
    for u in C:
#        print("u=", u)
        for v in C:
#            print("v=", v)
            if (u, v) in G.edges(): 
#                print("there's edge")
                sinC += structuralSimilarity(G, u, v, Gdict)
    if sinC == 0:
#        sinC = 1
        print("SinC = 0")
    return sinC

def SoutC(C, G,similarityStore, Gdict):
    soutC = 0
    N = set(findNeighboorOfC(G, C))
    for u in C:
        for v in N:
            if (u, v) in G.edges():
                soutC += structuralSimilarity(G, u, v, Gdict)
    return soutC

def SinCa(C, G, a, similarityStore, Gdict):
    sinCa = 0
    for v in C:
        if (v, a) in G.edges():            
            sinCa +=  structuralSimilarity(G, v, a, Gdict)  
#    if sinCa == 0:
#        print("SinCa = 0")
#        sinCa = 1              
    return sinCa

def SoutCa(C, G, a, similarityStore, Gdict):
    soutCa = 0
    N = set(findNeighboorOfC(G, C))
    for u in N:
        if (a, u) in G.edges():
            soutCa += structuralSimilarity(G, a, u, Gdict)
    return soutCa

# definition 5: Tunable Tightness Gain for the community C merging a neighbor vertex a
def tunableTightnessGain(C, CWithA, G, a, factor,similarityStore, Gdict):
    return ((SoutC(C, G, similarityStore, Gdict) / SinC(C, G, similarityStore, Gdict)) - ((factor*SoutCa(C, G, a,similarityStore, Gdict) - SinCa(C, G, a,similarityStore, Gdict)) / 2 * SinCa(C, G, a,similarityStore, Gdict)))


def lte(seedsetFile, myFile, sim, G, Gdict, Gor, Graph):

    # main program
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().split(" ")
    lenS = len(seeds)
 
    if sim == 1:
        alg = 'lte1'
    else:
        alg = 'lte3'
    
    start_time = time.time()

#    node1 = file.split("<")[1].split("-")[0]   
#    node2 = file.split("-")[1].split(">")[0] 
#    wName = file.split(">")[1].split(".")[0]

    global simFlag    
    simFlag = sim
    
    # arxikopoihsh se 0 ths koinotitas C
    C = []
    
    # arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
    NInitial = []
    
    # arxikopoihsh ths seed list
    global s
    s = []

    for i in range(lenS):
        C.append(seeds[i])
        s.append(seeds[i])
        NInitial.append(findNeighboorOfu(G, seeds[i]))
    # Make list of lists one list    
    N = [val for sublist in NInitial for val in sublist]
    
#    factor = 0.27
    factor = 1
    
    similarityStore = {}
    
    for u in N:
        for vertex in C:
            if (u, vertex) in G.edges():
                similarityStore[u] = structuralSimilarity(G, u, vertex, Gdict)
      
          
    
    while len(similarityStore)>0 and len(C)<100:
        
      #step 2:Select a vertex a of N that possess the largest similarity with vertices in C 
      a  = max(similarityStore, key=similarityStore.get)

      similarityStore.pop(a) 
        
      CWithA = []
      for i in C:
          CWithA.append(i) 
      CWithA.append(a)    
      
      if len(C) == 1:
          tunable = 1
      else:
          tunable = tunableTightnessGain(C, CWithA, G, a, factor, similarityStore, Gdict)
  
      if tunable>0:
          C.append(a)
          
          #allazw to grafhma wste na pros8esw ton a me tis geitniaseis tou
          Gdict[a] = Graph[a]
          G = nx.Graph(Gdict)
          
          Na = findGamma(G, a)
      
          diffC = Na - set(C)

          diff = diffC - set(similarityStore.keys())

          for j in diff:
              for vertex in C:
                  if (j, vertex) in G.edges():
                      similarityStore[j] = structuralSimilarity(G, j, vertex, Gdict)
         
          print("C=", C)
        
    C = list(np.unique(C))
    
    with open('communities/'+str(myFile)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('communities/'+str(myFile)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm", "Node 1", "Node 2", "Multiplied Weight", "Seed node", "Community"])
        
#        row = [alg]+[node1]+[node2]+[wName]+[s]+C
#        row = [wName]+[s]+C
        row = C
        
        writer.writerow(row)   
        
    with open('time/time.txt', 'a') as time_file:
        time_file.write('LTE execution time is:')
        time_file.write(str(time.time() - start_time))
        time_file.write('\n')

