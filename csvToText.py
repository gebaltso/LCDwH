#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:10:50 2019

@author: georgiabaltsou
"""

import csv
import os





def csvToText(csv_file, txt_file):

#csv_file = 'new.csv'
#txt_file = 'new'


    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
        
     
    #replace ; with space
    with open(txt_file, 'r') as f:
        lines = f.readlines()
    
    
    lines = [line.replace(';', ' ') for line in lines]
    
    
    with open(txt_file, 'w') as f:
        f.writelines(lines)
        
    return txt_file

os.chdir('/Users/georgiabaltsou/Desktop/')
csvToText('/Users/georgiabaltsou/Desktop/lfrnew4.csv', 'lfrnew4.txt')