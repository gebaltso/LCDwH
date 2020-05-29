#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:23:27 2019

@author: georgiabaltsou
"""

import csv



def row_count(inputF):
    with open(inputF) as f:
        for i, l in enumerate(f):
            pass
    return i

inputF = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/youtubeL.csv'

print(row_count(inputF))