#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:00:31 2020

@author: georgiabaltsou
"""

import os
import csv

os.chdir('seperatedExps/datasets/lfr')
infile = 'YauGeneExpPValue.csv'
outfile = 'YauGeneExpPValueOnlyP.csv'


with open(infile, 'r') as source:
    rdr= csv.reader( source , delimiter=';')
    with open(outfile,"a") as result:
        wtr= csv.writer( result , delimiter=';')
        for r in rdr:
            wtr.writerow( [r[0], r[1], r[3]] )