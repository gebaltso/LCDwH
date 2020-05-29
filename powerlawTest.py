#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 11:42:58 2020

@author: georgiabaltsou
"""

import numpy as np



def power_law(k_min, k_max, y, gamma):
    return ((k_max**(-gamma+1) - k_min**(-gamma+1))*y  + k_min**(-gamma+1.0))**(1.0/(-gamma + 1.0))


nodes = 200
scale_free_distribution = np.zeros(nodes, float)
k_min = 1.0
k_max = 100*k_min
gamma = 3.0



for n in range(nodes):
    scale_free_distribution[n] = power_law(k_min, k_max,np.random.uniform(0,1), gamma)
    
    

print(scale_free_distribution)