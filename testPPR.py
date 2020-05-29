#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:59:01 2019

@author: georgiabaltsou
"""

import networkx as nx

G = nx.Graph()
G = nx.read_weighted_edgelist("karate/karate.csv", create_using=nx.Graph(), delimiter=";")


p = nx.pagerank(G, alpha=0.9, tol=1.e-08, weight='weight')

print(p)
