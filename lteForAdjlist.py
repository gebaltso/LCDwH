#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:53:49 2019

@author: georgiabaltsou
"""

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


prN = {}

# find the neighbors of a node u 
def findNeighboorOfu(Gdict,u):

    return set((Gdict[u].keys()))

# find the neighbors of a node u plus the node u (Γ(u))
def findGamma(Gdict, u):
    
    Gamma = findNeighboorOfu(Gdict,u)
    Gamma.add(u)
    
    return Gamma

#find the neighbors of a community C
def findNeighboorOfC(Gdict, C):

    neighborsOfC = set()
    for j in C:       
        neighborsOfC.update(findNeighboorOfu(Gdict,j))        
    
    return neighborsOfC
    
# definition 2 :(Structural Similarity) of a network G~(V ,E,w),
# between two adjacent vertices u and v is:
def structuralSimilarity(u, v, Gdict):
    nominator = 0
    denominator1 = 0
    denominator2 = 0

    n = findGamma(Gdict, u).intersection(findGamma(Gdict, v))
    

    # if the above intersection=0, return 0
    if not n:
        return 0
        
    for x in n:  
        #pass the calculation for self-loops
        if(x==u or x==v):
            continue        
        temp1 = float(Gdict[u][x]) #weight of edge (u,x)
        temp2 = float(Gdict[v][x]) #weight of edge (v,x)

        nominator = nominator + temp1*temp2
        

    set1 = findGamma(Gdict, u)
    for x in set1:
        if(x==u):
            continue
        d1 = float(Gdict[u][x])
        denominator1 = denominator1 + d1**2
        
    set2 = findGamma(Gdict, v)
    for x in set2:
        if(x==v):
            continue
        d2 = float(Gdict[v][x])
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


def SinC(C, similarityStore, Gdict):
    sinC = 0
    for u in C:
        for v in C: 
            if (u in Gdict and v in Gdict[u]):
                sinC += structuralSimilarity(u, v, Gdict)
#    if sinC == 0: 
#        print("SinC = 0")
    return sinC

def SoutC(C, similarityStore, Gdict):
    soutC = 0
    N = findNeighboorOfC(Gdict, C)
    for u in C:
        for v in N:
            if (u in Gdict and v in Gdict[u]):
                soutC += structuralSimilarity(u, v, Gdict)
    return soutC

def SinCa(C, a, similarityStore, Gdict):
    sinCa = 0
    for v in C:   
        if (v in Gdict and a in Gdict[v]):         
            sinCa +=  structuralSimilarity(v, a, Gdict)  
#    if sinCa == 0:
#        print("SinCa = 0") 
             
    return sinCa

def SoutCa(C, a, similarityStore, Gdict):
    soutCa = 0
#    N = findNeighboorOfC(Gdict, C)
    N = (findNeighboorOfu(Gdict,a))-C   
    for u in N:
        if (u in Gdict and a in Gdict[u]):
            soutCa += structuralSimilarity(a, u, Gdict)
    return soutCa

# definition 5: Tunable Tightness Gain for the community C merging a neighbor vertex a
def tunableTightnessGain(C, a, factor,similarityStore, Gdict):
    if SinC(C, similarityStore, Gdict) ==0 or SinCa(C, a, similarityStore, Gdict) == 0:
        gain = 0
    else:
        gain = ((SoutC(C, similarityStore, Gdict) / SinC(C, similarityStore, Gdict)) - ((factor*SoutCa(C, a, similarityStore, Gdict) - SinCa(C, a, similarityStore, Gdict)) / 2 * SinCa(C, a, similarityStore, Gdict)))
    
    return gain


def lte(seedsetFile, myFile, sim, G, Gdict, method,l):

    
    
    
    # main program
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().rstrip('\n').split(" ")
    lenS = len(seeds)
 
    # sim is used for tripling the similarity score(sim=3) or not (sim=1)
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
    C = set()
    
    # arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
    NInitial = []
    
    # arxikopoihsh ths seed list
    global s
    s = []

    for i in range(lenS):
        C.add(seeds[i])
        s.append(seeds[i])
        NInitial.append(findNeighboorOfu(Gdict,seeds[i]))
       
    # Make list of lists one list    
    N = set([val for sublist in NInitial for val in sublist])
    
    # the bigger the factor the smaller the communities (factor = the constant a of tunable tightness gain)
    factor = 10
    
    # dict for storing similarities
    similarityStore = {}
     
    #add to similarities dict the similaries between nodes in N and nodes in C
    for u in N:
        for vertex in C:
            if (u in Gdict and vertex in Gdict[u]):
                similarityStore[(u,vertex)] = structuralSimilarity(u, vertex, Gdict)

    while len(similarityStore)>0 and len(C)<l:
        
      #step 2:Select a vertex a of N that possess the largest similarity with vertices in C 
      am  = max(similarityStore, key=similarityStore.get)     
      a = am[0]

      # remove from similarity dict the node in order to avoid selecting the same node more than once
      similarityStore.pop(am)    
        
      # keep a temporary community (CWithA) which is C + a
      CWithA = set()
      for i in C:
          CWithA.add(i) 
      CWithA.add(a) 
      
      # if C has only the seed node don't calculate tunable gain until a new node is added because similarity will be calculated between a node and itself (u=v=node)
      if len(C) == 1:
          tunable = 1
      else:
          tunable = tunableTightnessGain(CWithA, a, factor, similarityStore, Gdict)
  
    
      # if tunable is >0 for CWithA, then add node a to C
      if tunable>0:
          C.add(a)
          
          #allazw to grafhma wste na pros8esw ton a me tis geitniaseis tou
#          Gdict[a] = Graph[a]
#          G = nx.Graph(Gdict)

          # step 3: find new N as N U Γ(a)-C
          Na = findGamma(Gdict, a)      
          diffC = Na - C

          # update the similarity scores only for the new nodes added
          for j in diffC:   
              for vertex in C:
                  if (j in Gdict and vertex in Gdict[j]):    
                      if ((j, vertex) not in similarityStore):
                          similarityStore[(j, vertex)] = structuralSimilarity(j, vertex, Gdict)
         
#          print("C=", C)
        
#    C = list(np.unique(C))
    
    with open('./communities/'+str(myFile)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('./communities/'+str(myFile)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm", "Seed node", "Method", "Community"])
        
#        row = [alg]+[node1]+[node2]+[wName]+[s]+C
#        row = [wName]+[s]+C
        row = [alg] + ["\n".join(seeds)] + [method] + list(C)
        
        writer.writerow(row)   
        
#    with open('time/time.txt', 'a') as time_file:
#        time_file.write('LTE execution time is:')
#        time_file.write(str(time.time() - start_time))
#        time_file.write('\n')

