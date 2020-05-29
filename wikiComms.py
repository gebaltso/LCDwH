#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:48:32 2020

@author: georgiabaltsou
"""

import networkx as nx
import csv
import os
import time
import shutil
import sys
import re
#change dir
os.chdir('seperatedExps/datasets/lfr/')


myFile = 'communityFile0.txt'
outFile = 'communityFile.txt'

lines = []

with open(myFile, 'r+') as comm:

    for line in comm:

        lines.append(re.sub('C.+?;', '', line))
        
        
            
with open(outFile, 'a') as out: 
    out.writelines(lines)          
        
        
        

        
