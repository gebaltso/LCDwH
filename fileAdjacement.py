#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:29:49 2019

@author: georgiabaltsou
"""

import csv
import os

def weightedFiles(myFile, GTC):
    #creation of weighted files from different seed each time
    for index, i in enumerate(GTC):
#        FileAdj(myFile, i)
        FilesAdj(myFile, i, GTC, index)

def FileAdj(myFile, s):

    counter = 1
        
    #change counter to <=10 for more weights
    while(counter<=10):
    
        with open(myFile) as data_file: 
            reader = csv.reader(data_file, delimiter=';')        
            with open('weighted/'+str(myFile)+'<'+str(s)+'-'+' '+'>'+str(counter)+'.csv', 'a') as out_file:
                writer = csv.writer(out_file, delimiter=';')
                
                for row in reader:
                    w = 1
                    if ((row[0] == s) or (row[1] == s)):
                        w *= counter  
                    writer.writerow([row[0],row[1], w])
                    
                counter += 1
                                      
                    
def FilesAdj(myFile, s, GTC, index):
                                     
    for j in GTC[index:]:       
        if s==j: continue
    
        counter2 = 1
        #change counter to <=10 for more weights
        while(counter2<=10):
            if counter2 == 1:
                counter2 += 1
                continue

            with open('lfr/'+str(myFile)) as data_file: 
                reader = csv.reader(data_file, delimiter=';')
                
                os.chdir('../weighted/')
                
                with open(str(myFile)+'<'+str(s)+'-'+str(j)+'>'+str(counter2)+'.csv', 'a') as out_file:
                    writer = csv.writer(out_file, delimiter=';')
                        
                    
                    for row in reader:
                        w = 1
                        if ((row[0] == s) or (row[1] == s) or (row[0] == j) or (row[1] == j)):
                            w *= counter2 
                        writer.writerow([row[0],row[1], w])
                            
                    counter2 += 1 

                os.chdir('../')                      
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        