#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:27:28 2019

@author: georgiabaltsou
"""


import csv
import os


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:13:39 2019

@author: georgiabaltsou
"""

import networkx as nx
import numpy as np
import csv
import os


def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors


def reWeighting(file):

    
    G = nx.Graph()
    G = nx.read_weighted_edgelist(file, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')
    
    
    cycls_3 = [c for c in nx.cycle_basis(G) if len(c)==3]   #cycles
        
    #Compute the denominator We
    WeDict = {}
    
    for edge in G.edges():
        
        We = 0
        EuUEv = []
        source, target = edge
        EuUEv = np.union1d(list(G.neighbors(source)), list(G.neighbors(target)))
           
        for node in EuUEv:
            
            if node == source:
                continue
    
            if (source,node) in G.edges:
            
                weightForux = G.get_edge_data(source, node)
                temp1 = weightForux['weight']
                We +=  temp1
                
            elif (target,node) in G.edges:
            
                weightForux = G.get_edge_data(target, node)
                temp1 = weightForux['weight']
                We +=  temp1
                
        #to add the edge weight too
        weightForux = G.get_edge_data(source, target)
        temp1 = weightForux['weight']    
        We += temp1
        
        WeDict[edge] = We
      
                
    #Compute the nominator Ge
    GeDict = {}
    
    for edge in G.edges():
                
        Ge = 0
        EuUEv = []
        source, target = edge
        EuUEv = np.union1d(list(G.neighbors(source)), list(G.neighbors(target)))
        
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
    
            if (source,node) in G.edges:
            
                weightForux = G.get_edge_data(source, node)
                temp1 = weightForux['weight']
                Ge +=  temp1
                
            elif (target,node) in G.edges:
            
                weightForux = G.get_edge_data(target, node)
                temp1 = weightForux['weight']
                Ge +=  temp1
                
        #to add the edge weight too
        weightForux = G.get_edge_data(source, target)
        temp1 = weightForux['weight']    
        Ge += temp1
        
        GeDict[edge] = Ge
                                              
      
    Ce = {}   
    for key, value in WeDict.items():   
        for key2, value2 in GeDict.items():    
            if(key==key2):
                Ce[key] = value/value2
                 
    
    #change the graph's weights after the re-calculating
    for u,v,d in G.edges(data=True):
             d['weight'] = Ce[u,v]
    
   
    with open('new', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=' ')
        for key, value in Ce.items():
            writer.writerow([key[0], key[1], value])

    return str(csv_file), G



def FilesAdjAll(myFile, s, graph): 
 
        counter2 = 2
        #change counter to <=10 for more weights
        while(counter2<=6):
            

            with open(myFile) as data_file: 
                reader = csv.reader(data_file, delimiter=' ')
                
                
                with open(str(myFile)+'<'+str(s)+'-'+str(s)+'>'+str(counter2), 'a') as out_file:
                    writer = csv.writer(out_file, delimiter=' ')
                        
                    
                    for row in reader:
                        w = float(row[2])
                        for j in graph.neighbors(s):

                            if ((row[0] == s) and (row[1] == j)) or ((row[1] == s) and (row[0] == j)):
                                w *= counter2 
                        writer.writerow([row[0],row[1], w])
                            
                    counter2 += 2 



file = 'lfr.csv'

newfile, G = reWeighting(file)

FilesAdjAll('lfr2', '433', G)
