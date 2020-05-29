#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:03:04 2019

@author: georgiabaltsou
"""


import csv

    
    
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply1.5.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*1.5])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply2.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*2])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply2.5.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*2.5])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply3.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*3])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply3.5.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*3.5])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply4.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*4])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply4.5.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*4.5])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply5.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*5])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply5.5.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*5.5])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply6.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*6])
#                
#            
#out_file.close()    
#in_file.close()
#
#with open('netCol.csv', 'r') as in_file:
#    spamreader = csv.reader(in_file, delimiter=';')
#    with open('netColMultiply6.5.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for row in spamreader:
#            out.writerow([row[0],row[1],(float(row[2]))*6.5])
#                
#            
#out_file.close()    
#in_file.close()
with open('netCol/netCol.csv', 'r') as in_file:
    spamreader = csv.reader(in_file, delimiter=';')
    with open('netCol/netColMultiply100.csv', 'w') as out_file:
        out = csv.writer(out_file, delimiter=';')
        
        for row in spamreader:
            out.writerow([row[0],row[1],(float(row[2]))*100])
                
            
out_file.close()    
in_file.close()
