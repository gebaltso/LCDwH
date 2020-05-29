import math
import csv
from decimal import Decimal


#computes the distance between two string vectors in s, columns c1 and c2 with dimension dim
def compute_distance(d,c1,c2,dim,properties):

    i =0
    dis =0
    

    ## distance computation - choosing the l_2 norm - euclidean distance
    for i in range (0,dim):
        dis = dis + abs(float(d[i][c1])-float(d[i][c2]))
        
    return math.sqrt(dim) - math.sqrt(dis)

    ## distance computation - choosing the cosine similarity measure
    # (-1 dissimilar and 1 similar - 0 orthogonal, since everything is positive
    # no negative similarities are possible)
##    dot = 0
##    sum1 = 0
##    sum2 = 0
##    for i in range(0, dim):
##        dot = dot + float(d[i][c1])*float(d[i][c2])
##        sum1 = sum1 + float(d[i][c1])
##        sum2 = sum2 + float(d[i][c2])
##
##    try:
##        return (float(dot)/(math.sqrt(sum1) * math.sqrt(sum2)))
##    except ZeroDivisionError:
##        return 0


   ## manhattan distance   
##    for i in range (0,dim):
##      dis = dis + abs(float(d[i][c1])-float(d[i][c2]))
##    return math.sqrt(dim)-dis



    ##jaccard similarity
##    sum_j11 = 0
##    sum_j01 = 0
##    sum_j10 = 0
##    for i in range(0,dim):
##      if int(d[i][c1])==1:
##          if int(d[i][c2])==1:
##              sum_j11+=1
##          else:
##              sum_j10+=1
##      else:
##          if int(d[i][c2])==1:
##              sum_j01+=1
##
##    # Can"t have division by 0
##    try:
##      return float(sum_j11)/(sum_j01+sum_j10+sum_j11)
##    except ZeroDivisionError:
##      return 0


    ##Pearson correlation
        # Input: 2 objects
        # Output: Pearson Correlation Score
##    
##    values = range(dim)
##    
##    # Summation over all attributes for both objects
##    sum_c1 = sum([float(d[i][c1]) for i in values])
##    sum_c2 = sum([float(d[i][c2]) for i in values])
##
##    # Sum the squares
##    square_sum1 = sum([pow(int(d[i][c1]),2) for i in values])
##    square_sum2 = sum([pow(int(d[i][c2]),2) for i in values])
##
##    # Add up the products
##    product = sum([(int(d[i][c1]))*(int(d[i][c2])) for i in values])
##
##    #Calculate Pearson Correlation score
##    numerator = product - (sum_c1*sum_c2/len(d))
##    denominator = ((square_sum1 - float(pow(sum_c1,2))/len(d)) * (square_sum2 - 
##    float(pow(sum_c2,2))/len(d))) ** 0.5
##            
##    # Can"t have division by 0
##    if denominator == 0:
##        return 0
##
##    return float(numerator)/denominator



#
#Takes a .csv file (; delimited) and turns it to
#a file where nodes are properties. Edges are weighted and
#correspond to distances betweeen the vectors of properties based on the patients
# dimensionality equal to the nuimber of patients
#
def make_graph_distprop(a):

    d = [] #contains the graph in numerical form
    properties = 12 # this is for the number of properties - hardcoded
 

    # read file in string s
    f = open(a, 'r')
    s = f.read()
    f.close()

    length = len(s)

    
    i = 0
    j = 0
    patients = 0
    while(i<length): #compute the number of patients
        
        if(s[i]=='\n'): patients += 1
        i += 1

    with open(a) as data_file: #read each element of the file as an integer or a float
       for line in data_file:
          d.append(line.strip().split(';')) #now d consists of elements of file s


    # column labels
    graph = ';'
    for count in range(0, properties):
        graph += str(count)
        graph += ';'
    graph += '\n'
    
    # make the graph string for the file
    for i in range(0, properties):  #row labels
        graph += str(i)
        graph += ';'

        for j in range(0,i+1):
            graph += '0;'


        #computing distance
        for j in range(i+1,properties):
            dist = compute_distance(d,i,j,patients,properties)
            graph += str(dist)
            graph += ';'
        graph += '\n'




    # write the graph in a file
    f = open('distpropo_graph.csv', 'w')
    f.write(graph)
    f.close()

    datafile = open('distpropo_graph.csv', 'r')
    datareader = csv.reader(datafile,delimiter=';')
    data = []

    for row in datareader:
        data.append(row)

    for i in range(1, properties):
        for j in range(1, properties+1):
            data[j][i]=data[i][j]


    f = open('distpropo_graph.csv', 'w')
    dist_graph = csv.writer(f, delimiter=';')
    rows = data
    dist_graph.writerows(rows)
    f.close()

    print('\n END')

    return


#MAIN
make_graph_distprop('thromv.csv')

