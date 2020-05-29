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
mydata = genfromtxt('/Users/georgiabaltsou/Desktop/Local_exp/distpropo_graph.csv', delimiter=';')   

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

#oloi oi komvoi tou grafhmatos
nodes = nx.nodes(G) 
      

#arxikopoihsh se 0 ths koinotitas C
C = [] 

#arxikopoihsh se 0 tou sunolou twn geitwnwn
N = [] 

#orizw ton komvo s ws ton arxiko seed node
s = 2

#pros8etw ton s sthn koinothta C
C.append(s)
#C.append(6) 


#orizw to distance
d = 1 

#gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo s kai me mhkos paths n
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
    un_nei_s=np.unique(N)
    return un_nei_s
    
    
def find_d_Ns(un_nei_u,un_nei_v):
    intersection_u_v=np.intersect1d(un_nei_u,un_nei_v)  #evresi tomis komvwn geitonwn u kai v
    len_intersection_u_v=len(intersection_u_v)
    
    union_u_v=np.union1d(un_nei_u,un_nei_v)             #evresi enwsis komvwn geitonwn u kai v
    len_union_u_v=len(union_u_v)
    
    d_Ns=len_intersection_u_v/len_union_u_v
    
    return d_Ns
    
#pinakas me to sunolo geitonwn tou s se d-level
N=find_un_nei_s(s, d)
print('pinakas N: ', N)
it = 0
while len(N)>0:
    
    len_N = len(N)
    len_C = len(C)
    
    #dimiourgia dictionary me keys ta onomata komvwn kai values tis d_Ns times
    D = {}
    for i in N:
      D[i] = 0 
     
    #dimiourgia dictionary me keys ta onomata komvwn ths C kai values tis d_Ns times tous
    DCn = {}
    for i in C:
      DCn[i] = 0 
      
      
    CIn = 0
    CId = 0
      
    IS = 0
    ES = 0
    
    for y in range(0,len_C):
           
        Nc = find_un_nei_s(C[y], d)
        len_Nc = len(Nc)
       
        #pinakas me geitones ka8e komvou tou N
        NofN =[]
        for x in range(0,len_Nc):
            NofN.append(find_un_nei_s(Nc[x], d))
    
        
        #elegxw an 1 apo tous 2 pinakes N kai Nc einai megaluteros apo ton allon wste na tous kanw isou mikous
        if len_N != len_Nc:
            if len_N > len_Nc:
                tmp = np.copy(N)
                for n,z in enumerate(tmp):
                    if z not in Nc:
                        tmp[n] = 0
                Nc = tmp
                
            else:
                tmp = np.copy(Nc)
                for n,z in enumerate(tmp):
                    if z not in N:
                        tmp[n] = 0
                N = tmp
                
        
        #pinakas me ta d_Ns
        len_NofN = len(NofN)
        for x in range(0,len_NofN):
            if(N[x] == Nc[x]):
                D[N[x]] = D[N[x]] + (find_d_Ns(Nc, NofN[x])) #a8roisma d_ns gia ka8e komvo sto Nc

        print(D)
    
        
    
    #evresi komvou me max a8roisma d_Ns sto Nc
    a=max(D.items(), key=operator.itemgetter(1))[0]    
    print("chosen node:", a)
    
    #pinakas me geitones tou komvou a se d-level
    Na = find_un_nei_s(a, d)
    len_Na = len(Na)
    
    #gia upologismo IS
    for y in range(0,len_C):
    
        #elegxw an 1 apo tous 2 pinakes Nc kai Na einai megaluteros apo ton allon wste na tous kanw isou mikous
        if len_Na != len_Nc:
            if len_Na > len_Nc:
                tmp = np.copy(Na)
                for n,z in enumerate(tmp):
                    if z not in Nc:
                        tmp[n] = 0
                Nc = tmp
                
            else:
                tmp = np.copy(Nc)
                for n,z in enumerate(tmp):
                    if z not in Na:
                        tmp[n] = 0
                Na = tmp
                
        IS = IS + find_d_Ns(Nc, Na)
        
    
    #vriskw tous komvous tou grafhmatos pou den anhkoun sthn C
    nodesC = np.setdiff1d(nodes, C)
    len_nodesC = len(nodesC)
    
    #gia upologismo ES
    for y in range(0,len_nodesC):
    
        #elegxw an 1 apo tous 2 pinakes nodesC kai Na einai megaluteros apo ton allon wste na tous kanw isou mikous
        if len_Na != len_nodesC:
            if len_Na > len_nodesC:
                tmp = np.copy(Na)
                for n,z in enumerate(tmp):
                    if z not in nodesC:
                        tmp[n] = 0
                nodesC = tmp
                
            else:
                tmp = np.copy(nodesC)
                for n,z in enumerate(tmp):
                    if z not in Na:
                        tmp[n] = 0
                Na = tmp
            
        ES = ES + find_d_Ns(nodesC, Na)
        
    
    #briskw to klasma IS/(ES-IS)
    fraction=IS/(ES-IS)
    
    if len_C == 1:
        CI = 0
    else:
        
        #pinakas geitonwn ka8e komvou ths C
        Cc =[]
        for y in range(0,len_C):
            Cc.append(find_un_nei_s(C[y], d))
            
        
        for y in range(0,len_C):
        
            #dictionary me d_Ns ka8e komvou pou anhkei sthn C
            for x in range(0, len(Cc)):
                        
               DCn[C[x]] = DCn[C[x]] + (find_d_Ns(C, Cc[x]))
            
            
        CIn = sum(DCn.values())
         
    
        CId = sum(D.values())   
               
         
        print(CIn)
        print(CId)
           
        CI = CIn/(1+CId)
         
    
    #an kalutereuei to fraction pros8etw ton komvo a sth C alliws oxi 
    if fraction > CI:
        C.append(a) 

        index = np.argwhere(N==a)
        N = np.delete(N, index)

#        N = N[N!=0]
#        N = N[N!=8]
        print(N)
        
    else:
        index = np.argwhere(N==a)
        N = np.delete(N, index)
        
#        N = N[N!=0]
#        N = N[N!=8]
#        it += 1
#        print("******",it)
        print(N)

print('Community: ', C)



