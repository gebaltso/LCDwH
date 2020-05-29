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

G=nx.karate_club_graph()
#print("Node Degree")
#for v in G:
#    print('%s %s' % (v,G.degree(v)))
    
    
labeldict = {}          
for x in range(0,34):
    labeldict[x] = x
    
nx.draw(G,labels=labeldict, with_labels = True) 

#oloi oi komvoi tou grafhmatos
nodes = nx.nodes(G) 
   

#arxikopoihsh se 0 ths koinotitas C
C = [] 

#arxikopoihsh se 0 tou sunolou twn geitwnwn
N = [] 

#orizw ton komvo s ws ton arxiko seed node
s = 11

#pros8etw ton s sthn koinothta C
C.append(s) 

A = nx.adjacency_matrix(G)


#print('Adjacent neighbors of node ',s, '= ', list(G.neighbors(s)))


#orizw to distance
d = 2 

#gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo s kai me mhkos paths d
#def findPathsNoLC(G,s,d):  
#    if d == 0:
#        return [[s]]
#    paths = []
#    for neighbor in G.neighbors(s):
#        for path in findPathsNoLC(G,neighbor,d-1):
#            if s not in path:
#                paths.append([s]+path)
#    return paths

#gia na krataw mono ta paths me length akrivws iso me d
def findPathsNoLC(G,s,d, excludeSet = None):
    if excludeSet == None:
        excludeSet = set([s])
    else:
        excludeSet.add(s)
    if d==0:
        return [[s]]
    paths = [[s]+path for neighbor in G.neighbors(s) if neighbor not in excludeSet for path in findPathsNoLC(G,neighbor,d-1,excludeSet)]
    excludeSet.remove(s)
#    print("paths =", paths)
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
#    un_nei_sN=np.unique(N)
#    un_nei_sIn=np.union1d(un_nei_sN,n_s)
#    un_nei_s=np.unique(un_nei_sIn)
    #print('Neighbors of node ',s, '= ', un_nei_s)
    
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