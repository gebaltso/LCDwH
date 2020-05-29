#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:22:42 2019

@author: georgiabaltsou
"""
import networkx as nx
import csv
import os
import time
import shutil
import sys
from collections import defaultdict
from fileWeightAdjacement import FilesAdjAll
from ReWeighting import reWeighting
from tceForAdjlist import tce 
from lteForAdjlist import lte
from newLCDForAdjlist import newLCD

#change dir
os.chdir('seperatedExps/datasets/lfr/')

#myFile is the input csv file with the LFR parameters in its name
#myFile = 'lfrEdgelistN1000MU0.1*.csv'
myFile = 'football.csv'
#myFile = 'youTube.csv'

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = myFile[:-4]

#copy input csv file to the weighted folder in order to run the experiments with the initial file too
#shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )

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


#calculate the number of edges and the number of nodes of the input graph
#numberOfEdges = G.number_of_edges()
#numberOfNodes = G.number_of_nodes()   
#print("The network has", numberOfNodes, "nodes with", numberOfEdges, "edges.")
print("------------------------------")

os.chdir('../')
#print("Current Working Directory " , os.getcwd())

#lte(seedsetFile, file, 1, G, Graph)
#lte(seedsetFile, file, 3, G, Graph)

#sys.exit()

#call reWeighting for find new weights for the graph's edges. ReWeigthedFile will be stored in weighted folder.
#graphRW, graphRWdict = reWeighting(seeds, G, Graph)   
#print("Re-Weighting of edges done.")
#print("------------------------------")

#f = open("dict.txt","w")
#f.write( str(GraphRW) )
#f.close()
#print(GraphRW)


#tce(graphRW, seedsetFile, file, graphRWdict)
#newLCD(seedsetFile, file, graphRW, graphRWdict)

#krataei ws Graph to allagmeno!!!!!to RW dld

#adjacement of all neighbors' of a node weight (x3)
graphM, graphMdict = FilesAdjAll(seeds, G, Graph)
print("Weighted graph created.")
print("------------------------------")


#newLCD(seedsetFile, file, graphM, graphMdict)
#sys.exit()

tce(graphM, seedsetFile, file, graphMdict)
















