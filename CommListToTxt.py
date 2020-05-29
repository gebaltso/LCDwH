#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:07:04 2019

@author: georgiabaltsou
"""


"from nodename communityname form to community members per row form "

#filename = '/Users/georgiabaltsou/Desktop/PhD/Local_exp/seperatedExps/datasets/lfr/emailComm.txt'
filename = '/Users/georgiabaltsou/Desktop/football/community.txt'

communities = {}

with open(filename) as f:
    for line in f:
        row = line.split()
        node = int(row[0])
        community = int(row[1])
        communities.setdefault(community, []).append(node)
                     
#print(communities)


with open('/Users/georgiabaltsou/Desktop/football/communityFile.txt','w') as log:
    for value in communities.values():
        log.write('{}\n'.format(value))
        
with open('/Users/georgiabaltsou/Desktop/football/communityFile.txt', 'r') as my_file:
        text = my_file.read()
        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace(",", "")
        
with open('/Users/georgiabaltsou/Desktop/football/communityFile.txt', 'w') as my_file:
            
        my_file.write(text)
        
            
            


        
        
        
        
        
        
        
        

        
