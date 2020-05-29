#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:27:02 2018

@author: georgiabaltsou
"""

# LTE

import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np 
import csv
import collections
import time



# definition 1: (Neighborhood) Γ(u) = geitones  + u
def neighborhoodOfu(G,u):

    neighbors = []
    for i in range(0, len(nodes[sourceNodes.index(u)])):
        neighbors.append(nodes[sourceNodes.index(u)][i])

    neighbors.append(u)
    #print("Length of neighbors= ", len(neighbors))
    return neighbors


# definition 2 :(Structural Similarity)network G~(V,E,w),
# between two adjacent vertices u and v is:
def structuralSimilarity(G, u, v):
    total = 0
    total1 = 0
    total2 = 0

    #n = intersection(neighborhoodOfu(G, u), neighborhoodOfu(G, v))
    n = np.intersect1d(neighborhoodOfu(G, u), neighborhoodOfu(G, v))
    #print("n = ", n)
    #print("Length of n= ", len(n))
#    n.remove(u)
#    n.remove(v)

    for x in n: 
        if(x==u or x==v):
            continue
        #print("x =", x)
        temp1 = weights[sourceNodes.index(u)][nodes[sourceNodes.index(u)].index(x)]        
        temp2 = weights[sourceNodes.index(v)][nodes[sourceNodes.index(v)].index(x)]
        total = total + temp1*temp2

    set1 = neighborhoodOfu(G, u)
    #set1.remove(u)

    for x in set1:
        if(x==u or x==v):
            continue
        temp1 = weights[sourceNodes.index(u)][nodes[sourceNodes.index(u)].index(x)]
        total1 = total1 + temp1**2

    total1 = total1**(1/2)

    set2 = neighborhoodOfu(G, v)
    #set2.remove(v)

    for x in set2:
        if(x==u or x==v):
            continue
        temp1 = weights[sourceNodes.index(v)][nodes[sourceNodes.index(v)].index(x)]
        total2 = total2 + temp1**2

    total2 = total2**(1/2)

    return total/total1*total2
    # 8eloume na mas gurisei pisw enas ari8mos me to structural gia 2 geitones

#internal similarity of community C
def SinC(C, G, similarityStore):
    Sin = 0
#    total = 0
#    for u in C:
#        for v in C:
#            if (u, v) in G.edges():
#                for i in similarityStore:
#                    if (u, v) or (v, u) == i[1]:
#                        total = 2 * i[0]
#                        break
#                    else:
#                        total = 2*structuralSimilarity(G, u, v)
#                        break
#    if total == 0:
#        total = 1
#    return total
    
    for u in C:
        for v in C:
            if (u, v) in G.edges():
                Sin = structuralSimilarity(G, u, v)
    
    return Sin
    

#external similarity of community C
def SoutC(C, N, G,similarityStore):
    Sout = 0
#    total = 0
#    for u in C:
#        for v in N:
#            if (u, v) in G.edges():
#                for i in similarityStore:
#                    if (u, v) or (v, u) == i[1]:
#                       total = total + i[0]
#                    else:
#                        total = total + structuralSimilarity(G, u, v)
#    return total
    
    for u in C:
        for v in N:
            if (u, v) in G.edges():
                Sout = structuralSimilarity(G, u, v)
    
    return Sout  
    


def SinCa(C, G, a, similarityStore):
    Sina = 0
#    total = 0
#    for u in C:
#        if (u, a) in G.edges():
#            for i in similarityStore:
#                if (u, a) or (a, u) == i[1]:
#                    total = total + i[0]
#                else:
#                    total = total + structuralSimilarity(G, u, a)
#
#    if total == 0:
#        total = 1
#    return total
    
    for v in C:
        if (v, a) in G.edges():
            Sina = structuralSimilarity(G, v, a)
    
    return Sina
    
    

def SoutCa(C, G, a, similarityStore):
    Souta = 0
#    total = 0
#    n = neighborhoodOfu(G, a)
#    n.remove(a)
#    n = list(set(n).difference(set(C)))
#
#    for u in n:
#        if (a, u) in G.edges():
#            for i in similarityStore:
#                if (u, a) or (a, u) == i[1]:
#                    total = total + i[0]
#                else:
#                    total = total + structuralSimilarity(G, u, a)
#
#    return total
    
    diff = []
    diff = np.setdiff1d(neighborhoodOfu(G,a), C)
    
    
    for u in diff:
        if (u, a) in G.edges():
            Souta = structuralSimilarity(G, u, a)
    
    return Souta
    
   
# intersection of lists - complexity O(n)
def intersection(list1, list2):
    temp = set(list2)
    list3 = [value for value in list1 if value in temp]
    return list3

# definition 5: Tunable Tightness Gain for the community C merging a neighbor vertex a
def tunableTightnessGain(C, G, N, a, factor,similarityStore):
#    return ((SoutC(C, N, G, similarityStore) / SinC(C, G,similarityStore)) - ((factor*SoutCa(C, G, a,similarityStore) - SinCa(C, G, a,similarityStore)) / 2 * SinCa(C, G, a,similarityStore)))
    return((SoutC(C, N, G, similarityStore) / SinC(C, G,similarityStore))-((factor*SoutCa(C, G, a,similarityStore) - SinCa(C, G, a,similarityStore)) / 2 * SinCa(C, G, a,similarityStore)))
    
## main program
#
#SourceFile = '/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv'
#TestFile = '/Users/georgiabaltsou/Desktop/test.csv'
#TestFile2 = '/Users/georgiabaltsou/Desktop/test 2.csv'
#
#
#G = nx.Graph()
#G = nx.read_weighted_edgelist(SourceFile, create_using=nx.Graph(), delimiter=";")
#
#
## print("Edges: ", G.number_of_edges()) # 2671753
#print("Nodes: ", G.number_of_nodes())
#
## arxikopoihsh se 0 ths koinotitas C
#C = []
#
## arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
#N = []
#
## step 1
#vertex = 'A_23_P251480'
#start_time = time.time()
#
#C.append(vertex)
#N = N + findNeighboorOfu(G, vertex)
#N.remove(vertex)
#factor = 0.005
#
#print("neighors of "+vertex +": "+str(N))
#while N:
#    print("N:" +str(len(N)))
#    similarityStore =[]
#    temp = []
#
#    # step 2:Select a vertex a of N that possess the largest similarity with vertices in C
#    for vertex in C:
#        flag = 0
#        for a in N:
#            if (a, vertex) in G.edges():
#                temp1 = structuralSimilarity(G, a, vertex)
#                similarityStore.append([temp1, (vertex, a)])
#                # print("vertex: " + vertex + " candidate: " + str(a) + " score: " + str(temp1))
#                # print("temp: " + str(temp))
#
#                for k in temp:
#                    scoreofmax = k[1]
#                    nameofmax = k[0]
#                    if nameofmax == a:
#                        if scoreofmax < temp1:
#                            temp.remove([a, scoreofmax])
#                            temp.append([a, temp1])
#                            flag = 1
#                            break
#                        elif scoreofmax >= temp1:
#                            flag = 2
#                            break
#
#                if flag == 0:
#                    temp.append([a, temp1])
#
#
#    temp = sorted(temp, key=lambda kv: kv[1])
#    # print("similarityStore: "+ str(similarityStore))
#
#    # step 3 orise to factor gia mikres koinoththtes megalo factor -> 10
#    print("------------------------------------------------------------------")
#
#    while temp:
#        i = len(temp) - 1
#        scoreofmax = temp[i][1]
#        nameofmax = temp[i][0]
#        # print("candicate: "+str(nameofmax))
#
#        tunable = tunableTightnessGain(C, G, N, nameofmax, factor, similarityStore)
#        # print("tunable:" + str(tunable))
#
#        if tunable > 0:
#            C.append(nameofmax)
#            N = N + findNeighboorOfu(G, nameofmax)
#            N = list(set(N).difference(set(C)))
#            del similarityStore
#            break
#        else:
#            N.remove(nameofmax)
#            del temp[i]
#
#    print("C: ")
#    print("members of C:" +str(len(C)))
#    print(C)
#
#
#print("C: ")
#print(len(C))
#print(C)
#print("--- %s seconds ---" % (time.time() - start_time))


###############################################################################
G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
  
#anoigma csv arxeiou grafou
#SourceFile = '/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv'
SourceFile = 'karate.csv'
TestFile = '/Users/georgiabaltsou/Desktop/test.csv'
TestFile2 = '/Users/georgiabaltsou/Desktop/test 2.csv'  

sourceNodes = []
nodes = []
weights = []

nodesTmp = []
weightsTmp = []

with open(SourceFile) as csvfile:
    dataFile = csv.reader(csvfile,skipinitialspace=True, delimiter = ',')
        
    for row in dataFile:
         sourceNodes.append(row[0])
         
         for y in range(len(row)):
             if(y%2 != 0):
                 nodesTmp.append(row[y])
             else:
                 if(y != 0):
                     weightsTmp.append(row[y])
         nodes.append(nodesTmp)
         nodesTmp = []
         weights.append(weightsTmp)
         weightsTmp = []
    
#gia na afairesw ta ' ' apo ta weights  
weights = [list(map(float, grp)) for grp in weights]


#print('nodes = ', nodes)
#print('weights = ', weights)
#print('Source Nodes = ', sourceNodes)


graph = collections.defaultdict(list)
edges = {}

for i in range (0,len(sourceNodes)):
    for j in range (0, len(nodes[i])):
            graph[sourceNodes[i]].append(nodes[i][j])
            edges[sourceNodes[i], nodes[i][j]] = weights[i][j]

#print("Edges with their weights: ", edges)
#print("Graph = ", dict(graph))

G = nx.Graph(graph)

#print(G['A_23_P123456']['A_23_P38584'])

for i in range(0, len(sourceNodes)):
    for j in range(0, len(nodes[i])):
        G[sourceNodes[i]][nodes[i][j]]['weight'] = weights[i][j]

#arxikopoihsh se 0 ths koinotitas C
C = [] 

#arxikopoihsh se 0 tou sunolou twn geitwnwn
S = [] 

#orizw ton komvo s ws ton arxiko seed node
#s = sourceNodes[7105] #BARCA-1
s = '34'
#s = sourceNodes[0] 
print("Node s = ", s)

#pros8etw ton s sthn koinothta C
C.append(s)


#print("Neighborhood =", neighborhoodOfu(G,s))

print("Structural Similarity = ", structuralSimilarity(G, s, s))









 