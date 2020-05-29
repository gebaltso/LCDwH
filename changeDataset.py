#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:46:57 2019

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
os.chdir('seperatedExps/datasets/lfr/')

#myFile = 'test.csv'
myFile = 'youtube.csv'
file = myFile[:-4]
counter = 0
my_list = []
outFile = str(file)+'Ref.csv'

        

############################################################################### 

           
with open(myFile) as data_file: 
    reader = csv.reader(data_file, delimiter=';')
                
    with open(outFile, 'a') as out_file:
        writer = csv.writer(out_file, delimiter=';') 
        
        for row in reader:
            newrow1 = [row[0]]
            writer.writerow(newrow1)
            newrow2 = [row[1]]
            writer.writerow(newrow2)
            
with open(outFile,'r') as in_file, open(str(file)+'L.csv','w') as out_file:
    seen = set() 
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)
        
with open(str(file)+'L.csv','r') as in_file:
    reader = csv.reader(in_file, delimiter=';')
    with open(str(file)+'SL.csv', 'a') as out_file:
        writer = csv.writer(out_file, delimiter=';')
    
    
        for row in reader:
            my_list.append(int(row[0]))
        
        my_list.sort()
        
        
        for item in my_list:
            out_file.write("%i\n" % item)

with open(str(file)+'SL.csv', 'r') as in_file:
 with open(str(file)+'Final.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, delimiter=';')
        for row in csv.reader(in_file, delimiter=';'):
            writer.writerow(row+[counter]+[1])
            counter += 1
 

counter = 0         
my_dict = {}

with open(str(file)+'SL.csv', 'r') as in_file:
        for row in csv.reader(in_file, delimiter=';'):
            my_dict[row[0]] = counter
            counter += 1
            


with open(myFile, 'r') as read_file:   
        with open(str(file)+'NewFinal.csv', 'a') as final:
            reader = csv.reader(read_file, delimiter=';')
            writer = csv.writer(final, delimiter=';')
            
            for row in reader:

                if str(row[0]) in my_dict.keys():
                    wrow1 = my_dict[row[0]]

                        
                if str(row[1]) in my_dict.keys():
                    wrow2 =  my_dict[row[1]]
                        
                    
                writer.writerow([wrow1]+[wrow2]+[1])

###############################################################################           
            
#gia pandas. De to xrhsimopoihsa
#                
#df_file = pd.read_csv(myFile, delimiter=';', header=None, names=['A', 'B', 'C'])
#
#len_of_file = len(df_file)
#
#df_lex = pd.read_csv(str(file)+'Final.csv', delimiter=';', header=None, names=['A', 'B', 'C'])
#
#len_of_lex = len(df_lex)
#
#df_final = pd.DataFrame(data=None, columns=df_file.columns,index=df_file.index)
#
#for i in range(0, len_of_file):
#    d1 = 0
#    d2 = 0
#    for j in range(0, len_of_lex):
#
#        if (df_file.iat[i, 0] == df_lex.iat[j, 0]):
#            df_final.iat[i, 0] = (df_lex.iat[j, 1])
#            d1 = 1
#            
#        if (df_file.iat[i, 1] == df_lex.iat[j, 0]):
#            df_final.iat[i, 1] = (df_lex.iat[j, 1])
#            d2 = 1
#            
#        if d1 == 1 and d2 == 1:
#            break
#            
#        df_final.iat[i, 2] = 1
#    
#print(df_final)
# 
 
            
  



              
with open(str(file)+'CommunityFinal.txt', 'r') as in_file:   
    with open(str(file)+'CommunityNewFinal.txt', 'a') as out_file:
        
#        flag = 1
        c = 0
        
        for line in in_file:    #read one line at a time 
            
            item = line.strip().split('\t')
            
            
            for i in item:

#                if flag == 0: 
                if c == len(item)-1:
                    out_file.write(str(my_dict[i])+' '+'\n')
#                    flag = 1
                    
                else:
                    out_file.write(str(my_dict[i])+' ')
                    c += 1
                    
            c = 0
                    
#            flag = 0
        
    

        


 