#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:52:32 2019

@author: georgiabaltsou
"""
import igraph as ig
import networkx as nx
import matplotlib.pyplot as plt



F = nx.read_weighted_edgelist("karate.csv", create_using=nx.Graph(), delimiter=";")

A = F.edges()

E = ig.Graph(35)

community = E.community_infomap()
plt.show()



plt.show(ig.plot(community))