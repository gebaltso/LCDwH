#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:59:15 2018

@author: georgiabaltsou
"""

import networkx as nx
import numpy as np 
import itertools
import time


def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors



#find all simlpe paths from source node to target node (A simple path is a path with no repeated nodes)
def findAllSimplePaths(G, s, t):
    paths = nx.all_shortest_paths(G, s, t)
#    print("Paths :", list(paths))
    return list(paths)

#find neighbors considering a highest T threshold of the sum of the weights of the coresponding edges
def findNeighbors(G, s, T):
    
    #pinakas me tous komvous pou einai geitones tou s kai plhroun to krithrio tou threshold T
    sumWeights = []
    
    for t in G.nodes(): #ekteleitai 16943
#    for t in sourceNodes:
        
        #briskw ta paths apo ton s pros ka8e allo komvo tou grafou
        paths = findAllSimplePaths(G, s, t)

        #print("Paths =", paths)

        #gia ka8e path 8a upologisw to a8roisma tou barous tou
        for x in paths:
            
            if(t not in sumWeights):
                sumN = 0 #a8roisma barous path
                for y in range(0, len(x)):
                    if x[y] != t:
                        #print("x= ", x, "y= ", y, "y+1 =", (y+1))
                        #sumN += weights[y][y+1]
                        weightFory = G.get_edge_data(x[y], x[y+1], default=0)
                        #print("weight = ", weightFory['weight'])
                        sumN += weightFory['weight']
#                        print("weight = ", sumN)
                        
                #efoson to a8roisma tou barous tou path einai <=T 8a krathsw ton komvo
                if sumN <= T:
                    sumWeights.append(t)
    #print("SumWeights= ", sumWeights)
    return sumWeights


#gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo s kai me mhkos paths d
def findPathsNoLC(G,s,d):  
    if d == 0:
        return [[s]]
    paths = []
    for neighbor in neighborsOfS:
        for path in findPathsNoLC(G,neighbor,d-1):
            if s not in path:
                paths.append([s]+path)
    return paths


#gia upologismo tou pinaka geitonwn tou komvou s se distance d
def find_un_nei_s(s, d, neighborsOfS):
    #pinakas adjacent geitonwn tou komvou s
    n_s = []
    N = []      
    for x in neighborsOfS:   
        n_s.append(x)
    

#    #an to d==1 tote oi geitones einai mono oi adjacent
    if d == 1:             
        N = n_s
    else:
#        for x in range(0,len(findPathsNoLC(neighborsOfS,s,d))):
#            N.append(findPathsNoLC(neighborsOfS,s,d)[x][d])
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

##############################################################################

##############################################################################


# main program


G = nx.Graph()
#G = nx.read_weighted_edgelist("myFile.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFilePearson.csv", create_using=nx.Graph(), delimiter=";")
G = nx.read_weighted_edgelist("karate.csv", create_using=nx.Graph(), delimiter=";")


#print("Edges: ", G.number_of_edges()) # 2671753
print("Nodes: ", G.number_of_nodes())  # 16943

# arxikopoihsh se 0 ths koinotitas C
C = []

# arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
N = []

# step 1
#s = 'A_23_P251480' #ΝΒΝ gene
#s = 'A_23_P149050'
s = '3'

start_time = time.time()

C.append(s)

#sunolo twn geitwnwn
neighborsOfS = findNeighboorOfu(G, s) 

#print("Number of neighbors = ", len(neighborsOfS))

#print("neighbors of "+ s +": "+ str(neighborsOfS))


#orizw to distance
d = 1 

#orizw to threshold
T = 2
    
#pinakas me to sunolo geitonwn tou s se d-level
N=find_un_nei_s(s, d, neighborsOfS)

#print("Neighbors = ", N)

#print("Paths: ", findAllSimplePaths(G, C[0], N[0]))

##gia oso uparxoun komvoi entos tou N
while len(N)>0:
#while len(C)<2:
   
   #print("N = ", N)
   
    len_N = len(N)
    len_C = len(C)
      
    IS = 0
    ES = 0
    
    #print("paradeigma ", find_d_Ns(find_un_nei_s(16, d), find_un_nei_s(2, d)))

    #pinakas gia ta a8roismata twn d_Ns 
    sum_array = []

    #gia na brw to a entos tou N
    for a in N:
        
        #find neighbors considering a highest T threshold of the sum of the weights of the coresponding edges 
        NA = findNeighbors(G, a, T)             
        sum_tmp = 0
               
        #gia ka8e u entos tou C
        for u in C:
                       
            sum_tmp += find_d_Ns(NA, findNeighbors(G, u, T))
                       
        sum_array.append(sum_tmp)
                    
        #print("sum_array =", sum_array)
                    
    #index tou max stoixeiou            
    max_a = sum_array.index(max(sum_array))
    #print("Max a = ", max_a)
     
    Nmax = findNeighbors(G, N[max_a], T)
        
    for y in range(0,len_C):
        if G.has_edge(C[y], N[max_a]):
            IS = IS + find_d_Ns(findNeighbors(G, C[y], T), Nmax)
                       
    #vriskw tous komvous tou grafhmatos pou den anhkoun sthn C
    nodes_not_C = np.setdiff1d(G.nodes, C)
    len_nodes_not_C = len(nodes_not_C)
#    print("C = ", C)
#    print("not C = ", nodes_not_C)
    for y in range(0,len_nodes_not_C):
        if G.has_edge(nodes_not_C[y], N[max_a]):
            ES = ES + find_d_Ns(findNeighbors(G, nodes_not_C[y], T), Nmax)  
  
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
#        print("lista komvwn = ", lista_kombwn_C)
           
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

print('Community: ', C)

#metraw me posous komvous entos C enwnetai o s prokeimenou na upologisw to dCs (ba8mos entos C tou komvou s)
dCs = 0
for i in C:
    if G.has_edge(s, i):
        dCs += 1


##pinakas me tous ba8mous twn komvwn tou G
degrees = []

#for i in range (0,len(sourceNodes)):
#    degrees.append(len(G.nodes[i]))
##    print("Degree of node ", sourceNodes[i], "is: ", len(nodes[i]))
#
##print(degrees)
#
#
###upologismos participation
#participation = (dCs/len(C))/(degrees[sourceNodes.index(s)]/len(nodes))
#
#print("max participation is ", len(G.nodes)/len(C))
#
#print("participation= ", participation)
      

