#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 18:05:33 2019

@author: georgiabaltsou
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import sys
import os
import random

def community_layout(g, partition):
    """
    Compute the layout for a modular graph.


    Arguments:
    ----------
    g -- networkx.Graph or networkx.DiGraph instance
        graph to plot

    partition -- dict mapping int node -> int community
        graph partitions


    Returns:
    --------
    pos -- dict mapping int node -> (float x, float y)
        node positions

    """

    pos_communities = _position_communities(g, partition, scale=3.)

    pos_nodes = _position_nodes(g, partition, scale=1.)

    # combine positions
    pos = dict()
    for node in g.nodes():
        pos[node] = pos_communities[node] + pos_nodes[node]

    return pos

def _position_communities(g, partition, **kwargs):

    # create a weighted graph, in which each node corresponds to a community,
    # and each edge weight to the number of edges between communities
    between_community_edges = _find_between_community_edges(g, partition)

    communities = set(partition.values())
    #htan DiGraph dld directed. To allaksa se Undirected
    hypergraph = nx.Graph()
    hypergraph.add_nodes_from(communities)
#    for (ci, cj), edges in between_community_edges.items():
#        hypergraph.add_edge(ci, cj, weight=len(edges))
    for (ci, cj), edges in between_community_edges.items():
        hypergraph.add_edge(ci, cj)

    # find layout for communities
    pos_communities = nx.spring_layout(hypergraph, **kwargs, k=0.5, iterations=20)

    # set node positions to position of community
    pos = dict()
    for node, community in partition.items():
        pos[node] = pos_communities[community]

    return pos

def _find_between_community_edges(g, partition):

    edges = dict()

    for (ni, nj) in g.edges():
        
        ci = partition[ni]
        cj = partition[nj]

        if ci != cj:
            try:
                edges[(ci, cj)] += [(ni, nj)]
            except KeyError:
                edges[(ci, cj)] = [(ni, nj)]     
    

    return edges

def _position_nodes(g, partition, **kwargs):
    """
    Positions nodes within communities.
    """

    communities = dict()
    for node, community in partition.items():
        try:
            communities[community] += [node]
        except KeyError:
            communities[community] = [node]

    pos = dict()
    for ci, nodes in communities.items():
        subgraph = g.subgraph(nodes)
        pos_subgraph = nx.spring_layout(subgraph, **kwargs, k=0.5, iterations=20)
        pos.update(pos_subgraph)

    return pos

def test():
    # to install networkx 2.0 compatible version of python-louvain use:
    # pip install -U git+https://github.com/taynaud/python-louvain.git@networkx2
    from community import community_louvain

    g = nx.karate_club_graph()
    partition = community_louvain.best_partition(g)
    pos = community_layout(g, partition)

    nx.draw(g, pos, node_color=partition.values()); plt.show()
    return


os.chdir('seperatedExps/datasets/lfr/')

myFile = 'football.csv'
filename = "football.csv"

#initial_communities = [[18, 800, 418, 803, 35, 421, 166, 679, 680, 423, 678, 557, 178, 52, 954, 962, 964, 840, 73, 458, 75, 78, 721, 467, 342, 90, 349, 224, 358, 365, 115, 117, 887], [257, 268, 144, 789, 929, 936, 552, 44, 815, 431, 819, 179, 565, 694, 311, 952, 185, 442, 59, 191, 65, 707, 455, 843, 715, 336, 96, 482, 104, 233, 106, 621, 765, 895], [322, 387, 132, 580, 510, 391, 392, 77, 718, 719, 334, 849, 464, 83, 532, 598, 982, 472, 343, 92, 480, 121, 556, 748, 302, 435, 502, 441, 60, 62],[199,649,74,606,525,749,306,568,986,798,671],[643,899,4,902,135,394,142,911,677,38,808,683,940,305,57,186,957,963,586,459,594,595,724,725,601,225,354,226,868,741,229,488,364,879,367,625,116,247,763,382],[129,7,520,140,658,790,345,797,93,289,739,486,493,624,377,506,123,255], [448,832,900,70,72,712,331,204,720,978,850,471,344,665,667,91,604,184,416,97,866,105,108,752,497,566,182,310,58,956,959], [805,294,654,335,729,405,86,436,373,409,282,284], [290,547,389,775,263,11,269,397,13,208,152,157], [960,521,527,400,402,275,853,406,668,412,36,232,489,426,239,757,120,380],
#               [417,217,646,41,812,110,847,80,146,407,153,603],[608,67,451,620,912,17,880,437,918,281,921,955,159], [200,393,778,526,786,916,24,413,414,420,169,43,47,944,240,125,767], [517,659,21,277,279,795,674,934,42,300,307,51,822,438,55,699,831,837,456,332,973,76,81,977,728,89,474,88,860,477,602,607,992,735,995,867,996,743,872,360,490,744,878,754,626,888,376,126,894], [897,583,9,841,276,727,920,216,215,609,610,483,227,487,555,363,945,114,629,632,570], [516,133,676,968,522,682,619,909,143,529,852,669,478], [896,642,130,388,134,647,264,905,650,137,801,804,498,563,564,883,635], [768,385,769,576,704,261,324,10,395,141,270,653,22,287,32,292,554,430,366,111,368,243,885,569], [1,645,328,202,396,972,206,211,857,924,734,479,94,932,613,491,756,633], [903,8,403,917,278,792,793,922,283,926,286,865,98,484,806,871,492,623,49,755,309,119,696,634,893],[836,453,145,661,346,163,291,168,427,684,942,434,882,949,181,444], [260,781,656,531,533,288,37,39,807,298,814,174,433,439,824,827,829,706,578,71,711,713,329,327,210,352,485,616,236,371,501,246,638,639], [779,907,915,160,673,675,422,681,810,811,428,425,686,297,46,562,312,446,449,834,835,708,325,68,714,971,213,218,475,611,230,359,234,875,747,237,112,636], [710,267,908,14,976,468,662,410,33,164,997,998,103,429,50,244,122,254],
#               [323,419,503,326,6,648,249,881,61,791,953,764,317], [515,139,154,542,672,161,802,40,172,685,301,943,816,687,947,948,53,823,443,702,958,705,579,201,842,591,79,339,854,600,473,858,347,219,731,223,481,355,612,102,617,362,877,622,245,766], [548,447,461,910,45,750,818,507,252,567,859,220,95], [928,457,784,528,466,530,370,469,54,951,253,892,925,990], [577,770,514,386,194,581,966,777,585,337,209,147,851,341,732,862,933,615,107,176,177,690,821,950,504,313,571,700,189,575], [512,518,399,657,274,788,148,150,666,539,923,541,158,543,799,551,296,558,560,304,817,946,561,688,188,573,318,450,965,198,584,846,981,856,991,863,737,356,869,614,740,101,746,494,631], [898,663,969,845,48,273,820,535,509,670], [258,131,644,772,774,838,651,523,589,280,408,156,931,173,180,758,183,760,505,316], [64,833,935,167,553,138,861,462,559,207,989,983,695,988,285], [265,12,785,537,415,162,34,809,830,192,321,709,587,460,717,465,596,212,470,985,733,221,99,357,742,999,870,745,753,628,374,761,381,127], [256,195,262,424,205,109,15,187,913,664,27,350,63], [0,3,19,930,299,175,691,308,826,314,828,319,320,582,203,974,975,338,980,855,87,730,993,994,738,361,235,369,627,630,759,250,511], [384,904,722,787,919,25,293,938,939,238,495,432,499,693,886,124], [197,839,780,588,782,716,593,82,937,873,874,618,941,113,500,118,56,762,383], 
#               [513,2,906,590,783,401,20,597,794,544,546,496,241,375,440,890,251], [771,773,266,652,190,592,248,891,796,30], [193,545,259,171,333,404,984,889,411,28,445], [454,574,813,660,149,85,697,29,222,703], [128,641,66,452,550,519,848,914,698,379,348,572], [69,136,655,534,538,26,927,31,165,295,689,692,825,315,508,701], [640,901,390,776,398,16,23,536,549,961,967,970,844,463,979,723,340,726,84,599,987,476,605,351,864,736,228,100,876,751,242,372,884,378,637], [353,196,5,231,330,170,524,271,272,303,214,151,155,540]]
#
#
#GTC = [260,781,656,531,533,288,37,39,807,298,814,174,433,439,824,827,829,706,578,71,711,713,329,327,210,352,485,616,236,371,501,246,638,639]

initial_communities =[[1, 25, 33, 37, 45, 89, 103, 105, 109],
[19, 29, 30, 35, 55, 79, 94, 101],
[2, 6, 13, 15, 32, 39, 47, 60, 64, 100, 106],
[3, 5, 10, 40, 52, 72, 74, 81, 84, 98, 102, 107],
[44, 57, 66, 75, 86, 91, 92, 112],
[48, 28, 46, 49, 53, 67, 73, 83, 88, 110, 114, 58],
[11, 24, 50, 69, 63, 59, 97],
[90, 82, 80, 42, 36],
[12, 14, 18, 26, 31, 34, 38, 43, 54, 61, 71, 85, 99],
[0, 4, 9, 16, 23, 41, 93, 104],
[7, 8, 21, 22, 51, 68, 77, 78, 108, 111],
[17, 20, 27, 56, 62, 65, 70, 76, 87, 95, 96, 113]]

GTC = [0, 4, 9, 16, 23, 41, 93, 104]



G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')


total = {}
communities = {}
community_id = 1
with open(filename) as f:
    for line in f:
        nodes = [n for n in line.strip().split(' ')]
        for node in nodes:
            total[node] = community_id
        communities[community_id] = nodes
        community_id = community_id + 1


number_of_colors = community_id - 1

pos = community_layout(G, total)

colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]


labels = {} 
#color = {} 
for node in G.nodes():
    if int(node) in GTC:
        #set the node name as the key and the label as its value 
        labels[node] = node
#        color[node] = colors[node]


GTC  = [str(i) for i in GTC]

edge_colors = ['green' if ((e[0] in GTC) or (e[1]) in GTC) else 'gray' for e in G.edges]
widths = [0.7 if ((e[0] in GTC) or (e[1]) in GTC) else 0.1 for e in G.edges]

nx.draw(G, pos, node_color='cyan', node_size= 20, width=widths, edge_color = edge_colors, alpha = 0.6)

nx.draw_networkx_nodes(G, pos, nodelist=GTC, node_color='y', node_size= 30)
nx.draw_networkx_labels(G,pos,labels,font_size=4,font_color='red')


plt.savefig("Graph.png", format="PNG", dpi=1000)
plt.show()


