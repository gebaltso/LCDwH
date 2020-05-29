#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:28:39 2019

@author: georgiabaltsou
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import sys
import os
import random


def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors



os.chdir('seperatedExps/datasets/lfr/')

myFile = 'lfrEdgelistN1000MU0.1*.csv'
filename = "lfrCommN1000MU0.1*.txt"



G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')


GTC = [260,781,656,531,533,288,37,39,807,298,814,174,433,439,824,827,829,706,578,71,711,713,329,327,210,352,485,616,236,371,501,246,638,639]

GTC  = [str(i) for i in GTC]


nei = findNeighboorOfu(G,GTC[33])

counter = 0
for i in nei:
    if i in GTC:
        counter +=1
        
#print(nei)     
print(counter)

