#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:11:17 2018

@author: georgiabaltsou
"""
import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np 
import itertools

def deg(s, adjacency):
    deg = 0
    neighbors = []
    
    for x in G.neighbors(s):
        neighbors.append(x)
        
    for x in neighbors:
        deg += adjacency[s][x] 
        print(adjacency[s][x] )
                
    return deg



G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
  
#anoigma csv arxeiou grafou
mydata = genfromtxt('/Users/georgiabaltsou/Desktop/Local_exp/thromvosis.csv', delimiter=';')   

#metatropi pinaka se adjacency pinaka
adjacency = mydata[1:,1:13] 


for i in range(len(adjacency)):     
    for j in range(len(adjacency)):
            adjacency[i][j] += 1

dt = []
dt = [('weight', float)]

#metatropi adjacency se numpy pinaka
A=np.matrix(adjacency, dtype=dt) 

#dimiourgia grafou  
G=nx.from_numpy_matrix(A)   

#ston pinaka weightTable krataw ta barh twn akmwn
weightTable = []
for i in range(0, len(adjacency)): 
    weightTable.append([])
    for j in range(0, len(adjacency)):
           weightTable[i].append(G[i][j]['weight'])

for i in range(0, len(adjacency)): 
#    weightTable.append([])
    for j in range(0, len(adjacency)):
           weightTable[i][j]=weightTable[i][j]-1


#print(weightTable)
#print(G[0][0]['weight'])

#print(weightTable[0][11])

for i in range(len(adjacency)):     
    for j in range(len(adjacency)):
            adjacency[i][j] -= 1

#filtrarisma akmwn wste na kratisw mono oses exouun baros apo 5.25 kai panw
for i in range(len(adjacency)):     
    for j in range(len(adjacency)):
        if(adjacency[i][j] < 5.25):
            adjacency[i][j] = 0

A=np.matrix(adjacency)
G=nx.from_numpy_matrix(A)


#onomata komvwn
labeldict = {}          
for x in range(0,12):
    labeldict[x] = x
    
#na mh sxediazontai oi aksones    
plt.axis('off')         

#sxediasmos grafou
nx.draw(G,labels=labeldict, with_labels = True) 

#oloi oi komvoi tou grafhmatos
nodes = nx.nodes(G)   


#pinakas me tous ba8mous twn komvwn tou G
degrees = []

for n in nodes:    
    degrees.append(G.degree(n))
    
#    print("Degree of node ", n, "is: ", G.degree(n))

#print(degrees)

#arxikopoihsh se 0 ths koinotitas C
C = [] 

#arxikopoihsh se 0 tou sunolou twn geitwnwn
S = [] 

#orizw ton komvo s ws ton arxiko seed node
s = 3

#pros8etw ton s sthn koinothta C
C.append(s)
C.append(11)
#C.append(6)

#pros8etw sto sunolo S tous geitones tou komvou s
for x in G.neighbors(s):
    S.append(x)

print("C =", C)



for e1,e2 in G.edges:
    if G.has_edge(e1,e2):
        G[e1][e2]['weight'] = adjacency[e1][e2]

print(G.edges(data=True))
#bb = 8
#att = nx.set_edge_attributes(G, 'weight', bb)
#
#example = nx.algorithms.cuts.conductance(G, C, V, weight='weight')
#print(example)

#swsto cut
cut = nx.cut_size(G,C, weight='weight')
print("cut =", cut)

#bazei epipleon mia fora to metaksu 3 kai 11 baros
vol = nx.algorithms.cuts.volume(G, C, weight='weight')
print("vol =", vol)


weightOfC = 0
start = 1
for i in C:
    for j in C[start:]:
        if G.has_edge(i,j):
            weightOfC += adjacency[i][j]
    start += 1 
                
print("Wc = ", weightOfC)

vol2 = vol - weightOfC
print("vol2 =", vol2)

conductance = cut/vol2
print("Conductance =", conductance)
