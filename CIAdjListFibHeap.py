#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:00:57 2018

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
###############################################################################
class FibonacciTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0
 
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
 
 
class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0
 
    def insert(self, key):
        new_tree = FibonacciTree(key)
        self.trees.append(new_tree)
        if (self.least is None or key > self.least.key):
            self.least = new_tree
        self.count = self.count + 1
 
    def get_max(self):
        if self.least is None:
            return None
        return self.least.key
 
    def extract_max(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.key
 
    def consolidate(self):
        aux = (floor_log2(self.count) + 1)*[None]
 
        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key < y.key:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x
 
        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                    or k.key > self.least.key):
                    self.least = k
 
 
def floor_log2(x):
    return math.frexp(x)[1] - 1
###############################################################################

#find all simlpe paths from source node to target node (A simple path is a path with no repeated nodes)
def findAllSimplePaths(G, s, t):
    paths = nx.all_shortest_paths(G, s, t)
    
#    paths = nx.dijkstra_path(G, s, t, weight='weight')
    
    print("Paths = ", list(paths))
    
    return list(paths)

#find neighbors considering a highest T threshold of the sum of the weights of the coresponding edges
def findNeighbors(G, s, T):

    sumWeights = []
    
#    for t in range(0, len(G)):
    for t in sourceNodes: #trexei sxedon 17.000 fores-->delay
        paths = findAllSimplePaths(G, s, t)
        
        
        for x in paths:
            
            if(t not in sumWeights):
                sumN = 0
                for y in range(0, len(x)):
                    if x[y] != t:
                        sumN += weights[y][y+1]
#                        print(weights[y][y+1])
                if sumN <= T:
                    sumWeights.append(t)
           
    return sumWeights


#gia upologismo olwn twn paths tou G ksekinwntas apo ton komvo s kai me mhkos paths d
def findPathsNoLC(G,s,d):  
    if d == 0:
        return [[s]]
    paths = []
    for neighbor in neighborsOfS:
        for path in findPathsNoLC(G,neighbor,d-1):
            if s not in path:
                paths.append([s]+path)
    return paths


#gia upologismo tou pinaka geitonwn tou komvou s se distance d
def find_un_nei_s(s, d, neighborsOfS):
    #pinakas adjacent geitonwn tou komvou s
    n_s = []
    N = []      
    for x in neighborsOfS:   
        n_s.append(x)
    

#    #an to d==1 tote oi geitones einai mono oi adjacent
    if d == 1:             
        N = n_s
    else:
        for x in range(0,len(findPathsNoLC(neighborsOfS,s,d))):
            N.append(findPathsNoLC(neighborsOfS,s,d)[x][d])
    
    
    #krataw tous geitones tou s xwris diplotupa    
    un_nei_sN=np.unique(N)
    un_nei_sIn=np.union1d(un_nei_sN,n_s)
    un_nei_s=np.unique(un_nei_sIn)
    #print('Neighbors of node ',s, '= ', un_nei_s)
    return un_nei_s
    
    
def find_d_Ns(un_nei_u,un_nei_v):
    intersection_u_v=np.intersect1d(un_nei_u,un_nei_v)  #evresi tomis komvwn geitonwn u kai v
    len_intersection_u_v=len(intersection_u_v)
    
    union_u_v=np.union1d(un_nei_u,un_nei_v)             #evresi enwsis komvwn geitonwn u kai v
    len_union_u_v=len(union_u_v)
    
    d_Ns=len_intersection_u_v/len_union_u_v
    
    print("tomi = ", intersection_u_v)
    print("enwsi = ", union_u_v)
    
    return d_Ns

##############################################################################

SourceFile = '/Users/georgiabaltsou/Desktop/Genes dataset/exportFinal.csv'
TestFile = '/Users/georgiabaltsou/Desktop/testSmall.csv'
TestFile2 = '/Users/georgiabaltsou/Desktop/test 2.csv'

sourceNodes = []
nodes = []
weights = []

nodesTmp = []
weightsTmp = []


with open(SourceFile) as csvfile:
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
#print(dict(graph)) #{Α34:[A53, A87], A46:[A21, A90]}...

##############################################################################


#G=nx.from_numpy_matrix(A)

G = nx.Graph(graph)
#print("Length of G: ", len(G))

#na mh sxediazontai oi aksones    
#plt.axis('off')         

#sxediasmos grafou
#nx.draw(G) 

#print("Nodes = ", G.nodes)

#
##oloi oi komvoi tou grafhmatos
#nodes = nx.nodes(G)   
#
#
##pinakas me tous ba8mous twn komvwn tou G
degrees = []

for i in range (0,len(sourceNodes)):
    degrees.append(len(nodes[i]))
#    print("Degree of node ", sourceNodes[i], "is: ", len(nodes[i]))

#print(degrees)

##arxikopoihsh se 0 ths koinotitas C
C = [] 
#
##arxikopoihsh se 0 tou sunolou twn geitwnwn
N = [] 
#
##orizw ton komvo s ws ton arxiko seed node
s = sourceNodes[0]

#print("# of nodes: ", len(sourceNodes))

##pros8etw ton s sthn koinothta C
C.append(s)
#print("C =", C)
 
#geitones tou komvou s se morfi pinaka
neighborsOfS = nodes[sourceNodes.index(s)]


##orizw to distance
d = 1 
#
##orizw to threshold
T = 2
#    
##pinakas me to sunolo geitonwn tou s se d-level
N=find_un_nei_s(s, d, neighborsOfS)
#
#N = findNeighbors(G, s, T)
#
#print("Neighbors = ", N) 


#print("Paths: ", findAllSimplePaths(G, C[0], N[0]))


##gia oso uparxoun komvoi entos tou N
while len(N)>0: #len(N)=170
#while len(C)<2:
    
    #print("N = ", N)
    
    len_N = len(N)
    len_C = len(C)
      
    IS = 0
    ES = 0
    
    #print("paradeigma ", find_d_Ns(find_un_nei_s(16, d), find_un_nei_s(2, d)))

    #pinakas gia ta a8roismata twn d_Ns 
    sum_array = []
#    sum_array = FibonacciHeap()
#    sum_array = MaxHeap()

    #gia na brw to a entos tou N
    for a in range(0, len_N):
                    
        sum_tmp = 0
        NA = findNeighbors(G, N[a], T)
        
        #gia ka8e u entos tou C
        for u in range(0, len_C):
                       
#            print("Geitones v = ", findNeighbors(G, N[a], T))
#            print("Geitones u = ", findNeighbors(G, C[u], T))
            sum_tmp += find_d_Ns(NA, findNeighbors(G, C[u], T))
            
            print("***")
                       
        sum_array.append(sum_tmp)
#        sum_array.insert(sum_tmp)
                    
        #print("sum_array =", sum_array)
        
    dictionary = dict(zip(sum_array, sourceNodes))
    print(dictionary)
    
#    sum_array.print()
                    
    #index tou max stoixeiou            
#    max_a = sum_array.index(max(sum_array))
#    max_a = sum_array.extract_max()()
    #sum_array.extract_max()
    #print("Max a = ", max_a)
    
       
    N0 = findNeighbors(G, N[sum_array[0]], T)
      
    for y in range(0,len_C):
        #if G.has_edge(C[y], N[max_a]):
        if G.has_edge(C[y], N[sum_array[0]]):
            #IS = IS + find_d_Ns(findNeighbors(G, C[y], T), findNeighbors(G, N[max_a], T))
            IS = IS + find_d_Ns(findNeighbors(G, C[y], T), N0)
                       
    #vriskw tous komvous tou grafhmatos pou den anhkoun sthn C
    nodes_not_C = np.setdiff1d(nodes, C)
    len_nodes_not_C = len(nodes_not_C)
#    print("C = ", C)
#    print("not C = ", nodes_not_C)
    for y in range(0,len_nodes_not_C):
        #if G.has_edge(nodes_not_C[y], N[max_a]):
        if G.has_edge(nodes_not_C[y], N[sum_array[0]]):
            #ES = ES + find_d_Ns(findNeighbors(G, nodes_not_C[y], T), findNeighbors(G, N[max_a], T))
            ES = ES + find_d_Ns(findNeighbors(G, nodes_not_C[y], T), N0)
  
#    print("IS = ", IS)
#    print("ES = ", ES)
    #briskw to klasma IS/(ES-IS)
    fraction=IS/(ES-IS)
    
#    print("fraction = ", fraction)
       
    nominator = 0
    denominator = 0
    
    if len_C == 1:
        CI = 0
    else:
        #oloi oi pi8anoi sunduasmoi metaksu 2 kombwn entos C
        lista_kombwn_C=list(itertools.combinations(C, 2))
#        print("lista komvwn = ", lista_kombwn_C)
           
        for y in range(0, len(lista_kombwn_C)):
            #print("stoixeio: ", (lista_kombwn_C[y])[0])
            if G.has_edge((lista_kombwn_C[y])[0], (lista_kombwn_C[y])[1]):
                nominator += find_d_Ns(findNeighbors(G, (lista_kombwn_C[y])[0], T), (findNeighbors(G, (lista_kombwn_C[y])[1], T)))
        
        
        for y in range(0, len(C)):       
            for x in range(0, len(N)): 
                if G.has_edge((C[y]), (N[x])):
                    denominator +=  find_d_Ns(findNeighbors(G, C[y], T), (findNeighbors(G, N[x], T)))
        
        denominator += 1

        CI = nominator/denominator
        
#        print("nominator = ", nominator)
#        print("denominator = ", denominator)
#        print("CI =", CI)
        
    #an kalutereuei to fraction pros8etw ton komvo a sth C alliws oxi 
    if fraction > CI:
        #C.append(N[max_a])
        C.append(N[sum_array[0]])
        #N = np.delete(N, max_a)
        N = np.delete(N, sum_array[0])
        sum_array.extract_max()
        
    else:
        #N = np.delete(N, max_a)
        N = np.delete(N, sum_array[0]) 
        sum_array.extract_max()             

print('Community: ', C)

#metraw me posous komvous entos C enwnetai o s prokeimenou na upologisw to dCs (ba8mos entos C tou komvou s)
dCs = 0
for i in C:
    if G.has_edge(s, i):
        dCs += 1


##upologismos participation
participation = (dCs/len(C))/(degrees[sourceNodes.index(s)]/len(nodes))

print("max participation is ", len(nodes)/len(C))

print("participation= ", participation)
      

