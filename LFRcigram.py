#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:24:33 2019

@author: georgiabaltsou
"""

from cigram import lfr_benchmark_graph

params = {
    'n': 10000,
    'average_degree': 10,
    'max_degree': 1000,
    'mu': 0.5,
    'tau': 2.0,
    'tau2': 2.0,
    'minc_size': 3,
    'maxc_size': 1000,
    'overlapping_nodes': 0,
    'overlapping_memberships': 1,
    'seed': 1337
}

graph, comms = lfr_benchmark_graph(**params)