#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:43:18 2019

@author: georgiabaltsou
"""
#!/usr/bin/python3
import networkx as nx
import csv
import os
import time
import shutil
import sys
import copy
from metrics import metrics
from collections import defaultdict
from fileWeightAdjacement import FilesAdjAll
from ReWeighting import reWeighting
from tceForAdjlist import tce 
from lteForAdjlist import lte
from newLCDForAdjlist import newLCD
from simRank import simRank
from loopEdge import addLoopEdge
from CNR import cnr
from WERWKpath import KpathAlg
from propinquity import propinquityD



#change dir
os.chdir('seperatedExps/datasets/lfr/')

#myFile is the input csv file
#myFile = 'lfrEdgelistN200MU0.10*.csv'
#myFile = 'lfrEdgelistN5000MU0.40*.csv'
#myFile = 'lfrEdgelistN200MU0.10*.csv'
#myFile = 'football.csv'
myFile = 'genes2001.csv'
#myFile = 'dblp.csv'
#myFile = 'karate.csv'
#myFile = 'NetCol.csv'

#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = myFile[:-4]

#copy input csv file to the weighted folder in order to run the experiments with the initial file too
#shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )

#community file for Lemon algorithm
communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'

#seeds = read seed nodes from seedFile
seedFile = open('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', 'r')
seeds = seedFile.readline().rstrip('\n').split(" ")
seedsetFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt'

#keep as seed the 1st seed of seedFile
seed = seeds[0]

#Creation of the graph with the input file
#G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')
#Graph = defaultdict(dict)
#with open(myFile, 'r') as read_file: 
#    reader = csv.reader(read_file, delimiter=';')
#    for row in reader:
##        if row[0] in seeds or row[1] in seeds:
#            Graph[row[0]][row[1]] = row[2] 
#            Graph[row[1]][row[0]] = row[2]
#G = nx.Graph(Graph)
#
#print("------------------------------")
#
##edges = set(G.edges())
##print("------------------------------")

os.chdir('../')

###newG = copy.deepcopy(G) #graph
###newGraph = copy.deepcopy(Graph)  #dictionary


#method = 'plain'
#
#lte(seedsetFile, file, 1, copy.deepcopy(G), copy.deepcopy(Graph), method)
#lte(seedsetFile, file, 3, copy.deepcopy(G), copy.deepcopy(Graph), method)
##
##newLCD(seedsetFile, file, copy.deepcopy(G), copy.deepcopy(Graph), method)
##tce(copy.deepcopy(G), seedsetFile, file, copy.deepcopy(Graph), myFile, copy.deepcopy(Graph), method)
##print("Initial method completed.")
##print("------------------------------")
#
#
#
#graphProp, graphPropdict = propinquityD(seeds, copy.deepcopy(G), copy.deepcopy(Graph), 2, 11, 3)
#
#method = 'propinquity'
##print(graphPropdict)
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict), method)
##tce(copy.deepcopy(graphProp), seedsetFile, file, copy.deepcopy(graphPropdict), myFile, copy.deepcopy(graphPropdict), method)
##newLCD(seedsetFile, file, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict), method)
#print("Propinquity method completed.")
#print("------------------------------")
#
#del graphProp
#del graphPropdict
#
##graphKpath, graphKpathdict = KpathAlg(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphKpath, graphKpathdict = KpathAlg(seeds, copy.deepcopy(G), copy.deepcopy(Graph))
#####print(graphKpathdict)
#
#method = 'k-path'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphKpath), copy.deepcopy(graphKpathdict), method)
##tce(copy.deepcopy(graphKpath), seedsetFile, file, copy.deepcopy(graphKpathdict), myFile, copy.deepcopy(graphKpathdict), method)
##newLCD(seedsetFile, file, copy.deepcopy(graphKpath), copy.deepcopy(graphKpathdict), method)
#print("k-path method completed.")
#print("------------------------------")
#
#del graphKpath
#del graphKpathdict
#
##graphCNR, graphCNRdict = cnr(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphCNR, graphCNRdict = cnr(seeds, copy.deepcopy(G), copy.deepcopy(Graph))
#
####print(graphCNRdict)
#
#method = 'CNR'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphCNR), copy.deepcopy(graphCNRdict), method)
##tce(copy.deepcopy(graphCNR), seedsetFile, file, copy.deepcopy(graphCNRdict), myFile, copy.deepcopy(graphCNRdict), method)
##newLCD(seedsetFile, file, copy.deepcopy(graphCNR), copy.deepcopy(graphCNRdict), method)
#print("CNR weighted graph created.")
#print("------------------------------")
#
#del graphCNR
#del graphCNRdict
#
##graphSR, graphSRdict = simRank(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
##graphSR, graphSRdict = simRank(seeds, copy.deepcopy(G), copy.deepcopy(Graph))
##print("SimRank weighted graph created.")
##print("------------------------------")
##
####print(graphSRdict)
##
##method = 'SimRank'
##
##lte(seedsetFile, file, 1, copy.deepcopy(graphSR), copy.deepcopy(graphSRdict), method)
##tce(copy.deepcopy(graphSR), seedsetFile, file, copy.deepcopy(graphSRdict), myFile, copy.deepcopy(graphSRdict), method)
##newLCD(seedsetFile, file, copy.deepcopy(graphSR), copy.deepcopy(graphSRdict), method)
##
##del graphSR
##del graphSRdict
#
#
##graphM, graphMdict = FilesAdjAll(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphM, graphMdict = FilesAdjAll(seeds, copy.deepcopy(G), copy.deepcopy(Graph))
#print("Weighted graph created.")
#print("------------------------------")
#
#method = 'MultiplyWeight'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphM), copy.deepcopy(graphMdict), method)
##tce(copy.deepcopy(graphM), seedsetFile, file, copy.deepcopy(graphMdict), myFile, copy.deepcopy(graphMdict), method)
##newLCD(seedsetFile, file, copy.deepcopy(graphM), copy.deepcopy(graphMdict), method)
#
#del graphM
#del graphMdict
#
##graphRW, graphRWdict = reWeighting(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphRW, graphRWdict = reWeighting(seeds, copy.deepcopy(G), copy.deepcopy(Graph))   
#print("Re-Weighting of edges done.")
#print("------------------------------")
#
#
#method = 'Triangles'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphRW), copy.deepcopy(graphRWdict), method)
##tce(copy.deepcopy(graphRW), seedsetFile, file, copy.deepcopy(graphRWdict), myFile, copy.deepcopy(graphRWdict), method)
##newLCD(seedsetFile, file, copy.deepcopy(graphRW), copy.deepcopy(graphRWdict), method)
#
#del graphRW
#del graphRWdict
#
##graphLoop, graphLoopdict = addLoopEdge(seeds, copy.deepcopy(graphProp), copy.deepcopy(graphPropdict))
#graphLoop, graphLoopdict = addLoopEdge(seeds, copy.deepcopy(G), copy.deepcopy(Graph))
#print("Loop edges added.")
#print("------------------------------")
#
#method = 'Loop edge'
#
#lte(seedsetFile, file, 1, copy.deepcopy(graphLoop), copy.deepcopy(graphLoopdict), method)
##tce(copy.deepcopy(graphLoop), seedsetFile, file, copy.deepcopy(graphLoopdict), myFile, copy.deepcopy(graphLoopdict), method)
##newLCD(seedsetFile, file, copy.deepcopy(graphLoop), copy.deepcopy(graphLoopdict), method)
#
#del graphLoop
#del graphLoopdict

###Give ground truth community details for metrics computation
seedstr = seed+' '  # without spaces eg if seed = 10 if is sees 101 firstly it will stop and take as community the one that 101 belongs to.

## !!!!!! if seed is the first item of a line it won't be read properly. SHOULD ADD SPACE IN FRONT OF EACH LINE OF COMMUNITYFILE!


with open(communityFile, 'r') as comm:
    for line in comm:
        if seedstr in line:
            GTC = [n for n in line.strip().split(' ')]
trueComm = len(GTC)
print(trueComm)


#create seperated metrics file for each algorithm in the communities dir
os.chdir('communities')

metrics(str(file)+'_communities.csv', GTC, trueComm)

print("Computation of metrics completed.")
print("------------------------------")


















