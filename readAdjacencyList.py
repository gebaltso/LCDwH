#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 19:36:07 2018

@author: georgiabaltsou
"""

import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np 
import pandas as pd
from sqlalchemy import create_engine
import csv
import collections
import itertools


#mydata = genfromtxt('/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv', delimiter=',')

#adjacency = list

#G = nx.Graph()
#
#G=nx.read_adjlist("/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv", delimiter=',')
#
##na mh sxediazontai oi aksones    
#plt.axis('off')         
#
##sxediasmos grafou
#nx.draw(G, with_labels = False) 

#############read length of csv file
#f = open('/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv', 'r')
#s = f.read()
#f.close()
#
#length = len(s)
#
#i = 0
#genes = 0
#d = []

#while(i<length): #compute the number of patients
#        
#        if(s[i]=='\n'): genes += 1
#        i += 1
#print('number of genes is: ', genes)

#with open('/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv') as data_file:
#    for line in data_file:
#         x = line.split(',')
#         d.append(x)
#         
#print (d[2])


###############

#G = nx.read_weighted_edgelist('/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv') 
#A = nx.adjacency_matrix(G)
#
#print (A.todense())

#with open('/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv') as f:
#    for i,line in enumerate(f):             
#        print ("line {0} = {1}".format(i,line.split()))


#file = '/Users/georgiabaltsou/Desktop/test.csv'
#
#G=nx.read_adjlist(file, create_using=nx.DiGraph(), delimiter = ',')


##na mh sxediazontai oi aksones    
#plt.axis('off')         
#
##sxediasmos grafou
#nx.draw(G, with_labels = False)

SourceFile = '/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv'
TestFile = '/Users/georgiabaltsou/Desktop/test.csv'
TestFile2 = '/Users/georgiabaltsou/Desktop/test 2.csv'
TestFile5 = '/Users/georgiabaltsou/Desktop/test5.csv'

sourceNodes = []
nodes = []
weights = []

nodesTmp = []
weightsTmp = []

with open(TestFile2) as csvfile:
    dataFile = csv.reader(csvfile,skipinitialspace=True, delimiter = ',')
        
    for row in dataFile:
         sourceNodes.append(row[0])
         
         for y in range(len(row)):
             if(y%2 != 0):
                 nodesTmp.append(row[y])
             else:
                 if(y != 0):
                     weightsTmp.append(row[y])
         nodes.append(nodesTmp)
         nodesTmp = []
         weights.append(weightsTmp)
         weightsTmp = []
    
#gia na afairesw ta ' ' apo ta weights  
weights = [list(map(float, grp)) for grp in weights]

                
#print('nodes = ', nodes)
#print('weights = ', weights)
#
#print('Source Nodes = ', sourceNodes)

graph = collections.defaultdict(list)
edges = {}

for i in range (0,len(sourceNodes)):
    for j in range (0, len(nodes[i])):
            graph[sourceNodes[i]].append(nodes[i][j])
            edges[sourceNodes[i], nodes[i][j]] = weights[i][j]


print("Edges with their weights: ", edges)
#print(dict(graph))

G = nx.Graph(graph)

#G = nx.Graph()
#
##add nodes to graph
#for i in range (0,len(sourceNodes)):
#    G.add_node(sourceNodes[i])
# 
print("Nodes of the graph: ", G.nodes())
print("Edges of the graph: ", G.edges)

#add edges to graph
#for i in range (0,len(sourceNodes)):
#    for j in range (0, len(nodes[i])):    
#        G.add_edge(sourceNodes[i], nodes[i][j])
#        G[sourceNodes[i]][nodes[i][j]]['weight']= weights[i][j]
 


#na mh sxediazontai oi aksones    
plt.axis('off')         

#sxediasmos grafou
nx.draw(G) 


    
#d = []
#       
#for i in range(0, len(sourceNodes)):
#    
#    for j in range (0, len(nodes[i])):
#        d.append(sourceNodes[i])
#        d.append(nodes[i][j])
#        d.append(weights[i][j])
#        
##d = [d[x:x+len(nodes[i])+1] for x in range(0, len(d),len(nodes[i])+1)]
#             
#
#d = list(zip(*[iter(d)]*3))
#      
#print(set(d))
#
##unique_combinations = itertools.combinations(d, 1)
##print(list(unique_combinations))
#
#
#y = list(set(d))
#
#print(y)
#
#G = nx.Graph()
#
##G.add_edges_from(d)
#
##na mh sxediazontai oi aksones    
#plt.axis('off')         
#
##sxediasmos grafou
#nx.draw(G) 












