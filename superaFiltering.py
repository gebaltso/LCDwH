#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:50:19 2019

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
                if(counter == 7):
                    break;



#####################################################################################
# 1 Creation of disease list which contains the 25 different diseases/attributes of the dataset
                    
diseases=['supera', 'age', 'male_gender', 'diabetes', 'hypertension', 'hyperlipidemia', 'smoking', 'renal_disease', 'ischemic_heart_disease', 'rutherford_stage', 'popliteal', 'subintimal', 'occlusion_length', 'baseline_runoff', 'completion_runoof', 'stent_diameter', 'stent_length', 'dapt;, ;anticoagulation', 'restenosis', 'recurrence', 'tlr', 'amputation', 'death', 'male_events']


######################################################################################
# 2 Creation of 25 different files each containing a different disease/attribute and its neighbors
with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/outputsMetrics/pearsonSupera.csv', 'r') as csvfile:

    
    spamreader = csv.reader(csvfile, delimiter=';')
    
    counter = 0
    
    for i in diseases:
        
        
        
        with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedDiseases/sPearson'+str(counter)+'.csv', 'a') as out_file:
  
            out = csv.writer(out_file, delimiter=';')
            
            for row in spamreader:
                
                
                if(row[0]==i):
 
                    out.writerow([row[0],row[1],float(row[2])])
                    
                else:
                    
                    with open('/Volumes/Georgia/Έγγραφα/PhD/Local_exp/seperatedDiseases/sPearson'+str(counter+1)+'.csv', 'a') as out_file:
                        out = csv.writer(out_file, delimiter=';')
                        out.writerow([row[0],row[1],float(row[2])])
                        break
            
            counter += 1
 
           




                   
                    
                    
