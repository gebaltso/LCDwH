#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:19:29 2019

@author: georgiabaltsou
"""

from collections import defaultdict
import csv
import networkx as nx

file = 'football.csv'

graph = defaultdict(dict)



with open(file, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
        graph[row[0]][row[1]] = row[2]
        graph[row[1]][row[0]] = row[2]
        
#print(graph['1'])
        
G = nx.Graph(graph)

#print([n for n in G.neighbors('168')])

numberOfEdges = G.number_of_edges()
numberOfNodes = G.number_of_nodes()   
print("The network has", numberOfNodes, "nodes with", numberOfEdges, "edges.")
print("------------------------------")