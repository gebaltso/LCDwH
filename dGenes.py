#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:31:53 2020

@author: georgiabaltsou
"""

import pandas as pd

df = pd.read_csv("agilentPearsonAll.csv")

#df = data.sort_values(['value', 'geneA'], ascending=False)
#
#
#print(df)
#
#df = data.groupby(['geneA'], sort=False).first()


#data = data.loc[data.groupby(['geneA']).value.idxmax()]



#A = df.groupby('geneA')['value'].nlargest(2).reset_index()
#A.rename(columns={'geneA': 'gene'}, inplace=True)
#
#B = df.groupby('geneB')['value'].nlargest(2).reset_index()    
#B.rename(columns={'geneB': 'gene'}, inplace=True) 
#
#d = A.append(B)
#
#d.groupby('gene')['value'].nlargest(2).reset_index().drop('level_1', 1)
#
#
#print(d)


total_df = pd.concat([df, df.rename(columns={'geneA':'geneB','geneB':'geneA'})], sort=True)

df = (total_df.sort_values(['geneA','value'], ascending=[True,False])
   .groupby('geneA').head(2)
)


df.to_csv(r'agilentPearsonAllFinal.csv')