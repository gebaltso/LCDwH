#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:49:46 2018

@author: georgiabaltsou
"""

import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np 
import itertools

def CONDUCTANCE(G, C, adjacency):  
    
    #cut
    cut = nx.cut_size(G,C, weight='weight')
    #print("cut =", cut)
    
    #bazei epipleon mia fora to metaksu 3 kai 11 baros
    vol = nx.cuts.volume(G, C, weight='weight')
    #print("vol =", vol)
    
    
#    weightOfC = 0
#    start = 1
#    for i in C:
#        for j in C[start:]:
#            if G.has_edge(i,j):
#                weightOfC += adjacency[i][j]
#        start += 1 
#                    
#    
#    vol2 = vol - weightOfC
    
    
    conductance = cut/vol
    #print("Conductance =", conductance)

    return conductance


#upologismos tou deg ston paronomasth tou edge score
def deg(s, adjacency):
    deg = 0
    neighbors = []
    
    for x in G.neighbors(s):
        neighbors.append(x)
        
    for x in neighbors:
        deg += adjacency[s][x]   
                
    return deg


#upologismos tou edge score
def SCORE(s, S, C, adjacency):
    
    degs = G.degree(s)
     
    #geitones Nu
    N = []
    for n in G.neighbors(s):
       N.append(n)
    #print("neighbors of ",s, " =", N)
    
    #briskw thn tomh sthn opoia anhkei o komvos v
    V = []    
    intersection = np.intersect1d(C, N)
    for x in intersection:
        V.append(x)
    
    #print(V)
    
    #krataw ta edgeScores ka8e komvou pou anhkei sto V    
    #edgeScore = []
    
    sumOfEdgeScore = 0

    #neighbors of node v
    VN = []

    for v in V:
            
        #w(u,v)
        w = adjacency[s][v]
    
        for n in G.neighbors(v):
            VN.append(n)

        #print("S =", S)
        #print("VN =", VN)


        #X h tomh geitonwn u me geitones tou v
        X = []
        intersection2 = np.intersect1d(VN, N)
        #print("tomi = ", intersection2)
        for n in intersection2:
            X.append(n)

        sumOfMin = 0
        #minW = []
        for x in X:
            ux = adjacency[s][x]
            #print("ux =", ux)
            vx = adjacency[v][x]
            #print("vx =", vx)
            #minW.append(min(ux, vx))
            sumOfMin += (min(ux, vx))
           
        #print("minW =", minW)
            
        #briskw to a8roisma twn minW 
#        sumOfMin = 0
#        for x in minW:
#            #print("x =", x)
#            sumOfMin += x
            
        #print("sumOfMin =", sumOfMin)
        
        #o ari8mhths tou klasmatos tou edge score
        nominator = w + sumOfMin
        
        degu = deg(s, adjacency)
        #print("degu =", degu)
        degv = deg(v, adjacency)
        #print("degv =", degv)
        
        denominator = min(degu, degv)
        #print("denominator =", denominator)
        
        #edgeScore.append(nominator/denominator)
        #print("edgeScore = ", edgeScore)
        
        sumOfEdgeScore += (nominator/denominator)
    
#    sumOfEdgeScore = 0
#    for x in edgeScore:
#        sumOfEdgeScore += x
    
    #print("sumOfEdgeScore =", sumOfEdgeScore)
    
    score = ((1/degs)*(sumOfEdgeScore))
    
    return score


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
    
#bazw weights stis akmes tou grafou   
for e1,e2 in G.edges:
    if G.has_edge(e1,e2):
        G[e1][e2]['weight'] = adjacency[e1][e2]

#print(G.edges(data=True))

#arxikopoihsh se 0 ths koinotitas C
C = [] 

#arxikopoihsh se 0 tou sunolou twn geitwnwn
S = [] 

#orizw ton komvo s ws ton arxiko seed node
s = 0

#pros8etw ton s sthn koinothta C
C.append(s) 

#pros8etw sto sunolo S tous geitones tou komvou s
for x in G.neighbors(s):
    S.append(x)
print("Neighbors of node ",s, "=", S)

###############################################################################
while len(S)>0:

    
    #pinakas me ta scores twn stoixeiwn tou S
    score_array = []
    for u in S:
        score_array.append(SCORE(u, S, C, adjacency))
    
    
    #gia na sbhsw ta NaN
    score_array = np.nan_to_num(score_array)
        
    if (type(score_array) != list):
        score_array = score_array.tolist()
    
    print("score_array =", score_array)
    
    #briskw to maximum score apo ta scores twn S
    maxScore = np.amax(score_array)
    
    index = score_array.index(maxScore)
    
    #briskw ton komvo me to max score
    umax = S[index]
    #print("umax =", umax)
    
    #afairw apo to S ton komvo me to max score 

    if (type(S) != list):
        S = S.tolist()
    
    #print("umax =", umax)
    
    S.remove(umax)
     
    #print(S)
    
    #conductance of C
    conOfC = CONDUCTANCE(G, C, adjacency)
    
    CWithU = []
    for i in C:
        CWithU.append(i)
    CWithU.append(umax)
    
    #conductance of C with umax
    conOfCWithUmax = CONDUCTANCE(G, CWithU, adjacency)
    

    
    #an isxuei h sun8hkh pros8etw ton umax sthn C ki episis pros8etw sto S tous geitones tou umax pou den anhkoun sth C
    if (conOfCWithUmax<conOfC ):
        if (type(C) != list):
            C = C.tolist()
        C.append(umax)
        
        #briskw geitones tou umax
        neighborsOfUmax = []    
        for x in G.neighbors(umax):
            neighborsOfUmax.append(x) 
    
        #print(neighborsOfUmax)
        #print("newC =", C)
    
        #briskw tous geitones tou umax pou den anhkoun sthn C kai tous pros8etw sthn S
        diff = []
        diff = np.setdiff1d(neighborsOfUmax, C)
        for i in diff:
            S.append(i)
        
        #briskw ta stoixeia tou S xwris diplotupa
        S = np.unique(S)        
    
        #print("newS =", S)
        
    C = np.unique(C)
    
print("Community =", C)


