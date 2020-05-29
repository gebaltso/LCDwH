#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:14:38 2020

@author: georgiabaltsou
"""

import re


txt_file = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/infomap/newman.txt'
new_txt = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/newman.txt'
final_txt = '/Users/georgiabaltsou/Desktop/Datasets/CondensedMatterArxiv/1995-2005/infomap/finanewman.txt'

listInfo = []

with open(txt_file, 'r') as in_file:
#    stripped = (line.strip() for line in in_file)
#    lines = (line.split(" ") for line in stripped if line)  #change split to "\t" for tabbed txt file
    
    for line in in_file:

        listInfo.append(re.findall(r'"(.*?)"', line)) 

       
with open(new_txt, 'w') as out_file:
        for item in listInfo:
            out_file.write("%s\n" % item)
            
with open(new_txt, 'r') as infile, \
     open(final_txt, 'w') as outfile:
    data = infile.read()
    data = data.replace("'", "")
    data = data.replace("[", "")
    data = data.replace("]", "")
    outfile.write(data)