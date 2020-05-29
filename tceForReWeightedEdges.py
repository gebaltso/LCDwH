#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:43:18 2019

@author: georgiabaltsou
"""

#2017-Michael Hamann,Eike Röhrs and Dorothea Wagner- 
#Local Community Detection Based on Small Cliques



import networkx as nx
import numpy as np 
import csv
import os


def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors

def CONDUCTANCE(G, C):  
    
    #cut
    cut = nx.cut_size(G,C, weight='weight')
    #print("cut =", cut)
    
    #bazei epipleon mia fora to metaksu 3 kai 11 baros
    vol = nx.cuts.volume(G, C, weight='weight')
    #print("vol =", vol)

    conductance = cut/vol
    #print("Conductance =", conductance)

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
        #minW = []
#        for x in X:
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
    
    #an o komvos einai kapoios apo autous pou 8ewrw shmantikous tote diplasiase to score
#    if u in firstS:
#        score = 10 * ((1/len(Nu))*(sumOfEdgeScore))
#    else:
#        score = ((1/len(Nu))*(sumOfEdgeScore))
    
    score = ((1/len(Nu))*(sumOfEdgeScore))
        
    return score

def tce(file, s, myFile):
    # main program
    
#    node1 = file.split("<")[1].split("-")[0]
#    
#    node2 = file.split("-")[1].split(">")[0]
#    
#    wName = file.split(">")[1].split(".")[0]
    
    G = nx.Graph()
    #G = nx.read_weighted_edgelist("myFile.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("filteredOutputEucl.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("filteredOutputCos.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("finalGeneFilePearson.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("finalGeneFileCosine.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("finalGeneFileEuclidean.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("pearsonSupera.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("/Volumes/Georgia/Έγγραφα/PhD/Local_exp/finalGenes/finalAbsPearson/final160GeneAbsFilePearson.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("karate.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("karateChanged1Seed10.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("netCol.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("netCol/netCol.csv", create_using=nx.Graph(), delimiter=";")
    #G = nx.read_weighted_edgelist("dblp/dblpWeighted.csv", create_using=nx.Graph(), delimiter=";")
    G = nx.read_weighted_edgelist(file, create_using=nx.Graph(), delimiter=";")
    
    #print("Edges: ", G.number_of_edges()) # 2671753
    #print("Nodes: ", G.number_of_nodes())  # 16943
    
    # arxikopoihsh se 0 ths koinotitas C
    C = []
    
    # arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
    N = []
    
    # step 1
    #s = 'supera'
    #s = 'amputation'
    #s = 'smoking'
    #s = 'A_23_P251480' #ΝΒΝ gene
    #s = 'A_23_P149050'
    #s = '78' #Newman
    #s = '281' #Sole
    #s = '18323' #dblp
    #s = '269383'
    
    
    C.append(s)
    
    #sunolo twn geitwnwn
    S = findNeighboorOfu(G, s)
    #xrhsimopoieitai mono gia th diaforopoihsh tou score
    #firstS = S
    
    while len(S)>0:
    
        #pinakas me ta scores twn stoixeiwn tou S
        score_array = []
        for u in S:
            score_array.append(SCORE(u, S, C, G))
        
        #briskw to maximum score apo ta scores twn S
        maxScore = np.amax(score_array)
        
        #print("maxScore =", maxScore)
            
        #briskw th 8esh tou maxScore
        index = score_array.index(maxScore)
            
        #briskw ton komvo me to max score
        umax = S[index]
    #    print("umax =", umax)
        
        #afairw apo to S ton komvo me to max score 
        if (type(S) != list):
            S = S.tolist()
        S.remove(umax)
        #print("S : ", S)
        
        #conductance of C
        conOfC = CONDUCTANCE(G, C)
    #    print("Cond C =", conOfC)
        
        CWithU = []
        for i in C:
            CWithU.append(i)
        CWithU.append(umax)
            
        #conductance of C with umax
        conOfCWithUmax = CONDUCTANCE(G, CWithU)
    #    print("Cond with umax =", conOfCWithUmax)
        
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
    #    print("newC =", C)
    
#    print("-----------------------------------")
#    print("Number of nodes in C: ", len(C))
#    print("Community =", C)
    

    with open('communities/tce_communities'+str(myFile)+'.csv', 'a') as out_file:
              
        writer = csv.writer(out_file, delimiter=';')
        
        if os.stat('communities/tce_communities'+str(myFile)+'.csv').st_size == 0:
#            writer.writerow(["Node 1", "Node 2", "Multiplied Weight", "Community"])
            writer.writerow(["Seed Node", "Community"])
        
#        row = [node1]+[node2]+[wName]+[s]+list(C)
        row = [s]+list(C)
        
        writer.writerow(row)



#counter = 0
#
#comm = ['18323', '146590', '240098', '249900', '269383', '319507', '319508', '337203', '339699', '348984', '349177']
#
#for i in C:
#    if i in comm:
#        counter += 1
#
#print("nodes of ground truth in C: ", counter)
