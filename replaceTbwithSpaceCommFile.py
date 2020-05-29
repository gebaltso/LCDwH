#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:32:38 2019

@author: georgiabaltsou
"""


import networkx as nx
import os
import time
import shutil
import sys
import csv
import pandas as pd



#change dir
os.chdir('dblp/')


with open('dblpComm.txt', 'r') as in_file:   
    with open('dblpCommFinal.txt', 'a') as out_file:
        
#        flag = 1
        c = 0
        
        for line in in_file:    #read one line at a time 
            
            item = line.strip().split('\t')
            
            
            for i in item:

#                if flag == 0: 
                if c == len(item)-1:
                    out_file.write(str(i)+' '+'\n')
#                    flag = 1
                    
                else:
                    out_file.write(str(i)+' ')
                    c += 1
                    
            c = 0