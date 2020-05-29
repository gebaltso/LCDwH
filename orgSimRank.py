#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:47:49 2019

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


def simrank(G, r, max_iter):

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
            for n_u in G.neighbors(u):
              for n_v in G.neighbors(v):
                s_uv += sim_old[n_u][n_v]
            sim[u][v] = (r * s_uv / (len(list(G.neighbors(u))) * len(list(G.neighbors(v)))))
      return sim

def _is_converge(s1, s2, eps=1e-4):
      for i in s1.keys():
        for j in s1[i].keys():
          if abs(s1[i][j] - s2[i][j]) >= eps:
            return False
      return True




#change dir
os.chdir('seperatedExps/datasets/lfr/')

#myFile is the input csv file with the LFR parameters in its name
#myFile = 'lfrEdgelistN1000MU0.1*.csv'
myFile = 'football.csv'
#myFile = 'youTube.csv'

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = myFile[:-4]

#copy input csv file to the weighted folder in order to run the experiments with the initial file too
shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )

#community file for Lemon algorithm
communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'

#seeds = read seed nodes from seedFile
seedFile = open('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', 'r')
seeds = seedFile.readline().split(" ")
seedsetFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt'

#keep as seed the 1st seed of seedFile
seed = seeds[0]

#Creation of the graph with the input file
#G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')
Graph = defaultdict(dict)
with open(myFile, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
        Graph[row[0]][row[1]] = row[2] 
        Graph[row[1]][row[0]] = row[2]
G = nx.Graph(Graph)

#graphSim, GraphDictSim = simRank(myFile, file, seeds, G, Graph)

s = simrank(G, 0.8, 10)
#
#
#print(s['0']['114'])
