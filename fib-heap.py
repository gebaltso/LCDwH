import math
import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np 
import csv
import collections
import itertools


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
#print(dict(graph))

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

#print(neighborsOfS)


 
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
 
    def get_min(self):
        if self.least is None:
            return None
        return self.least.key
 
    def extract_min(self):
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
 
 
fheap = FibonacciHeap()
 
#print('Menu')
#print('insert <data>')
#print('min get')
#print('min extract')
#print('quit')
# 
#while True:
#    do = input('What would you like to do? ').split()
# 
#    operation = do[0].strip().lower()
#    if operation == 'insert':
#        data = int(do[1])
#        fheap.insert(data)
#    elif operation == 'min':
#        suboperation = do[1].strip().lower()
#        if suboperation == 'get':
#            print('Minimum value: {}'.format(fheap.get_min()))
#        elif suboperation == 'extract':
#            print('Minimum value removed: {}'.format(fheap.extract_min()))
# 
#    elif operation == 'quit':
#        breakinsert
        
for i in range(0, len(neighborsOfS)):       
    fheap.insert(neighborsOfS[i]) 
    
    
    
    
print("Min is: ", fheap.get_min())
        
        
        
        
        
        
        
        