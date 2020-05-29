#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:37:59 2018

@author: georgiabaltsou
"""

import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np 
import csv
import collections
import itertools
import json

def CONDUCTANCE(G, C, weights):  
    
    #cut
    cut = nx.cut_size(G,C, weight='weight')
    #print("cut =", cut)
    
    #bazei epipleon mia fora to metaksu 3 kai 11 baros
    vol = nx.cuts.volume(G, C, weight='weight')
    #print("vol =", vol)

    conductance = cut/vol
    #print("Conductance =", conductance)

    return conductance


#upologismos tou deg ston paronomasth tou edge score
def deg(u, weights):
    deg = 0
#    neighbors = []
    
#    for x in G.neighbors(u):
#        neighbors.append(x)
    
    for i in range(0, len(nodes[sourceNodes.index(u)])):
        #print(nodes[sourceNodes.index(u)][i])
#        neighbors.append(nodes[sourceNodes.index(u)][i])
        deg += weights[sourceNodes.index(u)][nodes[sourceNodes.index(u)].index(nodes[sourceNodes.index(u)][i])]
    #print("Neighbors =", neighbors)

#    for x in neighbors:
##    for x in range(0, len(neighbors)):
#        
#        deg += weights[sourceNodes.index(u)][nodes[sourceNodes.index(u)].index(x)]   
      
#    print("DEGpalio = ", deg)
          
    return deg


#upologismos tou edge score
def SCORE(u, S, C, weights):
    
#    degs = []
#    for i in range (0,len(sourceNodes)):
#        degs.append(len(nodes[i]))
     
    ###degs=[170, 170, ...., 170]
     
    #geitones Nu
#    N = []
#    for n in G.neighbors(u):
#       N.append(n)
#    #print("neighbors of ",u, " =", N)
    
    #geitones Nu
    N = []
    for i in range(0, len(nodes[sourceNodes.index(u)])):
        #print(nodes[sourceNodes.index(u)][i])
        N.append(nodes[sourceNodes.index(u)][i])
    #print("neighbors of ",u, " =", N)
    
    #briskw thn tomh sthn opoia anhkei o komvos v
#    V = []    
    V = np.intersect1d(C, N)

#    for x in intersection:
#        V.append(x)
    
#    print("Intersection of N and C =", V)
    
    #krataw ta edgeScores ka8e komvou pou anhkei sto V        
    sumOfEdgeScore = 0

    #neighbors of node v
    VN = []

    for v in V:
#    for v in range(0, len(V)):
                
        #w(u,v)       
        w = weights[sourceNodes.index(u)][nodes[sourceNodes.index(u)].index(v)]
        #print("Weight between u and v is= ", w)
#        for i in range(0, sourceNodes.index(u)):
#            print(weights[sourceNodes.index(u)][i])
        
        #print("item is= ", nodes[sourceNodes.index(u)][44])   #bgainei ontws to A_23_P149050     
        #print("u = ", u, "!!!", sourceNodes.index(u), "v = ", v)

        #geitones tou v
#        for n in G.neighbors(V[v]):
#            VN.append(n)
        
        #geitones tou v
        for i in range(0, len(nodes[sourceNodes.index(v)])):
            #print(nodes[sourceNodes.index(u)][i])
            VN.append(nodes[sourceNodes.index(v)][i])
        
        #print("S =", S)
        #print("VN =", VN)


        #X h tomh geitonwn u me geitones tou v
#        X = []
        X = np.intersect1d(VN, N)
        #print("tomi = ", intersection2)
#        for n in intersection2:
#            X.append(n)
        #print("X = ", X)
        #print(len(X)) #113

        sumOfMin = 0
        #minW = []
#        for x in X:
        for x in range(0, len(X)):
            ux = weights[sourceNodes.index(u)][x]
            #print("ux =", ux)
            vx = weights[sourceNodes.index(v)][x]
            #print("vx =", vx)
            #minW.append(min(ux, vx))
            sumOfMin += (min(ux, vx))
           
        #print("minW =", minW)
            
        #print("sumOfMin =", sumOfMin)
        
        #o ari8mhths tou klasmatos tou edge score
        nominator = w + sumOfMin
        
        degu = deg(u, weights)
        #print("degu =", degu)
        degv = deg(v, weights)
        #print("degv =", degv)
        
        denominator = min(degu, degv)
        #print("denominator =", denominator)
        
        #edgeScore.append(nominator/denominator)
#        print("edgeScore = ", edgeScore)
        
        sumOfEdgeScore += (nominator/denominator)
    
#    sumOfEdgeScore = 0
#    for x in edgeScore:
#        sumOfEdgeScore += x
    
    #print("sumOfEdgeScore =", sumOfEdgeScore)
    
    
#    score = ((1/degs[sourceNodes.index(u)])*(sumOfEdgeScore))
    
#    print("len =", len(nodes[sourceNodes.index(u)])) #ba8mos deg tou komvou u
    
    score = ((1/len(nodes[sourceNodes.index(u)]))*(sumOfEdgeScore))
    
    #print("Score =", score)
    
    return score


G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
  
#anoigma csv arxeiou grafou
SourceFile = '/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv'
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



#fo = open("file.txt", "w")
#
#for k, v in edges.items():
#    fo.write(str(k) + ' >>> '+ str(v) + '\n\n')
#
#fo.close()


#print("Edges with their weights: ", edges)
#print("Graph = ", dict(graph))

G = nx.Graph(graph)


#print(G['A_23_P123456']['A_23_P38584'])


for i in range(0, len(sourceNodes)):
    for j in range(0, len(nodes[i])):
        G[sourceNodes[i]][nodes[i][j]]['weight'] = weights[i][j]


#nx.write_edgelist(G, "test.edgelist.txt")
 

#print("Nodes of the graph: ", G.nodes())
#print("Edges of the graph: ", G.edges(data=True))

#file = open("testfile.txt","w") 
#for e in G.edges():
##    G[e[0]][e[1]]['weight'] = edges[e]
#
#    line = ' '.join(str(x) for x in e)
#    file.write(line + '\n') 
#
#file.close()
#print("Edges of the graph: ", G.edges(data=True))

#na mh sxediazontai oi aksones    
#plt.axis('off')         

#sxediasmos grafou
#nx.draw(G)



#pinakas me tous ba8mous twn komvwn tou G
#degrees = []
#
#for i in range (0,len(sourceNodes)):
#    degrees.append(len(nodes[i]))
    
#    print("Degree of node ", n, "is: ", G.degree(n))

#print(degrees)

#arxikopoihsh se 0 ths koinotitas C
C = [] 

#arxikopoihsh se 0 tou sunolou twn geitwnwn
S = [] 

#orizw ton komvo s ws ton arxiko seed node
#s = sourceNodes[7105] #HOXB9
s = sourceNodes[7016] #BARCA-1
print("Node s = ", s)

#pros8etw ton s sthn koinothta C
C.append(s) 

neighborsOfS = nodes[sourceNodes.index(s)]

#pros8etw sto sunolo S tous geitones tou komvou s
for x in neighborsOfS:
    S.append(x)
#print("Neighbors of node ",s, "=", S)
#print(len(S)) #170


###############################################################################
while len(S)>0:

    #pinakas me ta scores twn stoixeiwn tou S
    score_array = []
    for u in S:

        score_array.append(SCORE(u, S, C, weights))
       
    #gia na sbhsw ta NaN
#    score_array = np.nan_to_num(score_array)
#        
#    if (type(score_array) != list):
#        score_array = score_array.tolist()
        
    #print("score_array =", score_array)
        
    #briskw to maximum score apo ta scores twn S
    maxScore = np.amax(score_array)

    
    #print("maxScore =", maxScore)
    
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
    conOfC = CONDUCTANCE(G, C, weights)
    #print("Cond C =", conOfC)
    
    CWithU = []
    for i in C:
        CWithU.append(i)
    CWithU.append(umax)
    
    #conductance of C with umax
    conOfCWithUmax = CONDUCTANCE(G, CWithU, weights)
    #print("Cond with umax =", conOfCWithUmax)
    
    #an isxuei h sun8hkh pros8etw ton umax sthn C ki episis pros8etw sto S tous geitones tou umax pou den anhkoun sth C
    if (conOfCWithUmax<conOfC ):
        if (type(C) != list):
            C = C.tolist()
        C.append(umax)
        
        #briskw geitones tou umax
        neighborsOfUmax = []    
#        for x in G.neighbors(umax):
#            neighborsOfUmax.append(x) 
        for i in range(0, len(nodes[sourceNodes.index(umax)])):
            neighborsOfUmax.append(nodes[sourceNodes.index(umax)][i])
    
        #print(neighborsOfUmax)
        #print("newC =", C)
    
        #briskw tous geitones tou umax pou den anhkoun sthn C kai tous pros8etw sthn S
        diff = []
        diff = np.setdiff1d(neighborsOfUmax, C)
        #print("diff =" ,diff)
        if (type(S) != list):
            S = S.tolist()
        for i in diff:
            S.append(i)
        
        #briskw ta stoixeia tou S xwris diplotupa
        S = np.unique(S)        
    
        #print("newS =", S)
        
    C = np.unique(C)
    print("newC =", C)
    
print("Community =", C)


