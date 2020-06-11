#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:21:33 2019

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
    
    return set(G.neighbors(u))

def CONDUCTANCE(G, C, Gdict):  
    
    cut = nx.cut_size(G,C, weight='weight')    
    
    vol = nx.cuts.volume(G, C, weight='weight')
    
    if(vol==0): return 0
      
    conductance = cut/vol

    return conductance


#upologismos tou deg ston paronomasth tou edge score
def deg(u, N, G, Gdict):
    deg = 0
    
    
    for i in N:
        w = G.get_edge_data(u, i)
#        wei = float(Gdict[u][i])
        
        deg += w['weight']
#        deg += wei
          
    return deg


#upologismos tou edge score
def SCORE(u, C, G, Gdict):
        
    #geitones Nu
    Nu = findNeighboorOfu(G,u)
    
    #briskw thn tomh sthn opoia anhkei o komvos v    
#    V = np.intersect1d(C, Nu)
    V = Nu.intersection(set(C))

    
    #krataw ta edgeScores ka8e komvou pou anhkei sto V        
    sumOfEdgeScore = 0

    #baros metaksu u kai v
    wuv = 0

    for v in V:
                
        #w(u,v)       
        w = G.get_edge_data(u, v)
#        wuv = float(Gdict[u][v])
        wuv = w['weight']

        #geitones tou v
        Nv = findNeighboorOfu(G,v)
        
        #X h tomh geitonwn u me geitones tou v
#        X = np.intersect1d(Nv, Nu)
        X = Nv.intersection(Nu)


        sumOfMin = 0
        for x in X:
            w1 = G.get_edge_data(u, x)
            ux = w1['weight']
            w2 = G.get_edge_data(v, x)
            vx = w2['weight']
#            ux = float(Gdict[u][x])
#            vx = float(Gdict[v][x])
  
            sumOfMin += (min(ux, vx))
           
        
        #o ari8mhths tou klasmatos tou edge score
        nominator = wuv + sumOfMin
        
        degu = deg(u, Nu, G, Gdict)
        degv = deg(v, Nv, G, Gdict)
        
        denominator = min(degu, degv)
        
        sumOfEdgeScore += (nominator/denominator)
    
    
    score = ((1/len(Nu))*(sumOfEdgeScore))
        
    return score

def tce(G, seedsetFile, file, Gdict, myFile, bdict, method,l):
    # main program
    
#    print(G.edges.data())
    
    start_time = time.time()
    
    alg = 'tce'
    
    seedFile = open(seedsetFile, 'r')
    seeds = seedFile.readline().rstrip('\n').split(" ")
    lenS = len(seeds)
    
    
    # arxikopoihsh se 0 ths koinotitas C
    C = []  
#    C = {}
#    C.append(s)
    
    #sunolo twn geitwnwn
#    S = findNeighboorOfu(G, s)
    #xrhsimopoieitai mono gia th diaforopoihsh tou score
    #firstS = S
    
    # arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
    SInitial = []
#    S = {}
    
    # arxikopoihsh ths seed list
    global s
    s = []
    
    for i in range(lenS):
        C.append(seeds[i])
        s.append(seeds[i])
        SInitial.append(findNeighboorOfu(G, seeds[i]))

#        S = Gdict[seeds[i]]
#        S.values() = 0
#       
    #conductance of C
    conOfC = CONDUCTANCE(G, C, Gdict)
    
    # Make list of lists one list    
    S = [val for sublist in SInitial for val in sublist]
#    Sset = set()
#    for item in S:
#        Sset.add(S[i])
 
    score_array = {}
#    curmax = 0
    
    for u in S:
#        curscore = SCORE(u, S, C, G, Gdict)
#        if curscore > curmax:
#            score_array.clear()

            score_array[u] = SCORE(u, C, G, Gdict)
#            curmax = curscore
     
    while len(score_array)>0  and len(C)<l:
    
        #pinakas me ta scores twn stoixeiwn tou S
#        score_array = []
#        score_array = {}
#        curmax = 0
#        for u in S:
##            score_array.append(SCORE(u, S, C, G, Gdict))
#            curscore = SCORE(u, S, C, G, Gdict)
#            if curscore > curmax:
#                score_array.clear()
#                score_array[u] = SCORE(u, S, C, G, Gdict)
#                curmax = curscore
        
        #briskw to maximum score apo ta scores twn S
#        maxScore = np.amax(score_array)
            
        #briskw th 8esh tou maxScore
#        index = score_array.index(maxScore)
            
        #briskw ton komvo me to max score
#        umax = S[index]
        
        umax = max(score_array, key=score_array.get)
#        print("S=", S)
#        print("umax=", umax)
#        print("SCORE= ", score_array)
        
#        print("SCORE=", score_array)

#        umax = [k for k,v in score_array.items() if v == curmax]
#        print(umax)
        
        
        #afairw apo to S ton komvo me to max score 
#        if (type(S) != list):
#            S = S.tolist()
#        if umax in S:
#        print("S=", S)
#        print("umax=", umax)
#        S.remove(umax)
#        print("S=", S)
        score_array.pop(umax)
#        #conductance of C
#        conOfC = CONDUCTANCE(G, C, Gdict)
        
        CWithU = []
        for i in C:
            CWithU.append(i)
        CWithU.append(umax)
            
        #conductance of C with umax
        conOfCWithUmax = CONDUCTANCE(G, CWithU, Gdict)
        
        #an isxuei h sun8hkh pros8etw ton umax sthn C ki episis pros8etw sto S tous geitones tou umax pou den anhkoun sth C
        if (conOfCWithUmax<conOfC):
#            if (type(C) != list):
#                C = C.tolist()
            C.append(umax)
#            pbar.update(1)
            conOfC = conOfCWithUmax
            
#            del score_array[umax]
            
            #allazw to grafhma wste na pros8esw ton umax me tis geitniaseis tou
#            os.chdir('/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/')
#            with open(myFile, 'r') as read_file: 
#                reader = csv.reader(read_file, delimiter=';')
#                for row in reader:
#                    if (row[0]==umax   or row[1]==umax):
#                        try:
#                            x = Gdict[row[0]][row[1]]
#                        except KeyError:
#                            Gdict[row[0]][row[1]] = row[2] 
#                            Gdict[row[1]][row[0]] = row[2]
#            G = nx.Graph(Gdict)
                       
#            for key1 in bdict.keys():
#                for key2 in bdict[key1].keys():
#                    if key1==umax or key2==umax:
#                        try:
#                            x = Gdict[key1][key2]
#                        except KeyError:
#                            Gdict[[key1][key2]] =  bdict[[key1][key2]]
#                            Gdict[[key2][key1]] = bdict[[key1][key2]]
#            G = nx.Graph(Gdict)
            
            #allazw to grafhma wste na pros8esw ton umax me tis geitniaseis tou
            Gdict[umax] = bdict[umax]
#            G = nx.Graph(Gdict)
                  
            #briskw geitones tou umax
            Numax = findNeighboorOfu(G, umax)

        
            #briskw tous geitones tou umax pou den anhkoun sthn C kai tous pros8etw sthn S
#            diffC = list(np.setdiff1d(Numax, C))
            diffC = Numax - set(C)
#            diff = np.setdiff1d(diffC, list(score_array.keys()))
            diff = diffC - set(score_array.keys())


            for j in diff:
                score_array[j] = SCORE(j, C, G, Gdict)
        
#            if (type(S) != list):
#                S = S.tolist()
#            for i in diff:
#                S.append(i)
#                
#            #briskw ta stoixeia tou S xwris diplotupa
#            S = list(np.unique(S))
                
#            print("C=", C)
            
        
#        pbar.close()    
        C = list(np.unique(C))
        
    print("TCE time: ", time.time() - start_time)
    
    with open('./communities/'+str(file)+'_communities.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('./communities/'+str(file)+'_communities.csv').st_size == 0:
            writer.writerow(["Algorithm", "Seed node", "Method", "Community"])
        
#        row = [alg]+[node1]+[node2]+[wName]+[s]+list(C)
#       row = [wName]+[s]+list(C)
        row = [alg] + ["\n".join(seeds)] + [method] + list(C)
        
        writer.writerow(row)


