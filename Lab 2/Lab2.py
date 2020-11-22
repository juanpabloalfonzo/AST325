# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:18:33 2019

@author: juanp
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import spreadsheet which contains pixel count data for each light source
data=pd.read_excel (r'C:\Users\juanp\Documents\U of T\3rd Year\AST325\Lab 2\Lab2.xlsx')
#Reading incandescent light bulb data from spreadsheet
I=data['Incandescent']
#Reading Neon data from spreadsheet
N=data['Neon']
#Reading Hydrogen data from spreadsheet
H=data['Hydrogen']
#Reading Fluorescent data from spreadsheet
F=data['Fluorescent']  
#Reading Sun data from spreadsheet
S=data['Sun'] 

#create index for while loop to find peaks of hydrogen
i=1
#empty set for output of peak while loop
HP=[]
#emoty set for x values of peaks
HPL=[]
#define a threshold for the data set
thresh1=3500  

while i<len(H)-1:
    if H[i]>H[i+1] and H[i]>H[i-1] and H[i]>thresh1: 
        HP.append(H[i])
        HPL.append(i)
    i=i+1
print('These are the peaks for Hydrogen:',HP)
print('These are the locations of the Hydrogen Peaks', HPL)

#create function that will be helpful to compute valleys
j=1 #index for function

def minInter(DataList,start,end): #start and end are where peaks are located
    j=start+1 #To be able to compare j-1
    mins=[] #empty set for the min values to go into
    while j<end: #while loop that finds all min values in a specific region
        if DataList[j]<DataList[j+1] and DataList[j]<DataList[j-1]:
            mins.append(DataList[j])
        j=j+1
    global themin
    themin=min(mins) #taking the minimum of the list of minimums 
    return(themin) #returning this absolute min value

#Function to find index value of valleys
def minPosition(DataList,Value):
    j=0
    global position
    while j<len(DataList)-1:
        if DataList[j]==Value: position=j
        j=j+1
    return(position)

def plot_vert(x):
    plt.axvline(x, color='red', ls='-.')  


#def centroid(V, VL,vl):
#    k=vl
#    Num2=[]
#    Dem=[]
#    global centroidl
#    while k<vl+2:
#        Num2.append(V[k]*VL[k])
#        Dem.append(VL[k])
#        k=k+1
#    centroidl=(sum(Num2)/(sum(Dem))
#    return(centroidl)
        
        
    

#To find min simpy use the function on the Hydrogen List
#in the desired regions between the peaks
HV=[]
HV.append(807.5)
i=0
while i<len(HP)-1:
    HV.append(minInter(H,HPL[i],HPL[i+1]))
    i=i+1
HV.append(609)
print('These are the Valleys for Hydrogen:',HV)

i=1
HVL=[]
HVL.append(618)
while i< len(HV)-1:
    HVL.append(minPosition(H,HV[i]))
    i=i+1
HVL.append(1972)
print('These are the locations of the Valleys of Hydrogen', HVL)

#Weighted Mean for Hydrogen
d=0 #Create an index
Centroids=[]
while d<len(HV)-1:
    Centroids.append(((HV[d]*HVL[d])+(HV[d+1]*HVL[d+1]))/(HV[d]+HV[d+1]))
    d=d+1
print('These are centroids of Hydrogen:', Centroids)

plt.subplot
plt.plot(H)
plt.plot(HPL,HP, 'ro')
plt.plot(HVL,HV,'bo')
i=0
while i<len(Centroids):
    plot_vert(Centroids[i])
    i=i+1
plt.show()

#Neon
#Peak
k=1
NP=[]
NPL=[]
thresh2=7800
while k<len(N)-1:
    if N[k]>N[k+1] and N[k]>N[k-1] and N[k]>thresh2:
        NP.append(N[k])
        NPL.append(k)
    k=k+1
print('These are peaks for Neon:',NP)
print('These are peak positions for Neon:',NPL)
#Valleys
l=0
NV=[]
while l<7:
    NV.append(minInter(N,NPL[l],NPL[l+1]))
    l=l+1

NV.append(4793)

p=8
while p<len(NPL)-1:
    NV.append(minInter(N,NPL[p],NPL[p+1]))
    p=p+1
    
print('These are the Valleys for Neon:', NV)

NVL=[]
k=0
while k<len(NV):
    NVL.append(minPosition(N,NV[k]))
    k=k+1
print('These are the Valley Locations for Neon:',NVL)

NVL[7]=1415
NVL[11]=1524
NVL[9]=1481

#plt.plot(N)
#plt.plot(NPL,NP,'ro')
#plt.plot(NVL,NV, 'bo')




