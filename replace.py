#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:54:52 2019

@author: georgiabaltsou
"""


import os

os.chdir('seperatedExps/datasets/')

myFile = 'youtubeCommunityFinal.txt'
file = myFile[:-4]

with open(str(file)+'NewComm.txt', 'a') as out:
    with open(myFile, 'r') as data:

        plaintext = data.read()


        plaintext2 = plaintext.replace('/t', ' ')
    
    out.write(plaintext2)
    


#print(plaintext)