# LTE

import networkx as nx
import time


# definition 1: Γ(u) = geitones  + u
def findNeighboorOfu(G,u):
    neighbors = []
    for i in G.neighbors(u):
        neighbors.append(i)
    neighbors.append(u)
    return neighbors


# definition 2 :(Structural Similarity)network G~(V ,E,w),
# between two adjacent vertices u and v is:
def structuralSimilarity(G, u, v):
    total = 0
    total1 = 0
    total2 = 0

    n = intersection(findNeighboorOfu(G, u), findNeighboorOfu(G, v))
    n.remove(u)
    n.remove(v)

    for x in n:
        weightForux = G.get_edge_data(u, x, default=0)
        temp1 = weightForux['weight']
        weightForvx = G.get_edge_data(v, x, default=0)
        temp2 =weightForvx['weight']
        total = total + temp1*temp2

    set1 = findNeighboorOfu(G, u)
    set1.remove(u)

    for x in set1:
        weightForux = G.get_edge_data(u, x)
        temp1 = weightForux['weight']
        total1 = total1 + temp1**2

    total1 = total1**(1/2)

    set2 = findNeighboorOfu(G, v)
    set2.remove(v)

    for x in set2:
        weightForvx = G.get_edge_data(v, x)
        temp1 = weightForvx['weight']
        total2 = total2 + temp1**2

    total2 = total2**(1/2)

    return total/total1*total2
    # 8eloume na mas gurisei pisw enas ari8mos me to structural gia 2 geitones


def SinC(C, G, similarityStore):
    total = 0
    for u in C:
        for v in C:
            if (u, v) in G.edges():
                for i in similarityStore:
                    if (u, v) or (v, u) == i[1]:
                        total = 2 * i[0]
                        break
                    else:
                        total = 2*structuralSimilarity(G, u, v)
                        break
    if total == 0:
        total = 1
    return total


def SoutC(C, N, G,similarityStore):
    total = 0
    for u in C:
        for v in N:
            if (u, v) in G.edges():
                for i in similarityStore:
                    if (u, v) or (v, u) == i[1]:
                       total = total + i[0]
                    else:
                        total = total + structuralSimilarity(G, u, v)
    return total


def SinCa(C, G, a, similarityStore):
    total = 0
    for u in C:
        if (u, a) in G.edges():
            for i in similarityStore:
                if (u, a) or (a, u) == i[1]:
                    total = total + i[0]
                else:
                    total = total + structuralSimilarity(G, u, a)

    if total == 0:
        total = 1
    return total


def SoutCa(C, G, a, similarityStore):
    total = 0
    n = findNeighboorOfu(G, a)
    n.remove(a)
    n = list(set(n).difference(set(C)))

    for u in n:
        if (a, u) in G.edges():
            for i in similarityStore:
                if (u, a) or (a, u) == i[1]:
                    total = total + i[0]
                else:
                    total = total + structuralSimilarity(G, u, a)

    return total


# intersection of lists - complexity O(n)
def intersection(list1, list2):
    temp = set(list2)
    list3 = [value for value in list1 if value in temp]
    return list3

# definition 5: Tunable Tightness Gain for the community C merging a neighbor vertex a
def tunableTightnessGain(C, G, N, a, factor,similarityStore):
    return ((SoutC(C, N, G, similarityStore) / SinC(C, G,similarityStore)) - ((factor*SoutCa(C, G, a,similarityStore) - SinCa(C, G, a,similarityStore)) / 2 * SinCa(C, G, a,similarityStore)))

# main program


G = nx.Graph()
G = nx.read_weighted_edgelist("myFile.csv", create_using=nx.Graph(), delimiter=";")


# print("Edges: ", G.number_of_edges()) # 2671753
print("Nodes: ", G.number_of_nodes())

# arxikopoihsh se 0 ths koinotitas C
C = []

# arxikopoihsh se 0 tou sunolou tou Neighoorhood eksw apo thn koinothta C
N = []

# step 1
vertex = 'A_23_P251480'
start_time = time.time()

C.append(vertex)
N = N + findNeighboorOfu(G, vertex)
N.remove(vertex)
factor = 0.005

print("neighors of "+vertex +": "+str(N))
while N:
    print("N:" +str(len(N)))
    similarityStore =[]
    temp = []

    # step 2:Select a vertex a of N that possess the largest similarity with vertices in C
    for vertex in C:
        flag = 0
        for a in N:
            if (a, vertex) in G.edges():
                temp1 = structuralSimilarity(G, a, vertex)
                similarityStore.append([temp1, (vertex, a)])
                # print("vertex: " + vertex + " candidate: " + str(a) + " score: " + str(temp1))
                # print("temp: " + str(temp))

                for k in temp:
                    scoreofmax = k[1]
                    nameofmax = k[0]
                    if nameofmax == a:
                        if scoreofmax < temp1:
                            temp.remove([a, scoreofmax])
                            temp.append([a, temp1])
                            flag = 1
                            break
                        elif scoreofmax >= temp1:
                            flag = 2
                            break

                if flag == 0:
                    temp.append([a, temp1])


    temp = sorted(temp, key=lambda kv: kv[1])
    # print("similarityStore: "+ str(similarityStore))

    # step 3 orise to factor gia mikres koinoththtes megalo factor -> 10
    print("------------------------------------------------------------------")

    while temp:
        i = len(temp) - 1
        scoreofmax = temp[i][1]
        nameofmax = temp[i][0]
        # print("candicate: "+str(nameofmax))

        tunable = tunableTightnessGain(C, G, N, nameofmax, factor, similarityStore)
        # print("tunable:" + str(tunable))

        if tunable > 0:
            C.append(nameofmax)
            N = N + findNeighboorOfu(G, nameofmax)
            N = list(set(N).difference(set(C)))
            del similarityStore
            break
        else:
            N.remove(nameofmax)
            del temp[i]

    print("C: ")
    print("members of C:" +str(len(C)))
    print(C)


print("C: ")
print(len(C))
print(C)
print("--- %s seconds ---" % (time.time() - start_time))


