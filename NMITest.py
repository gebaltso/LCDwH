#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:15:06 2019

@author: georgiabaltsou
"""

from igraph import *

GT = [1,1,1,1,1,1]

C = [2,3,2,1,1,4]

nmi = compare_communities(GT, C, method="nmi")
ari = compare_communities(GT, C, method="ari")
vi = compare_communities(GT, C, method="vi")
rand = compare_communities(GT, C, method="rand")
adjustedRand = compare_communities(GT, C, method="adjusted.rand")
splitJoin = compare_communities(GT, C, method="split.join")

print(nmi, ari, vi, rand, adjustedRand, splitJoin)