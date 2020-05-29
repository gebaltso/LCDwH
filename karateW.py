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



G=nx.karate_club_graph()
    
    
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
s = 33

#pros8etw ton s sthn koinothta C
C.append(s) 

#orizw to distance
d = 2 
    
#pinakas me to sunolo geitonwn tou s se d-level
N=find_un_nei_s(s, d)

#print('pinakas N: ', N)

while len(N)>0:
    
    print("N = ", N)
    
    len_N = len(N)
    len_C = len(C)
      
    IS = 0
    ES = 0
    
    #print("paradeigma ", find_d_Ns(find_un_nei_s(16, d), find_un_nei_s(2, d)))

    #pinakas gia ta a8roismata twn d_Ns 
    sum_array = []

    for a in range(0, len_N):
                    
        sum_tmp = 0
                   
        for u in range(0, len_C):
                       
            sum_tmp += find_d_Ns(find_un_nei_s(N[a], d), find_un_nei_s(C[u], d))
                       
        sum_array.append(sum_tmp)
                    
                    #print("sum_array =", sum_array)
                    
    #index tou max stoixeiou            
    max_a = sum_array.index(max(sum_array))
        
       #print("max a= ", max_a)
        
    
    Na = find_un_nei_s(N[max_a], d)
    
    
    ###############################################
    
    adj_neig_a = find_un_nei_s(N[max_a], 1)
    
    nodes_for_IS = np.intersect1d(adj_neig_a, C)
    len_for_IS = len(nodes_for_IS)
    
    #gia upologismo IS
    for y in range(0,len_for_IS):
        
        #Nc_for = find_un_nei_s(C[y], d)
                
        IS = IS + find_d_Ns(find_un_nei_s(nodes_for_IS[y], d), Na)
      
    ###############################################   
       
    
    #gia upologismo IS
#    for y in range(0,len_C):
#        
#        Nc_for = find_un_nei_s(C[y], d)
#                
#        IS = IS + find_d_Ns(Nc_for, Na)
#        len_Nc_for = len(Nc)
#        for x in range(0,len_Nc_for):
#            index = np.argwhere(Na==-1)
#            Na = np.delete(Na, index)
#            
#            index = np.argwhere(Nc==-1)
#            Nc = np.delete(Nc, index)
        
    
    #vriskw tous komvous tou grafhmatos pou den anhkoun sthn C
    nodesC = np.setdiff1d(nodes, C)
    len_nodesC = len(nodesC)
    #print("NODESC: ", nodesC)
    
    nodes_for_ES = np.intersect1d(adj_neig_a, nodesC)
    len_for_ES = len(nodes_for_ES)
    
    
    for y in range(0,len_for_ES):
        ES = ES + find_d_Ns(find_un_nei_s(nodes_for_ES[y], d), Na)
    
    #gia upologismo ES
#    for y in range(0,len_nodesC):
#        
#        tmpC = find_un_nei_s(nodesC[y], d)
        #len_nodesC = len(nodesC)
    
#        #elegxw an 1 apo tous 2 pinakes nodesC kai Na einai megaluteros apo ton allon wste na tous kanw isou mikous
#        if len(Na) != len(nodesC):
#            if len(Na) > len(nodesC):
#                tmp = np.copy(Na)
#                for n,z in enumerate(tmp):
#                    if z not in nodesC:
#                        tmp[n] = -1
#                nodesC = tmp
#                
#            else:
#                tmp = np.copy(nodesC)
#                for n,z in enumerate(tmp):
#                    if z not in Na:
#                        tmp[n] = -1
#                Na = tmp

            
#        ES = ES + find_d_Ns(tmpC, Na)
#        len_Na_for = len(Na)
#        for x in range(0,len_Na_for):
#            index = np.argwhere(Na==-1)
#            Na = np.delete(Na, index)
#            
#            index = np.argwhere(nodesC==-1)
#            nodesC = np.delete(nodesC, index)
        
    
    #briskw to klasma IS/(ES-IS)
    fraction=IS/(ES-IS)
    
    nominator = 0
    denominator = 0
    
    if len_C == 1:
        CI = 0
    else:
        #oloi oi pi8anoi sunduasmoi metaksu 2 kombwn entos C
        lista_kombwn_C=list(itertools.combinations(C, 2))
        
        
        for y in range(0, len(lista_kombwn_C)):
            #print("stoixeio: ", (lista_kombwn_C[y])[0])
            nominator += find_d_Ns(find_un_nei_s((lista_kombwn_C[y])[0], d), (find_un_nei_s((lista_kombwn_C[y])[1], d)))
        
        
        for y in range(0, len(C)):
            #adj_neig_C = find_un_nei_s(C[y], d)
            
            #for x in range(0, len(adj_neig_C)):
            
                #denominator +=  find_d_Ns(find_un_nei_s(C[y], d), (find_un_nei_s(adj_neig_C[x], d)))
            for x in range(0, len(N)):    
                denominator +=  find_d_Ns(find_un_nei_s(C[y], d), (find_un_nei_s(N[x], d)))
        
        denominator += 1
        
        CI = nominator/denominator
        
    #an kalutereuei to fraction pros8etw ton komvo a sth C alliws oxi 
    if fraction > CI:
        C.append(N[max_a]) 

#        index = np.argwhere(N==N[max_a])
#        N = np.delete(N, N[max_a])
#        print("if")
        
        N = np.delete(N, max_a)
        
    else:
        
        N = np.delete(N, max_a)
        
#        index = np.argwhere(N==N[max_a])
#        N = np.delete(N, N[max_a])
#        print("else")
        
        ################################################
        
#        #pinakas geitonwn ka8e komvou ths C
#        Cc =[]
#        for y in range(0,len_C):
#            Cc.append(find_un_nei_s(C[y], d))
#            
#        
#        
#        for y in range(0,len_C):
#        
#            #dictionary me d_Ns ka8e komvou pou anhkei sthn C
#            for x in range(0, len(Cc)):
#                        
#               DCn[C[x]] = DCn[C[x]] + (find_d_Ns(C, Cc[x]))
#            
#         
#        print("D =", DCn)
#            
#        CIn = sum(DCn.values())
#         
#    
#        CId = sum(D.values())   
#               
#         
#        print('CIn= ', CIn)
#        print('CId= ', CId)
#           
#        CI = CIn/(1+CId)
#         
#    
#    #an kalutereuei to fraction pros8etw ton komvo a sth C alliws oxi 
#    if fraction > CI:
#        C.append(a) 
#
#        index = np.argwhere(N==a)
#        N = np.delete(N, index)
#
#        
#    else:
#        index = np.argwhere(N==a)
#        N = np.delete(N, index)
        

print('Community: ', C)


