#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:15:15 2019

@author: georgiabaltsou
"""

import sys

adjacency_list_filename = "lemonTEST/datasets/lfr/lfrAdjlistN1000MU0.1*.txt"
edge_list_filename = "lemonTEST/datasets/lfr/lfrEdgelistN1000MU0.1*.txt"

edge_list = []
with open(adjacency_list_filename, 'r') as f:
    for line in f:
        
        if line.startswith("#"):
            continue;
        else:

            line = line.rstrip('\n').split(' ')
            source = line[0]
            for target in line[1:]:
                edge_list.append("%s %s" % (source, target)) #1 is for the weight

with open(edge_list_filename, 'w') as f:
    f.write('%s\n' % ('\n'.join(edge_list)))