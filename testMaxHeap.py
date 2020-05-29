#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:54:02 2018

@author: georgiabaltsou
"""

import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np 
import csv
import collections
import itertools
import math
import heapq
from math import ceil

SourceFile = '/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv'
TestFile = '/Users/georgiabaltsou/Desktop/testSmall.csv'
TestFile2 = '/Users/georgiabaltsou/Desktop/test 2.csv'

sourceNodes = []
nodes = []
weights = []

nodesTmp = []
weightsTmp = []


with open(TestFile2) as csvfile:
    dataFile = csv.reader(csvfile,skipinitialspace=True, delimiter = ',')
        
    for row in dataFile:
         sourceNodes.append(row[0])
         
         for y in range(len(row)):
             if(y%2 != 0):
                 nodesTmp.append(row[y])
             else:
                 if(y != 0):
                     weightsTmp.append(row[y])
         nodes.append(nodesTmp)
         nodesTmp = []
         weights.append(weightsTmp)
         weightsTmp = []
    
#gia na afairesw ta ' ' apo ta weights  
weights = [list(map(float, grp)) for grp in weights]

#print('nodes = ', nodes)
#print('weights = ', weights)
#print('Source Nodes = ', sourceNodes)



graph = collections.defaultdict(list)
edges = {}

for i in range (0,len(sourceNodes)):
    for j in range (0, len(nodes[i])):
        graph[sourceNodes[i]].append(nodes[i][j])
        edges[sourceNodes[i], nodes[i][j]] = weights[i][j]


#print("Edges with their weights: ", edges)
#print(dict(graph))

##############################################################################


##G=nx.from_numpy_matrix(A)
#
#G = nx.Graph(graph)
#
#
#heapq.heapify(sourceNodes)
##print(sourceNodes)
##heapq.heapify(nodes)
#
###pinakas me tous ba8mous twn komvwn tou G
#degrees = []
#
#for i in range (0,len(sourceNodes)):
#    degrees.append(len(nodes[i]))
##    print("Degree of node ", sourceNodes[i], "is: ", len(nodes[i]))
#
##print(degrees)
#
###arxikopoihsh se 0 ths koinotitas C
#C = [] 
##
###arxikopoihsh se 0 tou sunolou twn geitwnwn
#N = [] 
##
###orizw ton komvo s ws ton arxiko seed node
#s = sourceNodes[1]
#
##print("# of nodes: ", len(sourceNodes))
#
###pros8etw ton s sthn koinothta C
#C.append(s)
##print("C =", C)
# 
##geitones tou komvou s se morfi pinaka
#neighborsOfS = nodes[sourceNodes.index(s)]
#print("Neighbors of node ", s, " = ", neighborsOfS)



class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        self.heap_size = 0
        if arr is not None:
            self.create_max_heap(arr)
            self.heap = arr
            self.heap_size = len(arr)

    def create_max_heap(self, arr):
        """
        Converts a given array into a max heap
        :param arr: input array of numbers
        """
        n = len(arr)

        # last n/2 elements will be leaf nodes (CBT property) hence already max heaps
        # loop from n/2 to 0 index and convert each index node into max heap
        for i in range(int(n / 2), -1, -1):
            self.max_heapify(i, arr, n)

    def max_heapify(self, indx, arr, size):
        """
        Assuming sub trees are already max heaps, converts tree rooted at current indx into a max heap.
        :param indx: Index to check for max heap
        """

        # Get index of left and right child of indx node
        left_child = indx * 2 + 1
        right_child = indx * 2 + 2

        largest = indx

        # check what is the largest value node in indx, left child and right child
        if left_child < size:
            if arr[left_child] > arr[largest]:
                largest = left_child
        if right_child < size:
            if arr[right_child] > arr[largest]:
                largest = right_child

        # if indx node is not the largest value, swap with the largest child
        # and recursively call min_heapify on the respective child swapped with
        if largest != indx:
            arr[indx], arr[largest] = arr[largest], arr[indx]
            self.max_heapify(largest, arr, size)

    def insert(self, value):
        """
        Inserts an element in the max heap
        :param value: value to be inserted in the heap
        """
        self.heap.append(value)
        self.heap_size += 1

        indx = self.heap_size - 1

        # Get parent index of the current node
        parent = int(ceil(indx / 2 - 1))

        # Check if the parent value is smaller than the newly inserted value
        # if so, then replace the value with the parent value and check with the new parent
        while parent >= 0 and self.heap[indx] > self.heap[parent]:
            self.heap[indx], self.heap[parent] = self.heap[parent], self.heap[indx]
            indx = parent
            parent = int(ceil(indx / 2 - 1))

    def delete(self, indx):
        """
        Deletes the value on the specified index node
        :param indx: index whose node is to be removed
        :return: Value of the node deleted from the heap
        """
        if self.heap_size == 0:
            print("Heap Underflow!!")
            return

        self.heap[-1], self.heap[indx] = self.heap[indx], self.heap[-1]
        self.heap_size -= 1

        self.max_heapify(indx, self.heap, self.heap_size)

        return self.heap.pop()

    def extract_max(self):
        """
        Extracts the maximum value from the heap
        :return: extracted max value
        """
        return self.delete(0)

    def print(self):
        print(*self.heap)

#heap = MaxHeap(sourceNodes)
#heap = MaxHeap([90, 80, 30, 60, 50, 100, 70, 5, 20, 10, 40, 55, 101, 45, 5])

#heap = heapq.heapify([90, 80, 30, 60, 50, 100, 70, 5, 20, 10, 40, 55, 101, 45, 5])
#
##heap.insert(15)
##print(heap.delete(2))
##print(heap.extract_max())
#print(heapq.nlargest(1,heap))
#heap.print()

#seq = [100, 2, 400, 500, 400]
#print(heapq.nlargest(1, enumerate(seq), key=lambda x: x[1]))


#heap = [(value, key) for key,value in graph.items()]
#largest = heapq.nsmallest(1, heap)
#largest = [(key, value) for value, key in largest]
#
#
#print(heap)
#print(largest)
#
#print(graph)

keys = [3.0, 2.0, 3.0]
dictionary = dict(zip(keys, sourceNodes))
#print(dictionary)

heap = MaxHeap(list(dictionary))
heap.print()

#print(max(heap))

#print(list(dictionary)[heap.print()])
#print(heapq.nlargest(1, enumerate(dictionary), key=lambda x: x[1]))
#print(heapq.nlargest(1, enumerate(dictionary)))

#print(dictionary)

