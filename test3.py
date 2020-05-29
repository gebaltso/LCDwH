#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:41:44 2018

@author: georgiabaltsou
"""

# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

from numpy import genfromtxt
import numpy as np 
import pandas as pd
import operator

G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
  
#anoigma csv arxeiou grafou
mydata = genfromtxt('/Users/georgiabaltsou/Desktop/Local_exp/thromvosis.csv', delimiter=';')   

#metatropi pinaka se adjacency pinaka
adjacency = mydata[1:,1:13] 
#print(adjacency)

#filtrarisma akmwn wste na kratisw mono oses exouun baros apo 5.25 kai panw
for i in range(len(adjacency)):     
    for j in range(len(adjacency)):
        if(adjacency[i][j] < 5.25):
            adjacency[i][j] = 0

#metatropi adjacency se numpy pinaka
A=np.matrix(adjacency) 

#dimiourgia grafou  
G=nx.from_numpy_matrix(A)   

#onomata komvwn
labeldict = {}          
for x in range(0,12):
    labeldict[x] = x
    
#na mh sxediazontai oi aksones    
plt.axis('off')         

#sxediasmos grafou
nx.draw(G,labels=labeldict, with_labels = True)        


#arxikopoihsh se 0 ths koinotitas C
C = [] 

#arxikopoihsh se 0 tou sunolou twn geitwnwn
N = [] 

#orizw ton komvo s ws ton arxiko seed node
s = 11

#pros8etw ton s sthn koinothta C
C.append(s)
C.append(6) 

#orizw to distance
d=2 

#gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo s kai me mhkos paths n
def findPathsNoLC(G,s,d):  
    if d==0:
        return [[s]]
    paths = []
    for neighbor in G.neighbors(s):
        #print(neighbor)
        #print("______")
        for path in findPathsNoLC(G,neighbor,d-1):
            if s not in path:
                paths.append([s]+path)
    return paths


def find_un_nei_s(s, d):
    #pinakas adjacent geitonwn tou komvou s
    n_s=[]      
    for x in G.neighbors(s):   
        #print(x)
        n_s.append(x)
    

    #an to d==1 tote oi geitones einai mono oi adjacent
    if d==1:             
        N = n_s
    else:
        for x in range(0,len(findPathsNoLC(G,s,d))):
            N.append(findPathsNoLC(G,s,d)[x][d])
    
    #krataw tous geitones tou s xwris diplotupa    
    un_nei_s=np.unique(N)
    return un_nei_s
    
    
def find_d_Ns(un_nei_u,un_nei_v):
    intersection_u_v=np.intersect1d(un_nei_u,un_nei_v)  #evresi tomis komvwn geitonwn u kai v
    len_intersection_u_v=len(intersection_u_v)
#    print("________________")
#    print("τομή κοινών κόμβων:")
#    print(intersection_u_v)
#    #print(len_intersection_u_v)
#    print("________________")
    
    union_u_v=np.union1d(un_nei_u,un_nei_v)             #evresi enwsis komvwn geitonwn u kai v
    len_union_u_v=len(union_u_v)
#    print("ένωση κόμβων:")
#    print(union_u_v)
    #print(len_union_u_v)
    
    d_Ns=len_intersection_u_v/len_union_u_v
    return d_Ns
    

N=find_un_nei_s(s, d)


#while N:
    
len_N=len(N)
len_C=len(C)

#a = np.empty(shape=(len_N,len_C))

#    #dimiourgia dictionary pou 8a exei keys ta onomata komvwn kai values tis d_Ns times
#    D1={}
#    for i in N:
#        D1[i] = 0 
  
D =[]
Dsum = []

for y in range(0,len(C)):
       
    Nc = find_un_nei_s(C[y], d)
    len_Nc=len(Nc)
   
    #pinakas me geitones(pinakas) ka8e komvou tou N dld NofN=[[4,6],[7,9]] klp
    NofN =[]
    for x in range(0,len_Nc):
        NofN.append(find_un_nei_s(Nc[x], d))
                 
        
    #koinoi komvoi metaksu N kai NofN
    common_nodes = [item for item in Nc if item in N]
    #print(common_nodes)

    
    #pinakas me ta d_Ns
    len_NofN=len(NofN)
    for x in range(0,len_NofN):
        D.append(find_d_Ns(Nc, NofN[x])) 
            
    Dsum.append(D)
    print(Dsum)

#    
#    #pinakas me ta d_Ns
#    len_NofN=len(NofN)
#    for x in range(0,len_NofN):
#        if(N[x] == Nc[x]):
#            D1[N[x]] = D1[N[x]] + (find_d_Ns(Nc, NofN[x])) #a8roisma d_ns gia ka8e komvo sto Nc
#    print(D1)   
#    
#    
##evresi komvou me max a8roisma d_Ns sto Nc
#a=max(D1.items(), key=operator.itemgetter(1))[0]    
#print("chosen node:", a)
    
