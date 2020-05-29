#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:28:53 2018

@author: georgiabaltsou
"""

import networkx as nx
import numpy as np 
import itertools

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


#gia upologismo tou pinaka geitonwn tou komvou s se distance d kai mikroterh
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

#
#def findPaths(G,u,n):
#    if n==0:
#        return [[u]]
#    paths = [[u]+path for neighbor in G.neighbors(u) for path in findPaths(G,neighbor,n-1) if u not in path]
#
#    return paths
#
#def finalPaths(paths):
#    finalNodes = []
#    for node in range(len(paths)):
#        finalNodes.append(paths[node][d])
#    return finalNodes

#briskw tous geitones me shortest path ston s akrivws iso me d
def R(G, s, d):
    R_neighbors = []
    source_path_lengths = nx.single_source_dijkstra_path_length(G, s)
    for (v, l) in source_path_lengths.items():
       if l == d:
           R_neighbors.append(v)
    return R_neighbors


def find_dNs_Weighted(u, v, d):
    Nu = find_un_nei_s(u, d)
    Nv = find_un_nei_s(v, d)

    inter = np.intersect1d(Nu, Nv)
    
    print("inter =", inter)
    
    sumx = 0
    
    for x in inter:
        
        sumj = 0
        for j in range(1, d+1):
            Iu = 0
            Iv = 0
            Ru = R(G, u, j)
            Rv = R(G, v, j)
            
            print("Ru =", Ru)
            print("Rv =", Rv)
            
            if x in Ru:
                Iu = 1
                print("IN Ru", x)
            if x in Rv:
                Iv = 1
                print("IN Rv", x)
            sumj += ((1/j)*(Iu + Iv))
        sumx += sumj
     
        
    sumj_d = 0
    
    for j in range(1, d+1):
        Ru = R(G, u, j)
        Rv = R(G, v, j)
        
        print("Ru2 =", Ru)
        print("Rv2 =", Rv)
        
        sumj_d += ((1/j)*(len(Ru)+len(Rv)))

    print("sumx =",sumx)
    print("sumj_d =",sumj_d)
    
    return (sumx/sumj_d)

#dimiourgia tou grafou G apo to uparxon dataset gia to karate club
G=nx.karate_club_graph()
    
#bazw etiketes onomatwn stous komvous   
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
s = 29

#pros8etw ton s sthn koinothta C
C.append(s) 

#orizw to distance
d = 2 
    
#pinakas me to sunolo geitonwn tou s se d-level
N=find_un_nei_s(s, d)

#print('pinakas N: ', N)
  
#paths = findPaths(G, s, d)
#print("paths se apostash d", paths)
#print("geitones se apostash d", np.unique(finalPaths(paths)))

#briskw tous geitones me shortest path ston s akrivws iso me d
#print("Neighbors with shortest path to node ", s, "exactly equal to distance ", d,": ", R(G, s, d))
#
#print(find_dNs_Weighted(16, 2, 2))

#gia oso uparxoun komvoi entos tou N
while len(N)>0:
    
    print("N = ", N)
    
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
                       
            #sum_tmp += find_dNs_Weighted(find_un_nei_s(N[a], d), find_un_nei_s(C[u], d), d)
            sum_tmp += find_dNs_Weighted(a, u, d)
                       
        sum_array.append(sum_tmp)
                    
                    #print("sum_array =", sum_array)
                    
    #index tou max stoixeiou            
    max_a = sum_array.index(max(sum_array))
             
    for y in range(0,len_C):
        if G.has_edge(C[y], N[max_a]):
            #IS = IS + find_dNs_Weighted(find_un_nei_s(C[y], d), find_un_nei_s(N[max_a], d), d)
            IS = IS + find_dNs_Weighted(y, max_a, d)
                       
    #vriskw tous komvous tou grafhmatos pou den anhkoun sthn C
    nodes_not_C = np.setdiff1d(nodes, C)
    len_nodes_not_C = len(nodes_not_C)
#    print("C = ", C)
#    print("not C = ", nodes_not_C)
    for y in range(0,len_nodes_not_C):
        if G.has_edge(nodes_not_C[y], N[max_a]):
            #ES = ES + find_dNs_Weighted(find_un_nei_s(nodes_not_C[y], d), find_un_nei_s(N[max_a], d), d)
            ES = ES + find_dNs_Weighted(y, max_a, d) 
  
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
                #nominator += find_dNs_Weighted(find_un_nei_s((lista_kombwn_C[y])[0], d), (find_un_nei_s((lista_kombwn_C[y])[1], d)), d)
                nominator += find_dNs_Weighted((lista_kombwn_C[y])[0], (lista_kombwn_C[y])[1], d)
        
        
        for y in range(0, len(C)):       
            for x in range(0, len(N)): 
                if G.has_edge((C[y]), (N[x])):
                    #denominator +=  find_dNs_Weighted(find_un_nei_s(C[y], d), (find_un_nei_s(N[x], d)), d)
                    denominator +=  find_dNs_Weighted(y, x, d)
        
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
