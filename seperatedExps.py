#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:10:01 2019

@author: georgiabaltsou

Run seperated examples for unweighted, reweighted etc graphs
"""

import networkx as nx
import csv
import os
import time
import shutil
import sys
from collections import defaultdict
from lemonW import lemon
from lte import lte
from tce import tce 
from newLCD import newLCD
from metrics import metrics
from fileWeightAdjacement import FilesAdjAll
from ReWeighting import reWeighting
from csvToText import csvToText


#keep the starting time
start_time = time.time()

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


#calculate the number of edges and the number of nodes of the input graph
numberOfEdges = G.number_of_edges()
numberOfNodes = G.number_of_nodes()   
print("The network has", numberOfNodes, "nodes with", numberOfEdges, "edges.")
print("------------------------------")

os.chdir('../')
#print("Current Working Directory " , os.getcwd())

#call reWeighting for find new weights for the graph's edges. ReWeigthedFile will be stored in weighted folder.
graphRW, GraphRW = reWeighting(myFile, file, seeds, G, Graph)   
print("Re-Weighting of edges done.")
print("------------------------------")


#adjacement of all neighbors' of a node weight (x3)
MultWeightedFile, graphM, GraphM = FilesAdjAll(myFile,file, seeds, G, Graph)
print("Weighted file created.")
print("------------------------------")


#convert each file in weighted folder to plain text file and move them to weightedForLemon dir
for filename in os.listdir('weighted'):        
    if not filename.startswith('.'):
        filenameSplit = filename.split('csv')[0]
        shutil.move(csvToText('weighted/'+filename, 'weighted/'+str(filenameSplit)), 'weightedForLemon/'+filenameSplit)
print("Convertion and move of files for Lemon algorithm completed.")
print("------------------------------")


#run the experiments with all the files in weighted dir, and with LTE, TCE, NewLCD algorithms
for filename in os.listdir('weighted'):        
    if not filename.startswith('.'): 
        #check if the file is the original or the RW in order to run LTE too, otherwise only TCE and NewLCD
        if (filename.split('>')[1]).split('.')[0] == '1' or (filename.split('>')[1]).split('.')[0] == '0':
            lte('weighted/'+str(filename), seedsetFile, file, 1, G)   #call lte 2 times, with flag=1 to return plain lte and with flag=3 to return lte with similarity*3 for u and its neighbors
            lte('weighted/'+str(filename), seedsetFile, file, 3, G)
            tce('weighted/'+str(filename), seedsetFile, file, G)         
            newLCD('weighted/'+str(filename), seedsetFile, file, G) 
        else:
            tce('weighted/'+str(filename), seedsetFile, file, G)         
            newLCD('weighted/'+str(filename), seedsetFile, file, G)
print("LTE, TCE, newLCD  algorithms completed.")
print("------------------------------")


#run the experiments with all thw files in weighted dir, and with Lemon algorithm
for filename in os.listdir('weightedForLemon'):        
    if not filename.startswith('.'):           
            lemon('weightedForLemon/'+str(filename), '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/seedsetFile.txt', str(filename), communityFile, str(file))
print("Lemon  algorithm completed.")
print("------------------------------")


#Give ground truth community details for metrics computation
#GTC = [3, 5, 10, 40, 52, 72, 74, 81, 84, 98, 102, 107]
#GTC  = [str(i) for i in GTC]
seedstr = ' '+seed+' '
with open(communityFile, 'r') as comm:
    for line in comm:
        if seedstr in line:
            GTC = [n for n in line.strip().split(' ')]
trueComm = len(GTC)


#create seperated metrics file for each algorithm in the communities dir
os.chdir('communities')
for filename in os.listdir(os.getcwd()): 
    if not filename.startswith('.'):      
        metrics(str(filename), GTC, trueComm)
print("Computation of metrics completed.")
print("------------------------------")

#print complete execution time
print("Execution time: %s seconds " % (time.time() - start_time))
print("------------------------------") 


###############################################################################




#GTC = [260,781,656,531,533,288,37,39,807,298,814,174,433,439,824,827,829,706,578,71,711,713,329,327,210,352,485,616,236,371,501,246,638,639]
#GTC  = [str(i) for i in GTC]
#
#
###find the length of the community stored in GTC
#trueComm = len(GTC)
#
#
##sys.exit()
#
#
#os.chdir('../')
#
#seed = '485'
#
##for seed in GTC:
###    FilesAdj(myFile,seed, G)
##    FilesAdjAll(myFile,seed, G)
#
#
###FilesAdj(myFile,seed, G) #adjacement of each node's weight
#
##FilesAdjAll(myFile,seed, G) #adjacement of all neighbors' of a node weight
##ReduceW(myFile,seed, G) #adjacement of all neighbors' of a node weights
##
##print("Weighted files created.")
##print("------------------------------")
#
##sys.exit()
#
##print("Current Working Directory " , os.getcwd())
##
##os.chdir('../')
##seed = '485'
#
#for filename in os.listdir('weighted'):
##    for seed in GTC:
#        
#    if not filename.startswith('.'):        
#    
##            lemon('weighted/'+str(filename), seed, file)
#            
#            lte('weighted/'+str(filename), seed, file)
#    
##            tce('weighted/'+str(filename), seed, file)
##           
##            newLCD('weighted/'+str(filename), seed, file)
#        
#
#print("Algorithms completed.")
#print("------------------------------")
#
#os.chdir('communities')
#
#
#for filename in os.listdir(os.getcwd()):
#    
#    
#    if not filename.startswith('.'):
#    
#        algorithm = filename.split("_")[0]
#        
#        metrics(str(filename), GTC, trueComm, algorithm)
#
#
#print("Execution time: %s seconds " % (time.time() - start_time))
#print("------------------------------") 

