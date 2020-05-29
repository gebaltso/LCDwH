#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:59:15 2018

@author: georgiabaltsou

2017-Michael Hamann,Eike Röhrs and Dorothea Wagner- 
Local Community Detection Based on Small Cliques
"""

import networkx as nx
import numpy as np 
import csv
import os
import time


def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors

def CONDUCTANCE(G, C):  
    
    #cut
    cut = nx.cut_size(G,C, weight='weight')
    
    #bazei epipleon mia fora to metaksu 3 kai 11 baros
    vol = nx.cuts.volume(G, C, weight='weight')

    conductance = cut/vol

    return conductance


#upologismos tou deg ston paronomasth tou edge score
def deg(u, N, G):
    deg = 0
    
    for i in N:
        w = G.get_edge_data(u, i, default=0)
        deg += w['weight']
          
    return deg


#upologismos tou edge score
def SCORE(u, S, C, G):
        
    #geitones Nu
    Nu = findNeighboorOfu(G,u)
    
    #briskw thn tomh sthn opoia anhkei o komvos v    
    V = np.intersect1d(C, Nu)
    
    #krataw ta edgeScores ka8e komvou pou anhkei sto V        
    sumOfEdgeScore = 0

    #baros metaksu u kai v
    wuv = 0

    for v in V:
                
        #w(u,v)       
        w = G.get_edge_data(u, v, default=0)
        wuv = w['weight']

        #geitones tou v
        Nv = findNeighboorOfu(G,v)
        
        #X h tomh geitonwn u me geitones tou v
        X = np.intersect1d(Nv, Nu)

        sumOfMin = 0
        for x in X:
            w1 = G.get_edge_data(u, x, default=0)
            ux = w1['weight']
            w2 = G.get_edge_data(v, x, default=0)
            vx = w2['weight']
  
            sumOfMin += (min(ux, vx))
           
        
        #o ari8mhths tou klasmatos tou edge score
        nominator = wuv + sumOfMin
        
        degu = deg(u, Nu, G)
        degv = deg(v, Nv, G)
        
        denominator = min(degu, degv)
        
        sumOfEdgeScore += (nominator/denominator)
    
    
    score = ((1/len(Nu))*(sumOfEdgeScore))
        
    return score

def tce(file, seedsetFile, myFile, G):
    # main program
    
    start_time = time.time()
    
    alg = 'tce'
    
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().split(" ")
    lenS = len(seeds)
    
    node1 = file.split("<")[1].split("-")[0]
    
    node2 = file.split("-")[1].split(">")[0]
    
    wName = file.split(">")[1].split(".")[0]
    
    # arxikopoihsh se 0 ths koinotitas C
    C = []    
#    C.append(s)
    
    #sunolo twn geitwnwn
#    S = findNeighboorOfu(G, s)
    #xrhsimopoieitai mono gia th diaforopoihsh tou score
    #firstS = S
    
    # arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
    SInitial = []
    
    # arxikopoihsh ths seed list
    global s
    s = []
    
    for i in range(lenS):
        C.append(seeds[i])
        s.append(seeds[i])
        SInitial.append(findNeighboorOfu(G, seeds[i]))
    # Make list of lists one list    
    S = [val for sublist in SInitial for val in sublist]
    
    while len(S)>0 and len(C)<100:
    
        #pinakas me ta scores twn stoixeiwn tou S
        score_array = []
        for u in S:
            score_array.append(SCORE(u, S, C, G))
        
        #briskw to maximum score apo ta scores twn S
        maxScore = np.amax(score_array)
            
        #briskw th 8esh tou maxScore
        index = score_array.index(maxScore)
            
        #briskw ton komvo me to max score
        umax = S[index]
        
        #afairw apo to S ton komvo me to max score 
        if (type(S) != list):
            S = S.tolist()
        S.remove(umax)
        
        #conductance of C
        conOfC = CONDUCTANCE(G, C)
        
        CWithU = []
        for i in C:
            CWithU.append(i)
        CWithU.append(umax)
            
        #conductance of C with umax
        conOfCWithUmax = CONDUCTANCE(G, CWithU)
        
        #an isxuei h sun8hkh pros8etw ton umax sthn C ki episis pros8etw sto S tous geitones tou umax pou den anhkoun sth C
        if (conOfCWithUmax<conOfC ):
            if (type(C) != list):
                C = C.tolist()
            C.append(umax)
        
            #briskw geitones tou umax
            Numax = findNeighboorOfu(G, umax)
        
            #briskw tous geitones tou umax pou den anhkoun sthn C kai tous pros8etw sthn S
            diff = np.setdiff1d(Numax, C)
        
            if (type(S) != list):
                S = S.tolist()
            for i in diff:
                S.append(i)
                
            #briskw ta stoixeia tou S xwris diplotupa
            S = np.unique(S) 
            
        C = np.unique(C)
    

    with open('communities/'+str(myFile)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('communities/'+str(myFile)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm","Node 1", "Node 2", "Multiplied Weight", "Seed node", "Community"])
        
        row = [alg]+[node1]+[node2]+[wName]+[s]+list(C)
#       row = [wName]+[s]+list(C)
        
        writer.writerow(row)

    with open('time/time.txt', 'a') as time_file:
        time_file.write('TCE execution time is:')
        time_file.write(str(time.time() - start_time))
        time_file.write('\n')

