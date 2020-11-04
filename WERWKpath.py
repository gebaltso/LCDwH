#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:01:16 2019

@author: georgiabaltsou
"""

import networkx as nx
import numpy as np
from collections import defaultdict
import copy
import sys
import random


def messagePropagation(un, N, k, Graph):
    
    # initialize the T containing the edges already visited
    T = set()
    
    # initialize the weight dict
    weightDict = defaultdict(dict)
    
    # initialize the probability dictionary
    Pr = defaultdict(dict)
    
    while N < k and (len(list(Graph[un].keys())) > len(T) ):
         
        # find the adjacent edges to node un        
        neiOfUn = set([((un), (node)) for node in Graph[un]])
                
        # Ihat is the set of edges that haven't been visited yet        
        Ihat = neiOfUn - T
        
        # weight = 1 for all edges in Ihat
        for i in Ihat:
            weightDict[i] = 1                             
        
        
        sumOfW = 0
        for i in Ihat:                         
            sumOfW = sumOfW + weightDict[i]  
     
        
        Pr = defaultdict(dict)
        for i in Ihat:
            Pr[i] = weightDict[i]/sumOfW
            
        # find the index of the edge at random way considering the probabilities of edges    
        newUnIndex = (np.random.choice(len((Pr.keys())), p=list(Pr.values())))
        
        # find the exact edge from the above index
        newUn = list(Pr)[newUnIndex]
        
        # find the node reached by the above edge
        newNode = newUn[1]  
        
        
        # increase by 1 the weight of the above edge        
        Graph[un][newNode] += 1
        Graph[newNode][un] += 1
        weightDict[newUn] += 1
        
        # add the edge to the visited edges        
        T.add(newUn)        
        
        # un is now the new edge
        un = newNode
        
        #increase N by 1
        N += 1
        
        
    return Graph
    


def findDelta(node, G, Graph):
    
    #delta is used for the selection of node un.
   
    # delta is in [0,1]. The higher it is, the better connected is node to the graph.
    
    nominator = len(list(Graph[node].keys()))
    denominator = (G.number_of_nodes())
        
    return nominator/denominator
    
    

def KpathAlg(seeds, G, Graph):
    
#    un = seeds[0] #the node is un
    
    for un in seeds:
    
        # depends on the preferred community size and depicts how many random walks will be held
        p = 10 
        
        for edge in Graph: # weight = 0 in the initial graph
            for secEdge in Graph[edge]:             
                    Graph[edge][secEdge] = 1 # weight = 1 in the un's adjacent nodes
                    Graph[secEdge][edge] = 1                           
        
        k = 20
                
    
        for i in range(1, p+1):
            N = 0 #counter to check the length of the k-path
                    
            Graph = messagePropagation(un, N, k, Graph)
                
            
        for key in Graph:
            for i in Graph[key]:
                Graph[key][i] = Graph[key][i]/p
                        



#    G = nx.Graph(Graph)
    
    for source, target in G.edges():
        G[source][target]['weight'] = Graph[source][target]



    return G, Graph

                
                

            
       
       
        
        
    
  
 
