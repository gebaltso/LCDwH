#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:02:33 2019

@author: georgiabaltsou
"""

# LTE

import networkx as nx
import math
import numpy as np 

# definition 1: (Neighborhood) Γ(u) = geitones  + u
def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    neighbors.append(u)
    return neighbors


# definition 2 :(Structural Similarity)network G~(V ,E,w),
# between two adjacent vertices u and v is:
def structuralSimilarity(G, u, v):


    n = np.intersect1d(findNeighboorOfu(G, u), findNeighboorOfu(G, v))

    nominator = len(n)

    denominator = math.sqrt(len(findNeighboorOfu(G, u))*len(findNeighboorOfu(G, v)))
    
    similarity = nominator/denominator


    if u in GTC:
        similarity *= 10 


    return similarity
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
    n.remove(a)
    n = list(set(n).difference(set(C)))

    for u in n:
        if (a, u) in G.edges():
            for i in similarityStore:
                soutCa += structuralSimilarity(G, a, u)

    return soutCa


# definition 5: Tunable Tightness Gain for the community C merging a neighbor vertex a
def tunableTightnessGain(C, G, N, a, factor,similarityStore):
    return ((SoutC(C, N, G, similarityStore) / SinC(C, G,similarityStore)) - ((factor*SoutCa(C, G, a,similarityStore) - SinCa(C, G, a,similarityStore)) / 2 * SinCa(C, G, a,similarityStore)))

# main program
G = nx.Graph()
#G = nx.read_edgelist("karate/karateUnw.csv", create_using=nx.Graph(), delimiter=";")
G = nx.read_edgelist("dblp/dblp.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("football/football.csv", create_using=nx.Graph(), delimiter=";")

# arxikopoihsh se 0 ths koinotitas C
C = []

# arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
N = []

# step 1
#s = 'supera'
#s = 'amputation'
#s = 'smoking'
#s = 'A_23_P251480' #ΝΒΝ gene
#s = 'A_23_P149050'
#s = '2'
s = '319507'
#s = '78' #Newman
#s = '281' #Sole


C.append(s)
N = findNeighboorOfu(G, s)
N.remove(s)
factor = 0.055

GTC = ['183323', '146590', '240098', '249900', '269383', '319507', '319508', '337203', '339699', '348984', '349177']

#print("neighors of "+vertex +": "+str(N))
while N:
#    print("N:" +str(len(N)))
    similarityStore =[]
    temp = []

    # step 2:Select a vertex a of N that possess the largest similarity with vertices in C
    for vertex in C:
        flag = 0
        for a in N:
            if (a, vertex) in G.edges():
                temp1 = structuralSimilarity(G, a, vertex)
                similarityStore.append([temp1, (vertex, a)])
                # print("vertex: " + vertex + " candidate: " + str(a) + " score: " + str(temp1))
                # print("temp: " + str(temp))

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
    # print("similarityStore: "+ str(similarityStore))

    # step 3 orise to factor gia mikres koinoththtes megalo factor -> 10
#    print("------------------------------------------------------------------")

    while temp:
        i = len(temp) - 1
        scoreofmax = temp[i][1]
        nameofmax = temp[i][0]
        # print("candicate: "+str(nameofmax))

        tunable = tunableTightnessGain(C, G, N, nameofmax, factor, similarityStore)
        # print("tunable:" + str(tunable))

        if tunable > 0:
            C.append(nameofmax)
            N = N + findNeighboorOfu(G, nameofmax)
            N = list(set(N).difference(set(C)))
            del similarityStore
            break
        else:
            N.remove(nameofmax)
            del temp[i]

#    print("C: ")
#    print("members of C:" +str(len(C)))
#    print(C)


print("C: ")
print(len(C))
print(C)
