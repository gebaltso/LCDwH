#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:34:10 2019

@author: georgiabaltsou
"""

with open('lemon_Alg/example/dblp/community.txt') as fin, open('lemon_Alg/example/dblp/newCom.txt', 'w') as fout:
    for line in fin:
        fout.write(line.replace('\t', ','))
        
with open('lemon_Alg/example/dblp/newCom.txt') as fin, open('lemon_Alg/example/dblp/newCom2.txt', 'w') as fout:
    for line in fin:
        fout.write(line.replace(',', ' '))