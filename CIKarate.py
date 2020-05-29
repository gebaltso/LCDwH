#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:48:46 2018

@author: georgiabaltsou
"""

import networkx as nx
import numpy as np 
import itertools

#find all simlpe paths from source node to target node (A simple path is a path with no repeated nodes)
def findAllSimplePaths(G, s, t):
    paths = nx.all_shortest_paths(G, s, t)
#    paths = nx.all_simple_paths(G, source=s, target=t, cutoff=2)
#    print("Paths :", list(paths))
    return list(paths)

#def findNeighbors(G, s, d):

#find neighbors considering a highest T threshold of the sum of the weights of the coresponding edges
def findNeighbors1(G, s, T):
    
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
    print("SumWeights= ", sumWeights)
    return sumWeights

def findNeighboorOfu(G,u):
    neighbors = []
        
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors


#gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo s kai me mhkos paths d
#def findPathsNoLC(G,s,d):  
#    if d == 0:
#        return [[s]]
#    paths = []
#    
#    for neighbor in findNeighboorOfu(G, s):
#        for path in findPathsNoLC(G,neighbor,d-1):
#            if s not in path:
#                paths.append([s]+path)
#    return paths

def findPathsNoLC(G,s,d,excludeSet = None):
    if excludeSet == None:
        excludeSet = set([s])
    else:
        excludeSet.add(s)
    if d==0:
        return [[s]]
    paths = [[s]+path for neighbor in G.neighbors(s) if neighbor not in excludeSet for path in findPathsNoLC(G,neighbor,d-1,excludeSet)]
    excludeSet.remove(s)
    return paths



#gia upologismo tou pinaka geitonwn tou komvou s se distance d
def find_un_nei_s(s, d, neighborsOfS):
    #pinakas adjacent geitonwn tou komvou s
    n_s = []
    N = []      
    for x in neighborsOfS:   
        n_s.append(x)
    

   #an to d==1 tote oi geitones einai mono oi adjacent
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
G = nx.read_weighted_edgelist("karate.csv", create_using=nx.Graph(), delimiter=";")


#print("Edges: ", G.number_of_edges()) # 2671753
#print("Nodes: ", G.number_of_nodes())  # 16943

# arxikopoihsh se 0 ths koinotitas C
C = []

# arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
N = []

# step 1
s = '9' 

C.append(s)

#sunolo twn geitwnwn
#neighborsOfS = findNeighboorOfu(G, s) 

#print("Number of neighbors = ", len(neighborsOfS))

#print("neighbors of "+ s +": "+ str(neighborsOfS))


#orizw to distance
d = 3 

#orizw to threshold
T = 2
    
#pinakas me to sunolo geitonwn tou s se d-level
#N=find_un_nei_s(s, d, neighborsOfS)
N = findNeighboorOfu(G, s)

#print("Neighbors = ", N)

#print("Paths: ", findAllSimplePaths(G, C[0], N[0]))

##gia oso uparxoun komvoi entos tou N
while len(N)>0:
#while len(C)<2:
   
    print("Length of N = ", len(N))
   
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
        NA = find_un_nei_s(a, d, findNeighboorOfu(G,a))             
        sum_tmp = 0
               
        #gia ka8e u entos tou C
        for u in C:
                       
            sum_tmp += find_d_Ns(NA, find_un_nei_s(u, d, findNeighboorOfu(G,u)))
                       
        sum_array.append(sum_tmp)
                    
#    print("sum_array =", sum_array)
                    
    #index tou max stoixeiou            
    max_a_index = sum_array.index(max(sum_array))
    
    max_a = N[max_a_index]

#    print("Max a = ", max_a)
     
    
#    Nmax = findNeighbors(G, N[max_a], T)
    Nmax = find_un_nei_s(max_a, d, findNeighboorOfu(G,max_a))
        
    for y in C:
        if G.has_edge(y, max_a):
            IS = IS + find_d_Ns(Nmax, find_un_nei_s(y, d, findNeighboorOfu(G,y)))
                       
    #vriskw tous komvous tou grafhmatos pou den anhkoun sthn C
    nodes_not_C = np.setdiff1d(G.nodes, C)
    len_nodes_not_C = len(nodes_not_C)
#    print("C = ", C)


#    print("not C = ", nodes_not_C)
    for y in nodes_not_C:
        if G.has_edge(y, max_a):
            ES = ES + find_d_Ns(Nmax, find_un_nei_s(y, d, findNeighboorOfu(G,y)))  
  
#    print("IS = ", IS)
#    print("ES = ", ES)
    #briskw to klasma IS/(ES-IS)
    fraction=IS/(ES-IS)
    
#    print("fraction = ", fraction)
       
    nominator = 0
    denominator = 0
    
    ##############################
    
    
    if len_C == 1:
        CI = 0
    else:
        #oloi oi pi8anoi sunduasmoi metaksu 2 kombwn entos C
        lista_kombwn_C=list(itertools.combinations(C, 2))
#        print("lista komvwn = ", lista_kombwn_C)
           
        for y in lista_kombwn_C:
            #print("stoixeio: ", (lista_kombwn_C[y])[0])
            if G.has_edge(y[0], y[1]):
                nominator += find_d_Ns(find_un_nei_s(y[0], d, findNeighboorOfu(G,y[0])), (find_un_nei_s(y[1], d, findNeighboorOfu(G,y[1]))))
        
        
        for y in C:       
            for x in N: 
                if G.has_edge(y, x):
                    denominator +=  find_d_Ns(find_un_nei_s(y, d, findNeighboorOfu(G,y)), (find_un_nei_s(x, d, findNeighboorOfu(G,x))))
        
        denominator += 1

        CI = nominator/denominator
        
#        print("nominator = ", nominator)
#        print("denominator = ", denominator)
#        print("CI =", CI)
        
    #an kalutereuei to fraction pros8etw ton komvo a sth C alliws oxi 
    if fraction > CI:
        C.append(max_a) 
        N = np.delete(N, max_a_index)
        
    else:
        N = np.delete(N, max_a_index) 
             
    print('Community: ', C)
    print('----------------------------')

print('Community: ', C)

#metraw me posous komvous entos C enwnetai o s prokeimenou na upologisw to dCs (ba8mos entos C tou komvou s)
#dCs = 0
#for i in C:
#    if G.has_edge(s, i):
#        dCs += 1


##pinakas me tous ba8mous twn komvwn tou G
#degrees = []

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
      

