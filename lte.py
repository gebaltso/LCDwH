#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:12:48 2019

@author: georgiabaltsou

2011 Towards Online Multiresolution Community Detection in Large-Scale Networks
Jianbin Huang
"""


import networkx as nx
import numpy as np 
import csv
import os
import time


# definition 1: (Neighborhood) Γ(u) = geitones  + u
def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
#    neighbors.append(u)
    return neighbors


# definition 2 :(Structural Similarity)network G~(V ,E,w),
# between two adjacent vertices u and v is:
def structuralSimilarity(G, u, v):
    nominator = 0
    denominator1 = 0
    denominator2 = 0

    n = np.intersect1d(findNeighboorOfu(G, u), findNeighboorOfu(G, v))
    
    weightForuv = G.get_edge_data(u, v, default=0)
    tempUV = weightForuv['weight']
    nominatorWeight = 2*tempUV
        
    for x in n:
        #pass the calculation for self-loops
        if(x==u or x==v):
            continue
        
        weightForux = G.get_edge_data(u, x, default=0)
        temp1 = weightForux['weight']
        weightForvx = G.get_edge_data(v, x, default=0)
        temp2 =weightForvx['weight']
        nominator = nominator + temp1*temp2


    nominator = nominator + nominatorWeight


    set1 = findNeighboorOfu(G, u)

    for x in set1:
        if(x==u):
            continue
        weightForux = G.get_edge_data(u, x)
        temp1 = weightForux['weight']
        denominator1 = denominator1 + temp1**2

    denominator1 = 1 + denominator1

    set2 = findNeighboorOfu(G, v)

    for x in set2:
        if(x==v):
            continue
        weightForvx = G.get_edge_data(v, x)
        temp1 = weightForvx['weight']
        denominator2 = denominator2 + temp1**2

        
    denominator2 = 1 + denominator2
    
    
    if simFlag == 1:
        return nominator/denominator1*denominator2
    
    else:
    
        if u in s:
                    
            return 3*(nominator/denominator1*denominator2)
        
        else:
    
            return nominator/denominator1*denominator2
    
    
    
#    return nominator/(denominator1*denominator2)**(1/2)
    # 8eloume na mas gurisei pisw enas ari8mos me to structural gia 2 geitones


def SinC(C, G, similarityStore):
    sinC = 0
    for u in C:
        for v in C:
            if (u, v) in G.edges():
                sinC += structuralSimilarity(G, u, v)
    if sinC == 0:
        sinC = 1

    return sinC



def SoutC(C, N, G,similarityStore):
    soutC = 0
    for u in C:
        for v in N:
            if (u, v) in G.edges():
                soutC += structuralSimilarity(G, u, v)
    return soutC


def SinCa(C, G, a, similarityStore):
    sinCa = 0
    for v in C:
        if (v, a) in G.edges():
            sinCa +=  structuralSimilarity(G, v, a)

    if sinCa == 0:
        sinCa = 1
    return sinCa


def SoutCa(C, G, a, similarityStore):
    soutCa = 0
    n = findNeighboorOfu(G, a)
#    n.remove(a)
    n = list(set(n).difference(set(C)))

    for u in n:
        if (a, u) in G.edges():
            for i in similarityStore:
                soutCa += structuralSimilarity(G, a, u)

    return soutCa


# definition 5: Tunable Tightness Gain for the community C merging a neighbor vertex a
def tunableTightnessGain(C, G, N, a, factor,similarityStore):
    return ((SoutC(C, N, G, similarityStore) / SinC(C, G,similarityStore)) - ((factor*SoutCa(C, G, a,similarityStore) - SinCa(C, G, a,similarityStore)) / 2 * SinCa(C, G, a,similarityStore)))


def lte(file, seedsetFile, myFile, sim, G):

    # main program
    
    
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().split(" ")
    lenS = len(seeds)

    
    #keep as seed the 1st seed of seedFile
#    s = seeds[0]
    
    if sim == 1:
        alg = 'lte1'
    else:
        alg = 'lte3'
    
    start_time = time.time()

    node1 = file.split("<")[1].split("-")[0]
    
    node2 = file.split("-")[1].split(">")[0]
    
    
    wName = file.split(">")[1].split(".")[0]

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
        
    
#    C.append(s)
#    N = findNeighboorOfu(G, s)
#    N.remove(s)
    factor = 0.07
#    factor = 0.02
    
    while len(N) > 0 and len(C)<100:
        
#        print(len(C))
    
        #keep the structural similarities
        similarityStore =[]
        #keep couples of node and its structural similarity score
        temp = []
    
        # step 2:Select a vertex a of N that possess the largest similarity with vertices in C
        for vertex in C:
            flag = 0
            for a in N:
                if (a, vertex) in G.edges():
                    temp1 = structuralSimilarity(G, a, vertex)
                    similarityStore.append([temp1, (vertex, a)])
    
                    for k in temp:
                        scoreofmax = k[1]
                        nameofmax = k[0]
                        if nameofmax == a:
                            if scoreofmax < temp1:
                                temp.remove([a, scoreofmax])
                                temp.append([a, temp1])
                                flag = 1
                                break
                            elif scoreofmax >= temp1:
                                flag = 2
                                break
    
                    if flag == 0:
                        temp.append([a, temp1])
    
    
        temp = sorted(temp, key=lambda kv: kv[1])
    
        # step 3 orise to factor gia mikres koinoththtes megalo factor -> 10
    
    
        while temp:
            i = len(temp) - 1
            scoreofmax = temp[i][1]
            nameofmax = temp[i][0]
    
            tunable = tunableTightnessGain(C, G, N, nameofmax, factor, similarityStore)
    
            if tunable > 0:
                C.append(nameofmax)
                N = N + findNeighboorOfu(G, nameofmax)
                N = list(set(N).difference(set(C)))
                del similarityStore
                break
            else:
                N.remove(nameofmax)
                del temp[i]
    
    
#    with open('communities/lte'+str(simFlag)+'_communities'+str(myFile)+'.csv', 'a') as out_file:
#              
#        writer = csv.writer(out_file, delimiter=';')
#        
#        if os.stat('communities/lte'+str(simFlag)+'_communities'+str(myFile)+'.csv').st_size == 0:
#            writer.writerow(["Node 1", "Node 2", "Multiplied Weight", "Seed node", "Community"])
#        
#        row = [node1]+[node2]+[wName]+[s]+C
##        row = [wName]+[s]+C
#        
#        writer.writerow(row)
                
                
    with open('communities/'+str(myFile)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('communities/'+str(myFile)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm", "Node 1", "Node 2", "Multiplied Weight", "Seed node", "Community"])
        
        row = [alg]+[node1]+[node2]+[wName]+[s]+C
#        row = [wName]+[s]+C
        
        writer.writerow(row)
        
        
        
        
    with open('time/time.txt', 'a') as time_file:
        time_file.write('LTE execution time is:')
        time_file.write(str(time.time() - start_time))
        time_file.write('\n')

