#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:05:46 2019

@author: georgiabaltsou

Re Weighting of edges based on 2011-Berry-Tolerating the community detection resolution limit with edge weighting
taking into account only the hint node and its adjacent edges

""" 

import networkx as nx
import numpy as np


pastSeed = ' ' 


def findNeighboorOfu(graphRW,u):
    neighbors = []
    for i in graphRW.neighbors(u):
        neighbors.append(i)
    return neighbors

def calculateCycles(seed, graphRW, graphRWdict):
    
            global pastSeed
            global cliques
            global cycls_3

            if seed != pastSeed:
                cliques = nx.cliques_containing_node(graphRW, seed) #triangles
                cycls_3 = [ x for x in cliques if len(x)==3 ]
            
     
            #Compute the denominator We
            WeDict = {}
            
            for edge in graphRW.edges(seed):
        
                
                We = 0
                EuUEv = []
                source, target = edge
                EuUEv = np.union1d(list(graphRW.neighbors(source)), list(graphRW.neighbors(target)))
                   
                for node in EuUEv:
                    
                    if node == source:
                        continue
            
                    if (source,node) in graphRW.edges(seed):
                    
                        temp1 = float(graphRWdict[source][node])
                        We +=  temp1
                        
                    elif (target,node) in graphRW.edges(seed):

                        temp1 = float(graphRWdict[target][node])
                        We +=  temp1
                        
                #to add the edge weight too
                temp1 = float(graphRWdict[source][target])
                We += temp1
                
                WeDict[edge] = We
              
                        
            #Compute the nominator Ge
            GeDict = {}
            
            for edge in graphRW.edges(seed):
                
                        
                Ge = 0
                EuUEv = []
                source, target = edge
                EuUEv = np.union1d(list(graphRW.neighbors(source)), list(graphRW.neighbors(target)))
                
                Te = 0  #number of cyrcles e participates in
                
                TeList = []
                
                for i in cycls_3:
                    if source in i and target in i:
                        Te += 1
                        TeList.append(i)
   
                intersection = np.intersect1d(EuUEv,TeList )
                
        
                   
                for node in intersection:
                    
                    if node == source:
                        continue
            
                    if (source,node) in graphRW.edges(seed):

                        temp1 = float(graphRWdict[source][node])
                        Ge +=  temp1
                        
                    elif (target,node) in graphRW.edges(seed):

                        temp1 = float(graphRWdict[target][node])
                        Ge +=  temp1
                        
                #to add the edge weight too
                temp1 = float(graphRWdict[source][target])
                Ge += temp1
                
                GeDict[edge] = Ge
                                                      
              
            Ce = {}   
            for key, value in WeDict.items():   
                for key2, value2 in GeDict.items():    
                    if(key==key2):
                        Ce[key] = value/value2

            for u,v in graphRW.edges(seed):
                graphRWdict[u][v] = Ce[u,v]
                graphRWdict[v][u] = Ce[u,v]
                     
                  
            pastSeed = seed
                
            return nx.Graph(graphRWdict), graphRWdict





def reWeighting(seeds, graphRW, graphRWdict):
    
    
    for node in graphRWdict:
        if node in seeds:
            graphRW, graphRWdict = calculateCycles(node, graphRW, graphRWdict)
            
      
        
    for source, target in graphRW.edges():
        graphRW[source][target]['weight'] = graphRWdict[source][target]       
    
    
    return graphRW, graphRWdict
        
        
