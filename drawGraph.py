#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:13:26 2019

@author: georgiabaltsou
"""

import matplotlib.pyplot as plt
import networkx as nx
import sys
import random
import os
from networkx.algorithms.community import LFR_benchmark_graph
import csv

def LFR(n, tau1, tau2, mu):

#n = 1000 #(int)number of nodes
#tau1 = 3  #(float) Power law exponent for the degree distribution of the created graph. This value must be strictly greater than one.
#tau2 = 1.1  #(float) Power law exponent for the community size distribution in the created graph. This value must be strictly greater than one.
#mu = 0.1  #(float) Fraction of intra-community edges incident to each node. This value must be in the interval [0, 1].

#greater mu => pio asafeis koinothtes!


#average_degree and min_degree  must be in [0, n]. One of these must be specified.
#max_degree if not specified is set to n.
#min_community if not specified is set to min_degree.
#max_community if not specified is set to n.
#tol(float) Tolerance when comparing floats, specifically when comparing average degree values.
#max_iters (int) Maximum number of iterations to try to create the community sizes, degree distribution, and community affiliations.
#seed (integer, random_state, or None (default)) Indicator of random number generation state.
    
    
    
    os.chdir('testGraph/lfr')

    G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=10, max_degree=50, min_community=10, max_community=50)
    
    #remove self loops
    G.remove_edges_from(G.selfloop_edges())
    
    numberOfEdges = G.number_of_edges()
    
    print("Number of edges of graph G: ", numberOfEdges)
    print("------------------------------")
    
    #na mh sxediazontai oi aksones    
    #plt.axis('off')         
    
    #sxediasmos grafou
    #nx.draw(G) 
    
    communities = {frozenset(G.nodes[v]['community']) for v in G}
    
    adjacency_list_filename = 'lfrAdjlistN'+str(n)+'MU'+str(mu)+'*.txt'
    edge_list_filename = 'lfrEdgelistN'+str(n)+'MU'+str(mu)+'*.txt'
    community_list_filename = 'lfrCommN'+str(n)+'MU'+str(mu)+'*.txt'
    
    #print('Communities: ', communities)
    
    with open('lfrCommN'+str(n)+'MU'+str(mu)+'*.txt', 'w') as fc:
        fc.write(str([list(x) for x in communities]))
    
    
    nx.write_adjlist(G,adjacency_list_filename)
    fh=open(adjacency_list_filename,'wb')
    nx.write_adjlist(G, fh)
    
    
    
    edge_list = []
    with open(adjacency_list_filename, 'r') as f:
        for line in f:
            
            if line.startswith("#"): #skip first comment lines
                continue;
            else:
    
                line = line.rstrip('\n').split(' ')
                source = line[0]
                for target in line[1:]:
                    #edge_list.append("%s %s 1" % (source, target)) #1 is for the weight
                    edge_list.append("%s %s" % (source, target))
    
    with open(edge_list_filename, 'w') as f:
        f.write('%s\n' % ('\n'.join(edge_list)))
        
      
    with open(community_list_filename, 'w') as f:
        for item in communities:
            f.write("%s\n" % str(list(item)))
     
    #remove unecessary symbols like []       
    with open(community_list_filename, 'r') as my_file:
        text = my_file.read()
        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace(",", "")
        
    with open(community_list_filename, 'w') as my_file:
            
        my_file.write(text)
    
    #convert edge txt file to csv file appending also weight 1 to all edges
    with open('lfrEdgelistN'+str(n)+'MU'+str(mu)+'*.txt') as data_file: 
                reader = csv.reader(data_file, delimiter=' ')        
                with open('lfrEdgelistN'+str(n)+'MU'+str(mu)+'*.csv', 'w') as out_file:
                    writer = csv.writer(out_file, delimiter=';')  
                    for row in reader:
                        writer.writerow([row[0],row[1], 1])
                        
    return 'lfrEdgelistN'+str(n)+'MU'+str(mu)+'*.csv', communities



#############################################################################################

os.chdir('seperatedExps/datasets/lfr/')

myFile = 'lfrEdgelistN1000MU0.1*.csv'


communities = [[18, 800, 418, 803, 35, 421, 166, 679, 680, 423, 678, 557, 178, 52, 954, 962, 964, 840, 73, 458, 75, 78, 721, 467, 342, 90, 349, 224, 358, 365, 115, 117, 887,], [257, 268, 144, 789, 929, 936, 552, 44, 815, 431, 819, 179, 565, 694, 311, 952, 185, 442, 59, 191, 65, 707, 455, 843, 715, 336, 96, 482, 104, 233, 106, 621, 765, 895], [322, 387, 132, 580, 510, 391, 392, 77, 718, 719, 334, 849, 464, 83, 532, 598, 982, 472, 343, 92, 480, 121, 556, 748, 302, 435, 502, 441, 60, 62],[199,649,74,606,525,749,306,568,986,798,671],[643,899,4,902,135,394,142,911,677,38,808,683,940,305,57,186,957,963,586,459,594,595,724,725,601,225,354,226,868,741,229,488,364,879,367,625,116,247,763,382],[129,7,520,140,658,790,345,797,93,289,739,486,493,624,377,506,123,255], [448,832,900,70,72,712,331,204,720,978,850,471,344,665,667,91,604,184,416,97,866,105,108,752,497,566,182,310,58,956,959], [805,294,654,335,729,405,86,436,373,409,282,284], [290,547,389,775,263,11,269,397,13,208,152,157], [960,521,527,400,402,275,853,406,668,412,36,232,489,426,239,757,120,380],
               [417,217,646,41,812,110,847,80,146,407,153,603],[608,67,451,620,912,17,880,437,918,281,921,955,159], [200,393,778,526,786,916,24,413,414,420,169,43,47,944,240,125,767], [517,659,21,277,279,795,674,934,42,300,307,51,822,438,55,699,831,837,456,332,973,76,81,977,728,89,474,88,860,477,602,607,992,735,995,867,996,743,872,360,490,744,878,754,626,888,376,126,894], [897,583,9,841,276,727,920,216,215,609,610,483,227,487,555,363,945,114,629,632,570], [516,133,676,968,522,682,619,909,143,529,852,669,478], [896,642,130,388,134,647,264,905,650,137,801,804,498,563,564,883,635], [768,385,769,576,704,261,324,10,395,141,270,653,22,287,32,292,554,430,366,111,368,243,885,569], [1,645,328,202,396,972,206,211,857,924,734,479,94,932,613,491,756,633], [903,8,403,917,278,792,793,922,283,926,286,865,98,484,806,871,492,623,49,755,309,119,696,634,893],[836,453,145,661,346,163,291,168,427,684,942,434,882,949,181,444], [260,781,656,531,533,288,37,39,807,298,814,174,433,439,824,827,829,706,578,71,711,713,329,327,210,352,485,616,236,371,501,246,638,639], [779,907,915,160,673,675,422,681,810,811,428,425,686,297,46,562,312,446,449,834,835,708,325,68,714,971,213,218,475,611,230,359,234,875,747,237,112,636], [710,267,908,14,976,468,662,410,33,164,997,998,103,429,50,244,122,254],
               [323,419,503,326,6,648,249,881,61,791,953,764,317], [515,139,154,542,672,161,802,40,172,685,301,943,816,687,947,948,53,823,443,702,958,705,579,201,842,591,79,339,854,600,473,858,347,219,731,223,481,355,612,102,617,362,877,622,245,766], [548,447,461,910,45,750,818,507,252,567,859,220,95], [928,457,784,528,466,530,370,469,54,951,253,892,925,990], [577,770,514,386,194,581,966,777,585,337,209,147,851,341,732,862,933,615,107,176,177,690,821,950,504,313,571,700,189,575], [512,518,399,657,274,788,148,150,666,539,923,541,158,543,799,551,296,558,560,304,817,946,561,688,188,573,318,450,965,198,584,846,981,856,991,863,737,356,869,614,740,101,746,494,631], [898,663,969,845,48,273,820,535,509,670], [258,131,644,772,774,838,651,523,589,280,408,156,931,173,180,758,183,760,505,316], [64,833,935,167,553,138,861,462,559,207,989,983,695,988,285], [265,12,785,537,415,162,34,809,830,192,321,709,587,460,717,465,596,212,470,985,733,221,99,357,742,999,870,745,753,628,374,761,381,127], [256,195,262,424,205,109,15,187,913,664,27,350,63], [0,3,19,930,299,175,691,308,826,314,828,319,320,582,203,974,975,338,980,855,87,730,993,994,738,361,235,369,627,630,759,250,511], [384,904,722,787,919,25,293,938,939,238,495,432,499,693,886,124], [197,839,780,588,782,716,593,82,937,873,874,618,941,113,500,118,56,762,383], 
               [513,2,906,590,783,401,20,597,794,544,546,496,241,375,440,890,251], [771,773,266,652,190,592,248,891,796,30], [193,545,259,171,333,404,984,889,411,28,445], [454,574,813,660,149,85,697,29,222,703], [128,641,66,452,550,519,848,914,698,379,348,572], [69,136,655,534,538,26,927,31,165,295,689,692,825,315,508,701], [640,901,390,776,398,16,23,536,549,961,967,970,844,463,979,723,340,726,84,599,987,476,605,351,864,736,228,100,876,751,242,372,884,378,637], [353,196,5,231,330,170,524,271,272,303,214,151,155,540]]

#GTC = [608,67,451,620,912,17,880,437,918,281,921,955,159]


all_nodes = []

for i, value in enumerate(communities):

    all_nodes = all_nodes + value


#node_lists_community1 = [1,2,3, 4]
#node_lists_community2 = [5, 6, 7]
#node_lists_community3 = [8,10,11,12, 13]
#all_nodes = node_lists_community1+ node_lists_community2+ node_lists_community3

#list of edges
#elist = [(1,2), (1,3), (2,4), (2, 5), (5,6), (6,7),
#        (7,9), (8,10), (8,11), (11,13), (12,13), (2, 11)]


G = nx.Graph()
G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')

elist = G.edges(data = False)


#create the networkx Graph with node types and specifying edge distances
G = nx.Graph()
for n in all_nodes:
    G.add_node(n)
for from_loc, to_loc in elist:
    G.add_edge(from_loc, to_loc)   

pos = nx.spring_layout(G) #calculate position for each node
#pos = nx.random_layout(G)
#pos = nx.spectral_layout(G)
# pos is needed because we are going to draw a few nodes at a time,
# pos fixes their positions.

# Notice that the pos dict is passed to each call to draw below

# Draw the graph, but don't color the nodes
#nx.draw(G, pos, edge_color='k',  with_labels=False,
#         font_weight='light', node_size= 20, width= 0.1)

#********************************************************************************
nx.draw(G, pos, edge_color='k',  with_labels=False,
         font_weight='light', node_size= 20, width= 0.1)

#For each community list, draw the nodes, giving it a specific color.
#nx.draw_networkx_nodes(G3, pos, nodelist=node_lists_community1, node_color='b')
#nx.draw_networkx_nodes(G3, pos, nodelist=node_lists_community2, node_color='r')
#nx.draw_networkx_nodes(G3, pos, nodelist=node_lists_community3, node_color='g')

#********************************************************************************
nx.draw_networkx_nodes(G, pos, nodelist=communities[9], node_color='g', node_size= 40)


#nx.draw_networkx_nodes(G, pos, nodelist=communities[9], node_color='g', node_size= 40)
#nodes = nx.draw_networkx_nodes(G, pos, node_size=node_size, cmap=plt.cm.winter, node_color=list(partition.values()))
#nx.draw_networkx_edges(G, pos, alpha=0.3)


plt.savefig('graph.png')
plt.show()