#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:25:08 2019

@author: georgiabaltsou
"""

import networkx as nx
from typing import *
import numpy as np
from .approximate_PageRank import approximate_PageRank


def PageRank_nibble(g,ref_nodes,
                    vol: float = 100,
                    phi: float = 0.5,
                    method: str = 'acl',
                    epsilon: float = 1.0e-2,
                    iterations: int = 10000,
                    timeout: int = 100,
                    ys: Sequence[float] = None, 
                    cpp: bool = True):
    
    n = g.adjacency_matrix.shape[0]
    nodes = range(n)
    
    m = g.adjacency_matrix.count_nonzero()/2
    
    B = np.log2(m)
    
    if vol < 0:
        print("The input volume must be non-negative")
        return [], [], [], [], []
    if vol == 0:
        vol_user = 1
    else:
        vol_user = vol
    
    b = 1 + np.log2(vol_user)
    
    b = min(b,B)
    
    alpha = (phi**2)/(225*np.log(100*np.sqrt(m)))
    
    rho = (1/(2**b))*(1/(48*B))
    
    p = approximate_PageRank(g, ref_nodes, timeout = timeout, iterations = iterations, alpha = alpha,
                                 rho = rho, epsilon = epsilon, ys = ys, cpp = cpp, method = method)
    
    
    return p



###########MAIN################
    
g = nx.Graph()

g = nx.read_edgelist("karateUnw.csv", create_using=nx.Graph(), delimiter=";")


ref_nodes = '34'

print(PageRank_nibble(g,ref_nodes, 100, 0.5, 'acl', 1.0e-2, 10000, 100, None, True))











