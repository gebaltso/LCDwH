#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:23:48 2019

@author: georgiabaltsou
"""

#2017-Michael Hamann,Eike Röhrs and Dorothea Wagner- 
#Local Community Detection Based on Small Cliques
#For Unweighted graphs


import networkx as nx
import numpy as np 


def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    return neighbors

def CONDUCTANCE(G, C):  
    
    #cut
    cut = nx.cut_size(G, C)
    #print("cut =", cut)
    
    #bazei epipleon mia fora to metaksu 3 kai 11 baros
    vol = nx.cuts.volume(G, C)
    #print("vol =", vol)

    conductance = cut/vol
    #print("Conductance =", conductance)

    return conductance


#upologismos tou deg
def deg(u):
    deg = G.degree(u)
      
    return deg


#upologismos tou edge score
def SCORE(u, S, C):
        
    #geitones Nu
    Nu = findNeighboorOfu(G,u)
    
    #briskw thn tomh sthn opoia anhkei o komvos v    
    V = np.intersect1d(C, Nu)
    
    
    #krataw ta edgeScores ka8e komvou pou anhkei sto V        
    sumOfEdgeScore = 0


    for v in V:
                

        #geitones tou v
        Nv = findNeighboorOfu(G,v)
        
        #X h tomh geitonwn u me geitones tou v
        X = np.intersect1d(Nv, Nu)
        
        #briskw to |Nu tomi Nv|+1
        #o ari8mhths tou klasmatos tou edge score
        nominator = len(X) + 1

       
        degu = deg(u)
        degv = deg(v)
        
        denominator = min(degu-1, degv-1)
        
        if(denominator ==0):
            denominator = 0.00000000000000001
        
        sumOfEdgeScore += (nominator/denominator)
    
    #an o komvos einai kapoios apo autous pou 8ewrw shmantikous tote diplasiase to score
    if u in firstS:
        score = 100 * ((1/len(Nu))*(sumOfEdgeScore))
    else:
        score = ((1/len(Nu))*(sumOfEdgeScore))
    
    #score = ((1/degu)*(sumOfEdgeScore))
        
    return score

# main program

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
#G = nx.read_edgelist("karateUnw.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("adjnoun.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("email/email.csv", create_using=nx.Graph(), delimiter=";")
#G = nx.read_edgelist("football/football.csv", create_using=nx.Graph(), delimiter=";")
G = nx.read_edgelist("dblp/dblp.csv", create_using=nx.Graph(), delimiter=";")

print("Graph Created")

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
#s = '2'
#s = '319507'
s = '269383'

#GTC = ['2', '3', '4', '56', '57', '58', '59', '63', '137', '138', '192', '193', '194', '195', '281', '286', '305', '408', '412', '456', '520', '532', '571', '586', '587', '606', '622', '625', '633', '634', '635', '636', '648', '670', '685', '691', '711', '718', '755', '762', '774', '803', '815', '826', '832', '845', '849', '863','865', '880', '882', '884', '899', '901', '921', '928', '982', '990', '993', '994', '1001' ]


C.append(s)

#sunolo twn geitwnwn
S = findNeighboorOfu(G, s)
#xrhsimopoieitai mono gia th diaforopoihsh tou score
firstS = S

while len(S)>0:

    #pinakas me ta scores twn stoixeiwn tou S
    score_array = []
    for u in S:
        score_array.append(SCORE(u, S, C))
    
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
    print("newC =", C)

print("-----------------------------------")
print("Community =", C)
