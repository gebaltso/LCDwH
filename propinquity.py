#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:49:14 2019

@author: georgiabaltsou
"""

import networkx as nx

#gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo s kai me mhkos paths d
def findPathsNoLC(G,s,d):  
    if d == 0:
        return [[s]]
    paths = []
    for neighbor in G[s].keys():
        for path in findPathsNoLC(G,neighbor,d-1):
            if s not in path:
                paths.append([s]+path)
    return paths



def propinquityD(seeds, G, Graph, newGraph, distance, a, b):

    C = nx.Graph()    
    for s in seeds: # gia ka8e seed kataskeuazw ton ypografo tou ws kai depth=distance
        tmp = nx.ego_graph(G, s, radius=distance)
        C = nx.compose(C, tmp)
        
#    print("Nodes=", len(C.nodes()), "Edges=", len(C.edges()))
        
    nodes = list(nx.nodes(C))
    for seed in seeds:
        neighbors_seed = [j for j in C.neighbors(seed)]
        for i in nodes:
            if C.has_edge(seed, i):
                s1 = 1
            else:
                s1 = 0
            neighbors_i = [j for j in C.neighbors(i)]
        
            common = set(neighbors_seed).intersection(set(neighbors_i))

            counter = 0 # find number of edges between the node's neighbors            
            for j in common:
                for k in common:
                    if j in Graph and k in Graph[j] :
                        counter += 1
            counter /= 2 
                
            prop = s1 + len(neighbors_i) + counter
            
            if prop >= b and not G.has_edge(seed, i):
#                print('add ', prop, seed, i)
                Graph[seed][i] = 1
                Graph[i][seed] = 1
                
            if prop <= a and G.has_edge(seed, i):
#                print('rem ', prop, seed, i)
                del Graph[seed][i]
                del Graph[i][seed]


    G = nx.Graph(Graph)
    

#    for source, target in G.edges():
#        if source in newGraph:
#            if target in newGraph[source]:
#                G[source][target]['weight'] = newGraph[source][target]
#            else:
#                G[source][target]['weight'] = 1
    
    for source, target in G.edges():
        G[source][target]['weight'] = Graph[source][target]
    
          
#    print(G.edges.data())

    return G, Graph




#os.chdir('seperatedExps/datasets/lfr/')
#
##myFile is the input csv file
##myFile = 'lfrEdgelistN1000MU0.1*.csv'
##myFile = 'lfrEdgelistN5000MU0.40*.csv'
#myFile = 'football.csv'
##myFile = 'youTube.csv'
##myFile = 'dblp.csv'
##myFile = 'karate.csv'
#
##file is the input file with the LFR parameters in its name, in string format(without .csv)
#file = myFile[:-4]
#
##seeds = read seed nodes from seedFile
#seedFile = open('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', 'r')
#seeds = seedFile.readline().split(" ")
#seedsetFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt'
#
##keep as seed the 1st seed of seedFile
#seed = seeds[0]
#
##Creation of the graph with the input file
##G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')
#Graph = defaultdict(dict)
#with open(myFile, 'r') as read_file: 
#    reader = csv.reader(read_file, delimiter=';')
#    for row in reader:
##        if row[0] in seeds or row[1] in seeds:
#            Graph[row[0]][row[1]] = row[2] 
#            Graph[row[1]][row[0]] = row[2]
#G = nx.Graph(Graph)



##distance = 2
## a = 3
## b = 8
#newG, newDictG = propinquityD(seeds, G, Graph, 2, 3, 8)



# to propinquity prepei na epistrefei enan pinaka me times metaksy olwn twn akmwn poy upologisthke! Oxi to Graph!!! Gt 8a kanw allages k meta 8a dhmiourghsw neo Graph!!!






