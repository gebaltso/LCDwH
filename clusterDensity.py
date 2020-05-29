#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:29:32 2018

@author: georgiabaltsou
"""

import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np 
import itertools

#find all simlpe paths from source node to target node (A simple path is a path with no repeated nodes)
def findAllSimplePaths(G, s, t):
    paths = nx.all_shortest_paths(G, s, t)
    return list(paths)

#find neighbors considering a highest T threshold of the sum of the weights of the coresponding edges
def findNeighbors(G, s, T):
    
    sumWeights = []
    
    for t in range(0, len(G)):
        paths = findAllSimplePaths(G, s, t)
    
        for x in paths:
            
            if(t not in sumWeights):
                sumN = 0
                for y in range(0, len(x)):
                    if x[y] != t:
                        sumN += adjacency[y][y+1]
                if sumN <= T:
                    sumWeights.append(t)
                
    return sumWeights


#gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo s kai me mhkos paths d
def findPathsNoLC(G,s,d):  
    if d == 0:
        return [[s]]
    paths = []
    for neighbor in G.neighbors(s):
        for path in findPathsNoLC(G,neighbor,d-1):
            if s not in path:
                paths.append([s]+path)
    return paths


#gia upologismo tou pinaka geitonwn tou komvou s se distance d
def find_un_nei_s(s, d):
    #pinakas adjacent geitonwn tou komvou s
    n_s = []
    N = []      
    for x in G.neighbors(s):   
        n_s.append(x)
    

    #an to d==1 tote oi geitones einai mono oi adjacent
    if d == 1:             
        N = n_s
    else:
        for x in range(0,len(findPathsNoLC(G,s,d))):
            N.append(findPathsNoLC(G,s,d)[x][d])
    
    
    #krataw tous geitones tou s xwris diplotupa    
    un_nei_sN=np.unique(N)
    un_nei_sIn=np.union1d(un_nei_sN,n_s)
    un_nei_s=np.unique(un_nei_sIn)
    #print('Neighbors of node ',s, '= ', un_nei_s)
    return un_nei_s
    
    
def find_d_Ns(un_nei_u,un_nei_v):
    intersection_u_v=np.intersect1d(un_nei_u,un_nei_v)  #evresi tomis komvwn geitonwn u kai v
    len_intersection_u_v=len(intersection_u_v)
    
    union_u_v=np.union1d(un_nei_u,un_nei_v)             #evresi enwsis komvwn geitonwn u kai v
    len_union_u_v=len(union_u_v)
    
    d_Ns=len_intersection_u_v/len_union_u_v
    
    return d_Ns

def weightedPmetric(C, adjacency, nodes):
    #sum of weights of the nodes that are in community C         
    weightOfC = 0
    start = 1
    for i in C:
        for j in C[start:]:
            if G.has_edge(i,j):
                weightOfC += adjacency[i][j]
    
        start += 1    

    
    sumOfWeights = 0
    for i in range(0, len(adjacency)):
        for j in range(0, len(adjacency)):
            sumOfWeights += adjacency[i][j]
    
    maxweightedParticipation = (len(nodes)/len(C))
    
    version2maxweightedParticipation = (sumOfWeights/weightOfC)
    
    print("Max weighted participation of node ", i, "= ", maxweightedParticipation)
    print("Version 2 of max weighted participation of node ", i, "= ", version2maxweightedParticipation)

    

    #upologismos participation gia ka8e komvo entos C   
    weightInCs = 0  
    weightS = 0
      
    for i in C:
        #metraw me posous komvous entos C enwnetai o s prokeimenou na upologisw to dCs (ba8mos entos C tou komvou s)
    
        weightS = 0
    
        for j in range(0,len(adjacency)):
            weightS += adjacency[i][j]
    
        weightInCs = 0
    
        
        for x in C:
            if G.has_edge(i, x):
                weightInCs += adjacency[i][x] 
    
        weightedParticipation = ((weightInCs/len(C))/(weightS/len(nodes)))
        version2weightedParticipation = ((weightInCs/weightOfC)/(weightS/sumOfWeights))
    
        print("weighted participation of node ", i, "= ", weightedParticipation)
        print("Version 2 of weighted participation of node ", i, "= ", version2weightedParticipation)
 
    
    
#upologismos ths poiothtas koinothtas ws to sunoliko baros koinothtas pros to sunoliko baros twn kombwn ths koinothtas pros olous omws tous kombous, oxi mono autous entos C  
def communityQuality(C, adjacency, nodes):
    weightOfC = 0
    start = 1
    for i in C:
        for j in C[start:]:
            if G.has_edge(i,j):
                weightOfC += adjacency[i][j]
        start += 1 
                
    print("Wc = ", weightOfC)
    
    sumOfWeights = 0
    
    for i in C:
       for j in G:
           if G.has_edge(i, j):
               sumOfWeights += adjacency[i][j]
               
    #afairw ta barh metaksy twn kombwn ths koinothtas giati apoteloun diplotypa mias kai upologizontai apo ka8e komvo
    sumOfWeights -= weightOfC
           
    print("Sc = ", sumOfWeights)
    
    CommunityQuality = weightOfC/sumOfWeights
    
    print("Community Quality = ", CommunityQuality)
    

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
N = [] 

#orizw ton komvo s ws ton arxiko seed node
s = 0

#pros8etw ton s sthn koinothta C
C.append(s) 

#orizw to distance
d = 2 

#orizw to threshold
T = 12
    
#pinakas me to sunolo geitonwn tou s se d-level
#N=find_un_nei_s(s, d)

N = findNeighbors(G, s, T)

print("Neighbors = ", N)

#print('pinakas N: ', N)

#gia oso uparxoun komvoi entos tou N
while len(N)>0:
    
#    print("N = ", N)
    
    len_N = len(N)
    len_C = len(C)
      
    IS = 0
    ES = 0
    
    #print("paradeigma ", find_d_Ns(find_un_nei_s(16, d), find_un_nei_s(2, d)))

    #pinakas gia ta a8roismata twn d_Ns 
    sum_array = []

    #gia na brw to a entos tou N
    for a in range(0, len_N):
                    
        sum_tmp = 0
               
        #gia ka8e u entos tou C
        for u in range(0, len_C):
                       
            sum_tmp += find_d_Ns(findNeighbors(G, N[a], T), findNeighbors(G, C[u], T))
                       
        sum_array.append(sum_tmp)
                    
                    #print("sum_array =", sum_array)
                    
    #index tou max stoixeiou            
    max_a = sum_array.index(max(sum_array))
             
    for y in range(0,len_C):
        if G.has_edge(C[y], N[max_a]):
            IS = IS + find_d_Ns(findNeighbors(G, C[y], T), findNeighbors(G, N[max_a], T))
                       
    #vriskw tous komvous tou grafhmatos pou den anhkoun sthn C
    nodes_not_C = np.setdiff1d(nodes, C)
    len_nodes_not_C = len(nodes_not_C)
#    print("C = ", C)
#    print("not C = ", nodes_not_C)
    for y in range(0,len_nodes_not_C):
        if G.has_edge(nodes_not_C[y], N[max_a]):
            ES = ES + find_d_Ns(findNeighbors(G, nodes_not_C[y], T), findNeighbors(G, N[max_a], T))  
  
#    print("IS = ", IS)
#    print("ES = ", ES)
    #briskw to klasma IS/(ES-IS)
    fraction=IS/(ES-IS)
    
#    print("fraction = ", fraction)
       
    nominator = 0
    denominator = 0
    
    if len_C == 1:
        CI = 0
    else:
        #oloi oi pi8anoi sunduasmoi metaksu 2 kombwn entos C
        lista_kombwn_C=list(itertools.combinations(C, 2))
        #print("lista komvwn = ", lista_kombwn_C)
           
        for y in range(0, len(lista_kombwn_C)):
            #print("stoixeio: ", (lista_kombwn_C[y])[0])
            if G.has_edge((lista_kombwn_C[y])[0], (lista_kombwn_C[y])[1]):
                nominator += find_d_Ns(findNeighbors(G, (lista_kombwn_C[y])[0], T), (findNeighbors(G, (lista_kombwn_C[y])[1], T)))
        
        
        for y in range(0, len(C)):       
            for x in range(0, len(N)): 
                if G.has_edge((C[y]), (N[x])):
                    denominator +=  find_d_Ns(findNeighbors(G, C[y], T), (findNeighbors(G, N[x], T)))
        
        denominator += 1

        CI = nominator/denominator
        
#        print("nominator = ", nominator)
#        print("denominator = ", denominator)
#        print("CI =", CI)
        
    #an kalutereuei to fraction pros8etw ton komvo a sth C alliws oxi 
    if fraction > CI:
        C.append(N[max_a]) 
        N = np.delete(N, max_a)
        
    else:
        N = np.delete(N, max_a)              

print('Community: ', C)


weightedPmetric(C, adjacency, nodes)

communityQuality(C, adjacency, nodes)
      
