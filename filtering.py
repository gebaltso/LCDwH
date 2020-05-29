#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:59:55 2018

@author: georgiabaltsou
"""

import csv


def sortFile(inputFile, outputFile):

    csv_lines = []
    # read csv
    with open(inputFile, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            csv_lines.append(row)
    
    # sort by 3rd column. - is for descending order.
    csv_lines_sorted = sorted((r for r in csv_lines if len(r) > 1), key=lambda r: (-float(r[2])))
    
    number_of_rows = len(csv_lines_sorted)
    print("Number of rows is: ", number_of_rows)
       
    # write csv
    with open(outputFile, 'wt') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', lineterminator='\n')
        for row in csv_lines_sorted:
            writer.writerow(row)
#        writer.writerows(csv_lines_sorted)
        
        
def maxValues(outputFile, outputFile2):
    
    with open(outputFile, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        with open(outputFile2, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            
            counter = 1
            
            for row in reader:
                writer.writerow([row[0],row[1], row[2]])
                counter += 1
                if(counter == 51):
                    break;

#krataw tis akmes opou plhroun ena krithrio

#cosine
#with open('outputCosineFinal.csv', 'r') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=';')
#    with open('filteredOutputCos.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        for row in spamreader:
#            if float(row[2]) < 0.2:
#                continue
#            else:
#                out.writerow([row[0],row[1], row[2]])
                                
                
##Euclidean
#with open('outputEucl.csv', 'r') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=';')
#    with open('filteredOutputEucl.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        for row in spamreader:
#            if float(row[2]) > 2:
#                continue
#            else:
#                out.writerow([row[0],row[1], row[2]])


#Pearson
#with open('outputPearson.csv', 'r') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=';')
#    with open('filteredOutputPearson.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        for row in spamreader:
#            if float(row[2]) < 0.3: #between 0.3 and 0.7 moderate positive correlation
#                continue
#            else:
#                out.writerow([row[0],row[1], row[2]])


#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/outputPearson.csv', 'r') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=';')
#    with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/filteredPearson2.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        firstGene = next(spamreader)[0] #first gene of the file
#        
#        for row in spamreader:
#                     
#            if(row[0]==firstGene):
#            
#                if float(row[2]) < 0.3: #between 0.3 and 0.7 moderate positive correlation
#                    continue
#                else:
#                    out.writerow([row[0],row[1], row[2]])



with open('naderi2007Final2.csv') as data_file: 
    lines = data_file.readlines()
  

#genes = []
#for line in lines:
#    data = line.split(';')
#    genes.append(data[0])
#      
##print(genes)
#print(len(genes))
#    
#
#
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/outputPearson.csv', 'r') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=';')
#    with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/filteredPearson3.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#
#        firstGene = genes[0] #first gene of the file
#        
#        for row in spamreader:
#  
#                     
#            if(row[0]==firstGene):
#                
#                out.writerow([row[0],row[1],float(row[2])])
##                if float(row[2]) < 0.3: #between 0.3 and 0.7 moderate positive correlation
##                    continue
##                else:
##                    out.writerow([row[0],row[1],float(row[2])])
                    
                    
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/outputPearson.csv', 'r') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=';')
#    with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/filteredPearsonNew.csv', 'w') as out_file:
#        out = csv.writer(out_file, delimiter=';')
#        
#        for _ in range(16941):
#            next(spamreader)
#
#        firstGene = next(spamreader)[0] #first gene of the file
#        
#        for row in spamreader:
#                     
#            if(row[0]==firstGene):
#           
#                out.writerow([row[0],row[1],float(row[2])])
                    
#                if float(row[2]) < 0.3: #between 0.3 and 0.7 moderate positive correlation
#                    continue
#                else:
#                    out.writerow([row[0],row[1],float(row[2])])


inputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/filteredPearson3.csv'
outputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/filteredPearson4.csv'
outputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/filteredPearson5.csv'

#sort the input file in a descending order of distances resulting to output file
#sortFile(inputFile, outputFile)

maxValues(outputFile, outputFile2)




