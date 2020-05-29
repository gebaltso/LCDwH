#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:19:14 2019

@author: georgiabaltsou
"""

import networkx as nx
import csv
import os
import time
import shutil
import sys
import copy
from collections import defaultdict
from numpy import array


def simrank(G, r, max_iter, n, Graph):

#    sim_old = defaultdict(list)
#    sim = defaultdict(list)
#      for n in G.nodes():
#    sim[n] = defaultdict(int)
#    sim[n][n] = 1
#    sim_old[n] = defaultdict(int)
#    sim_old[n][n] = 0
#
#      # recursively calculate simrank
#    for iter_ctr in range(max_iter):
#        if _is_converge(sim, sim_old):
#          break
#        sim_old = copy.deepcopy(sim)
#        for u in G.nodes():
#          for v in G.nodes():
#            if u == v:
#              continue
#            s_uv = 0.0
#            for n_u in Graph[u].keys():
#              for n_v in Graph[v].keys():
#                s_uv += sim_old[int(n_u)][int(n_v)]
#            sim[u][v] = (r * s_uv / (len(list(Graph[u].keys())) * len(list(Graph[v].keys()))))
#    return sim
#
#def _is_converge(s1, s2, eps=1e-4):
#      for i in s1.keys():
#        for j in s1[i].keys():
#          if abs(s1[i][j] - s2[i][j]) >= eps:
#            return False
#      return True
    
    
    
    
#    Na = list(Graph[n].keys()) 
#    numNa = len(Na)
#    
#    
#    for i in Na:
        
    
    
      sim_old = defaultdict(list)
      sim = defaultdict(list)
      for n in G.nodes():
        sim[n] = defaultdict(int)
        sim[n][n] = 1
        sim_old[n] = defaultdict(int)
        sim_old[n][n] = 0

      # recursively calculate simrank
      for iter_ctr in range(max_iter):
        if _is_converge(sim, sim_old):
          break
        sim_old = copy.deepcopy(sim)
        for u in G.nodes():
          for v in G.nodes():
            if u == v:
              continue
            s_uv = 0.0
            for n_u in list(Graph[u].keys()):
              for n_v in list(Graph[v].keys()):
                s_uv += sim_old[n_u][n_v]
            sim[u][v] = (r * s_uv / (len(list(Graph[u].keys())) * len(list(Graph[v].keys()))))
      return sim

def _is_converge(s1, s2, eps=1e-4):
      for i in s1.keys():
        for j in s1[i].keys():
          if abs(s1[i][j] - s2[i][j]) >= eps:
            return False
      return True
    
    
    