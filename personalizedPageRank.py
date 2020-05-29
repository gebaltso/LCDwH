!#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:09:37 2019

@author: georgiabaltsou
"""

import networkx as nx
from operator import itemgetter
from collections import OrderedDict

def ppr(g, seed, alpha=0.85, epsilon=10e-8, iters=100):
    pref = {}
    T = [seed]
    for node in g.neighbors(seed):
        T.append(node)
    for node in g:
        if node in T: 
            pref.update({node:(1.0 / len(T))})
        else:
            pref.update({node:0.0})
            
    return nx.pagerank(g, alpha=alpha, personalization=pref, max_iter=iters,
                tol=epsilon)

def ppr_sorted(g, pprv):
    spprv = {}
    for item in pprv.items():
        k, v = item
        spprv.update({k:(v/g.degree(k))})
        pass
    return sorted(spprv.items(), key=itemgetter(1), reverse=True)

def min_cond_cut(g, dspprv, max_cutsize=0):
    
    def conductance(nbunch):
        sigma = 0.0
        vol1 = vol2 = 0
        for node in nbunch:
            for n in g.neighbors(node):
                if n not in nbunch:
                    sigma += 1.0
                    
        for degseq in g.degree().dict.items():
            node, degree = degseq
            if node not in nbunch:
                vol2 += degree
            else:
                vol1 += degree
                
        return (sigma / min(vol1, vol2))
    
    k = 1
    conductance_list = []

    if max_cutsize < 1:
        # cutsize could be as big as the graph itself
        limit = (len(dspprv))
    else:
        # maximum size of the cut with minimum conductance 
        limit = max_cutsize
        
    while k < limit :
        nbunch = []
        for i in range(0, k):
            nbunch.append(dspprv[i][0])
            
        c = (k, conductance(nbunch))
        # conductane of current cut size
        print(c)
        conductance_list.append(c)
        k += 1

    return min(conductance_list, key=itemgetter(1))

## running the code ..
def loadGraph(gfile):
    return nx.read_edgelist(path=gfile, comments='#',
                            delimiter="\t", nodetype=int)

g = loadGraph(gfile='com-dblp.ungraph.txt')
a = ppr(g, seed=2, alpha=0.85, epsilon=10e-8, iters=100)
b = ppr_sorted(g, pprv=a)
# finding the best community around NodeId==5
print(min_cond_cut(g, dspprv=b, max_cutsize=10))