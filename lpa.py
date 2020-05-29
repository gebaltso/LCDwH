#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:05:17 2018

@author: georgiabaltsou
"""
#dividing the original network into several communities firstly,
#and then the community containing the given starting node is the local community of the given starting node. 

#https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.community.label_propagation.asyn_lpa_communities.html

import networkx as nx
 

G = nx.Graph()
#G = nx.read_weighted_edgelist("filteredOutputPearson.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFilePearson.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFileCosine.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("finalGeneFileEuclidean.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("pearsonSupera.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_weighted_edgelist("karate.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("karateUnw.csv", create_using=nx.Graph(), delimiter=";")
G = nx.read_weighted_edgelist("netCol.csv", create_using=nx.Graph(), delimiter=";")


print("Graph Created")

print(list(nx.algorithms.community.label_propagation.asyn_lpa_communities(G,'weight')))

#print(list(nx.algorithms.community.label_propagation.asyn_lpa_communities(G, weight=None)))