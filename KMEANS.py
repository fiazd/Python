#Daanish Fiaz
#KMeans Clustering Program
import matplotlib
import matplotlib.pyplot as plt
import csv
import math
import random
from mpl_toolkits.mplot3d import Axes3D

#First part is clustering, then we need to plot the clusters
#We first want to pull out h8 and h10 
file = open("expression_data.csv")
k = 3
finalk = 3
csvfile = csv.reader(file)
#iterate over csvfile
h9list = []
h18list = []
conlist = []
#Go over each row and get the data
for row in csvfile:
    conlist.append(row[3])
    h9list.append(row[4])
    h18list.append(row[5])
    
#remove labels h9 and h18 from element
del h9list[0]
del h18list[0]
del conlist[0]

mergedlist = h9list + h18list #+ conlist

for i in range(len(h9list)):
    h9list[i] = float(h9list[i])
    h18list[i] = float(h18list[i])
    conlist[i] = float(conlist[i])
    mergedlist[i] = float(mergedlist[i])

lenh9 = len(h9list)
lenh18 = len(h18list)
lencon = len(conlist)
file.close()
#euclidean distance function, checked to make sure this is working correctly, it is.
def findED(num1, centroidnum):
    distance = 0
    distance += (float(num1) - float(centroidnum))**2
    distance = math.sqrt(distance)
    return distance

#initialize centroids, with random values
centroids = []
for i in range(k):
    centroids.append(mergedlist[random.randint(1,lenh9)])
#now we have our three initial random values
#now for each point in the dataset, we need to find the nearest centroid, the closest is assigned to that cluster
j = 1
min_distance = 0
#Start of main loop
#for each point find the nearest centroid, and assign that point to the cluster corresponding with the centroid
cluster1 = []
cluster2 = []
cluster3 = []
smallest = 999999999999999
for k in range(len(mergedlist)):
    mdlist = []
    assignC = 0
    ed1 = findED(mergedlist[k], centroids[0])
    ed2 = findED(mergedlist[k], centroids[1])
    ed3 = findED(mergedlist[k], centroids[2])
    mdlist.append(ed1)
    mdlist.append(ed2)
    mdlist.append(ed3)
    smallest = min(float(l) for l in mdlist)
    assignC = mdlist.index(smallest)
    if (assignC == 0):
        cluster1.append(smallest)
    if(assignC == 1):
        cluster2.append(smallest)
    if(assignC == 2):
        cluster3.append(smallest)
#We are going to call this to recalc pd every time we find new centroids until the percent difference is less than .05%
def findDifference(newctemp, oldctemp):
    percentdiff = 0
    for i in range(len(newctemp)):
        percentdiff += (abs(newctemp[i] - oldctemp[i]) / ((newctemp[i] + oldctemp[i])/2)) * 100
    finalpd = percentdiff / len(newctemp)
    return finalpd


#Second loop to calculate 
difference = 1000
ideal = 0.05
oldcentroids = []
count = 0
iterationcount = 0
#while(difference > 0.05):
newcentroids = []
avg1 = (sum(cluster1)) / (len(cluster1))
avg2 = (sum(cluster2)) / (len(cluster2))
avg3 = (sum(cluster3)) / (len(cluster3))
newcentroids.append(avg1)
newcentroids.append(avg2)
newcentroids.append(avg3)
oldcentroids = newcentroids

while(difference > 0.05):
#Start while loop
    newcluster1 = []
    newcluster2 = []
    newcluster3 = []

    for a in range(len(mergedlist)):
        mdlist1 = []
        ed11 = 0
        ed21 = 0
        ed31 = 0
        smallest1 = 9999999999
        assignC1 = -1
        ed11 = findED(mergedlist[a], newcentroids[0])
        ed21 = findED(mergedlist[a], newcentroids[1])
        ed31 = findED(mergedlist[a], newcentroids[2])
        mdlist1.append(ed11)
        mdlist1.append(ed21)
        mdlist1.append(ed31)
        smallest1 = min(float(b) for b in mdlist1)
        assignC1 = mdlist1.index(smallest1)
        if(assignC1 == 0):
            newcluster1.append(smallest1)
        if(assignC1 == 1):
            newcluster2.append(smallest1)
        if(assignC1 == 2):
            newcluster3.append(smallest1)
    newcentroids1 = []
    avg11 = (sum(newcluster1)) / (len(newcluster1))
    avg21 = (sum(newcluster2)) / (len(newcluster2))
    avg31 = (sum(newcluster3)) / (len(newcluster3))
    newcentroids1.append(avg11)
    newcentroids1.append(avg21)
    newcentroids1.append(avg31)
    difference = findDifference(newcentroids1, newcentroids)
    newcentroids = newcentroids1
    iterationcount += 1
#Stop while loop
#Creating 3d scatter
##fig = plt.figure()
##ax = fig.add_subplot(111, projection = '3d')
#newcluster 1 2 and 3
#newcentroids1 1 2 and 3
#ax.scatter(newcluster1, newcluster2, newcluster3, c = 'r', marker = '+')
#ax.scatter(newcentroids1[0], newcentroids[1], newcentroids[2], c = 'g', marker = 'D')
##ax.set_xlabel('X Label')
##ax.set_ylabel('Y Label')
##ax.set_zlabel('Z Label')
##plt.show()
##    
print("K = " + str(finalk))
print("Completed in " + str(iterationcount) + " iterations.")

#Still trying to figure out how to plot this correctly, finish up tomorrow    
