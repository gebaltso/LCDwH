#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:39:24 2019

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
from fileWeightAdjacement import FilesAdjAll
from ReWeighting import reWeighting
from tceForAdjlist import tce 
from lteForAdjlist import lte
from newLCDForAdjlist import newLCD
from simRank import simRank


##change dir
#os.chdir('seperatedExps/datasets/lfr/')
#
##myFile is the input csv file with the LFR parameters in its name
##myFile = 'lfrEdgelistN1000MU0.1*.csv'
#myFile = 'football.csv'
##myFile = 'youTube.csv'
#
##file is the input file with the LFR parameters in its name, in string format(without .csv)
#file = myFile[:-4]
#
##copy input csv file to the weighted folder in order to run the experiments with the initial file too
##shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )
#
##community file for Lemon algorithm
#communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'
#
#Graph = defaultdict(dict)
#with open(myFile, 'r') as read_file: 
#    reader = csv.reader(read_file, delimiter=';')
#    for row in reader:
##        if row[0] in seeds or row[1] in seeds:
#            Graph[row[0]][row[1]] = row[2] 
#            Graph[row[1]][row[0]] = row[2]
#G = nx.Graph(Graph)
#
#
#degrees = [val for (node, val) in G.degree()]
#
#comm = ['17', '20', '27', '56', '62', '65', '70', '76', '87', '95', '96', '113']
#
#node = '113'
#count = 0
#
#for i in comm:
#    if G.has_edge(node, i):
#        count +=1
#
#print(count)

#####################################################################################################

##change dir
#os.chdir('LFRproducts/LFR1/')
#
#
#with open('communityFile.txt', 'r') as in_file:   
#
#    comms = []
#        
#    for line in in_file:    #read one line at a time 
#            
#        wholeLine = line.strip().split('\t')
#                       
#        for i in wholeLine:
#
#            item = i.strip().split(' ')
#            comms.append((item))
#            
#            
#            
#            
##change dir
#os.chdir('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/')
#
##myFile is the input csv file with the LFR parameters in its name
#myFile = 'lfrEdgelistN1000MU0.1*.csv'
##myFile = 'football.csv'
##myFile = 'youTube.csv'
#
##file is the input file with the LFR parameters in its name, in string format(without .csv)
#file = myFile[:-4]
#
##copy input csv file to the weighted folder in order to run the experiments with the initial file too
##shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )
#
##community file for Lemon algorithm
##communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'
#
#Graph = defaultdict(dict)
#with open(myFile, 'r') as read_file: 
#    reader = csv.reader(read_file, delimiter=';')
#    for row in reader:
##        if row[0] in seeds or row[1] in seeds:
#            Graph[row[0]][row[1]] = row[2] 
#            Graph[row[1]][row[0]] = row[2]
#G = nx.Graph(Graph)
#            
#       
##degrees = [val for (node, val) in G.degree()]
#
#
#
#degs = defaultdict(dict)
#node = comms[0][1]
#nodeDeg = (G.degree(node))
#
#count = 0
#
#for i in comms[0]:
#
#    if G.has_edge(node, i):
#        count += 1
#        degs[i] = count 
#  
#for i in degs:
#    degs[i] = round((degs[i]/nodeDeg),3)
#      
#print(degs)    
        
#####################################################################################################    
    

def findItem(theList, item):
   return [(ind, theList[ind].index(item)) for ind in range(len(theList)) if item in theList[ind]]


    
#change dir
os.chdir('/Users/georgiabaltsou/Desktop/Datasets/dblp/')

#myFile is the input csv file with the LFR parameters in its name
#myFile = 'dblp.csv'
#myFile = 'football.csv'
myFile = 'dblp.csv'
communityFile = 'communityFile.txt'
#myFile = 'karate.csv'


#file is the input file with the LFR parameters in its name, in string format(without .csv)
file = myFile[:-4]

finalReadFile = str(file) + 'NODES.csv'
finalFile = str(file) + 'Degrees.csv'


with open(communityFile, 'r') as in_file:   

    comms = []
        
    for line in in_file:    #read one line at a time 
            
        wholeLine = line.strip().split('\t')
                       
        for i in wholeLine:

            item = i.strip().split(' ')
            comms.append((item))
            
                    


#copy input csv file to the weighted folder in order to run the experiments with the initial file too
#shutil.copy2(myFile, '../weighted/'+str(file)+'<11111-11111>1.csv' )

#community file for Lemon algorithm
#communityFile = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/communityFile.txt'

Graph = defaultdict(dict)
with open(myFile, 'r') as read_file: 
    reader = csv.reader(read_file, delimiter=';')
    for row in reader:
#        if row[0] in seeds or row[1] in seeds:
            Graph[row[0]][row[1]] = row[2] 
            Graph[row[1]][row[0]] = row[2]
G = nx.Graph(Graph)
            
 
      
#degrees = [val for (node, val) in G.degree()]

with open(finalReadFile, 'r') as in_file:
    reader = csv.reader(in_file, delimiter=';')
            
    with open(finalFile, 'a') as out_file:
        writer = csv.writer(out_file, delimiter=';')
        
        for row in reader:
            
            degs = defaultdict(dict)
            node = str(row[0])
            

            nodeDeg = (G.degree(node))
            
            
            if not isinstance(nodeDeg, int): # if the node hasn't any neighbors it's type won't be int. So pass it!
                continue
            
            if len(findItem(comms, node))==0:
               
                continue
            else:
                indexOfComm = (findItem(comms, node)[0][0])
            
            count = 0
  
            for i in comms[indexOfComm]:
            
                if G.has_edge(node, i):
                    count += 1
#                    degs[i] = count 
              
#            for i in degs:
#                degs[i] = round((degs[i]/nodeDeg),3)
             


            writer.writerow([row[0], nodeDeg, count, round(count/nodeDeg, 2)])
            

        
        
        
        
        
    


      
      
        
 
        
        
        
