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
    
#    number_of_rows = len(csv_lines_sorted)
#    print("Number of rows is: ", number_of_rows)
       
    # write csv
    with open(outputFile, 'wt') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', lineterminator='\n')
        for row in csv_lines_sorted:
            writer.writerow(row)
#        writer.writerows(csv_lines_sorted)
        
        
def maxValues(inputFile2, outputFile2):
    
    with open(inputFile2, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        with open(outputFile2, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            
            counter = 1
            
            for row in reader:
                writer.writerow([row[0],row[1], row[2]])
                counter += 1
                if(counter == 161): #51 arxika
                    break;



#####################################################################################
# 1 Creation of genes list which contains the 16943 different genes of the dataset
#with open('naderi2007Final2.csv') as data_file: 
#    lines = data_file.readlines()
#  
#genes = []
#for line in lines:
#    data = line.split(';')
#    genes.append(data[0])
#      
###print(genes)
#print(len(genes))
    
######################################################################################
# 2 Creation of 16943 different files each containing a different gene and its neighbors
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/outputsMetrics/outputPearson.csv', 'r') as csvfile:
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/outputsMetrics/outputCosine.csv', 'r') as csvfile:
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/outputsMetrics/outputEuclidean.csv', 'r') as csvfile:
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/absPearsonInputFile.csv', 'r') as csvfile:
#    
#    spamreader = csv.reader(csvfile, delimiter=';')
#    
#    counter = 0
#    
#    for i in genes:
#        
##        with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fPearson'+str(counter)+'.csv', 'a') as out_file:
##        with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fCosine'+str(counter)+'.csv', 'a') as out_file:
##        with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fEuclidean'+str(counter)+'.csv', 'a') as out_file:
#         with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/absPearson/fabsPearson'+str(counter)+'.csv', 'a') as out_file:
#  
#            out = csv.writer(out_file, delimiter=';')
#          
#            for row in spamreader:
#     
#                if(row[0]==i):
#
#                    out.writerow([row[0],row[1],float(row[2])])
#                    
#                else:
##                    with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fPearson'+str(counter+1)+'.csv', 'a') as out_file:
##                    with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fCosine'+str(counter+1)+'.csv', 'a') as out_file:
##                    with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fEuclidean'+str(counter+1)+'.csv', 'a') as out_file:
#                    with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/absPearson/fabsPearson'+str(counter)+'.csv', 'a') as out_file:
#                        out = csv.writer(out_file, delimiter=';')
#                        out.writerow([row[0],row[1],float(row[2])])
#                        break
#            
#            counter += 1
 
           
                    
#####################################################################################
# 3 Sort the above generated files
#for i in range(0, 16943):
##    inputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fPearson'+str(i)+'.csv'
##    outputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/sortedGenes/sortedPearson'+str(i)+'.csv'
#    
##    inputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fCosine'+str(i)+'.csv'
##    outputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/sortedGenes/sortedCosine'+str(i)+'.csv'
#    
##    inputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/fEuclidean'+str(i)+'.csv'
##    outputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/sortedGenes/sortedEuclidean'+str(i)+'.csv'   
#    
#    inputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedGenes/absPearson/fabsPearson'+str(i)+'.csv'
#    outputFile = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/sortedGenes/sortedAbsPearson/sortedabsPearson'+str(i)+'.csv'
#    
#    sortFile(inputFile, outputFile)

#####################################################################################
# 4 Find the top max 50 neighbors of the sorted genes considering the weights
#for i in range(0, 16943):
##    inputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/sortedGenes/sortedPearson'+str(i)+'.csv'
##    outputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/maxGenes/maxPearson'+str(i)+'.csv'
#    
##    inputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/sortedGenes/sortedCosine'+str(i)+'.csv'
##    outputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/maxGenes/maxCosine'+str(i)+'.csv'
#    
##    inputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/sortedGenes/sortedEuclidean'+str(i)+'.csv'
##    outputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/maxGenes/maxEuclidean'+str(i)+'.csv'
#    
#    inputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/sortedGenes/sortedAbsPearson/sortedabsPearson'+str(i)+'.csv'
#    outputFile2 = '/Volumes/Georgia/Έγγραφα/PhD/Local_exp/maxGenes/maxAbsPearson/maxabsPearson'+str(i)+'.csv'
#    
#    maxValues(inputFile2, outputFile2)    
    
    
#####################################################################################
# 5 Write the above max values in a final csv file to be used as the dataset
    
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/finalGenes/finalGeneFilePearson.csv', 'a') as out_file:
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/finalGenes/finalGeneFileCosine.csv', 'a') as out_file:
#with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/finalGenes/finalGeneFileEuclidean.csv', 'a') as out_file:
with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/finalGenes/finalAbsPearson/final160GeneAbsFilePearson.csv', 'a') as out_file:
  
    writeFile = csv.writer(out_file, delimiter=';')
    
    for i in range(0, 16943):
#        with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/maxGenes/maxPearson'+str(i)+'.csv', 'r') as in_file:
#        with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/maxGenes/maxCosine'+str(i)+'.csv', 'r') as in_file:
#        with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/maxGenes/maxEuclidean'+str(i)+'.csv', 'r') as in_file:
        with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/maxGenes/maxAbsPearson/maxabsPearson'+str(i)+'.csv', 'r') as in_file:
            
            readFile = csv.reader(in_file, delimiter=';')
            
            for row in readFile:
                writeFile.writerow([row[0],row[1],float(row[2])])
    
    
    
    
    
    
    
    

