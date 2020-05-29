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

G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
  
mydata = genfromtxt('/Users/georgiabaltsou/Desktop/Local_exp/distpropo_graph.csv', delimiter=';')   #anoigma csv arxeiou grafou

adjacency = mydata[1:,1:13] #metatropi pinaka se adjacency pinaka
#print(adjacency)

for i in range(len(adjacency)):     #filtrarisma akmwn wste na kratisw mono oses exouun baros apo 5.25 kai panw
    for j in range(len(adjacency)):
        if(adjacency[i][j] < 5.25):
            adjacency[i][j] = 0

A=np.matrix(adjacency)   #metatropi adjacency se numpy pinaka
G=nx.from_numpy_matrix(A)   #dimiourgia grafou


labeldict = {}          #onomata komvwn
for x in range(0,12):
    labeldict[x] = x
    
plt.axis('off')         #na mh sxediazontai oi aksones

nx.draw(G,labels=labeldict, with_labels = True)        #sxediasmos grafou

d=2    #orizw to distance
u=2    #orizw ton komvo
v=4    #orizw ton epomeno komvo

C = [] #arxikopoihsh se 0 ths koinotitas C
N = [] #arxikopoihsh se 0 tou sunolou twn geitwnwn

s = 0 #orizw ton komvo s ws ton arxiko seed node

C.append(s) #pros8etw ton s sthn koinothta C


n_u=[] 
n_v=[]      

for x in G.neighbors(u):   #evresi geitonwn tou komvou
    #print(x)
    n_u.append(x)
    
for x in G.neighbors(v):   #evresi geitonwn tou komvou
    #print(x)
    n_v.append(x)
    
#print(nx.shortest_path_length(G,source=5,target=6))     #mikos shortest path metaksu 2 kombwn

def findPathsNoLC(G,u,d):               #gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo u kai me mhkos paths n
    if d==0:
        return [[u]]
    paths = []
    for neighbor in G.neighbors(u):
        #print(neighbor)
        #print("______")
        for path in findPathsNoLC(G,neighbor,d-1):
            if u not in path:
                paths.append([u]+path)
    return paths


findPathsNoLC(G,u,d)
#print("______")
#findPathsNoLC(G,u,d-1)
##print("______")
#findPathsNoLC(G,u,d-2)

findPathsNoLC(G,v,d)
#print("______")
#findPathsNoLC(G,v,d-1)
##print("______")
#findPathsNoLC(G,v,d-2)

#print(findPathsNoLC(G,u,d))
#print(findPathsNoLC(G,u,d)[1][d])
#print(len(findPathsNoLC(G,u,d)))

neigh_u = []          #pinakas feitonwn tou u me distance d
neigh_v = []          #pinakas feitonwn tou v me distance d

if d==1:              #an to d==1 tote oi geitones einai mono oi adjacent
    neigh_u = n_u
    neigh_v = n_v
else:
    for x in range(0,len(findPathsNoLC(G,u,d))):
        neigh_u.append(findPathsNoLC(G,u,d)[x][d])
    
un_nei_u=np.unique(neigh_u)     #krataw tous geitones tou u xwris diplotupa
#print(un_nei_u)
    
un_nei_v=np.unique(neigh_v)     #krataw tous geitones tou v xwris diplotupa
#print(un_nei_v)

intersection_u_v=np.intersect1d(un_nei_u,un_nei_v)  #evresi tomis komvwn geitonwn u kai v
len_intersection_u_v=len(intersection_u_v)
print("________________")
print("τομή κοινών κόμβων:")
print(intersection_u_v)
#print(len_intersection_u_v)
print("________________")

union_u_v=np.union1d(un_nei_u,un_nei_v)             #evresi enwsis komvwn geitonwn u kai v
len_union_u_v=len(union_u_v)
print("ένωση κόμβων:")
print(union_u_v)
#print(len_union_u_v)

d_Ns=len_intersection_u_v/len_union_u_v
print("d_NS u kai v:")
print(d_Ns)