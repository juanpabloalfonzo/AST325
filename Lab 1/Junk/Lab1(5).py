# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:19:09 2019

@author: juanp
"""
#import numpy to use math operations
import numpy as np
#import mathplotlib for graphing
import matplotlib.pyplot as plt
#Import pandas module that allows to read data from excel sheets
import pandas as pd
#Locating which excels file to read
data_small=pd.read_excel (r'C:\Users\juanp\Documents\U of T\3rd Year\AST325\DataSmall.xlsx')
#Select specific column of spreadsheet
ds=data_small['Data']
data_large=pd.read_excel (r'C:\Users\juanp\Documents\U of T\3rd Year\AST325\DataLarge.xlsx')
#Select specific column of spreadsheet
dl=data_large['Data']
#Taking mean of small data set
sm=sum(ds)/1000
#Show what the mean is for data small
print("The mean of 'data small' is:", sm)

#Create an empty set to put results of while loop into that we will use to calculate standard deviation
A=[]
#Create an index for the while loop
i=0
#create a while loop to calculate the square difference between data points and the mean
while i< 999:
    #add square differences to empty list A
    A.append((ds[i]-sm)**2)
    i=i+1
sd=(sum(A)/999)**(1/2)
print("This is the standard deviation of 'data small':", sd)

#Now we do the same but for the data large
#Take the mean of data large
lm=sum(dl)/1000
print("This is the mean of 'data large':", lm)

#Create emoty set to put results of while loop 
B=[]
#create an index for the while loop
j=0
#create a while loop to calculate the square difference between data points and the mean
while j<999:
    #add square differences to empty list B
    B.append((dl[j]-lm)**2)
    j=j+1
#Calculate the standard deviation using output from while loop
ld=((sum(B)/999))**(1/2)
print("This is the standard deviation of 'data large':", ld)

#create scatter plot for data small
plt.plot(ds, 'bo')
#x axis title
plt.xlabel('Measurement Number')
#y axis title
plt.ylabel('Photon Count Rate')
plt.show()

#create histograph for data small
plt.subplot()
plt.hist(ds, bins=11)
#x axis title
plt.xlabel('Photon Count Rate')
#y axis title
plt.ylabel('Times Measured')
#Create empty list for output of poission function
R=[]
#create new index l
l=0
#create while loop to model the poission function
while l < 30:
    #resets base value of factorial
    fact = 1
    #define factorial function using for loop
    for j in range(1, l+1):
        fact = fact*j
    #Add calculated values to empty set R, scaled by 325 to better suit the data
    R.append(325*((sm**(l+1)/fact)*np.exp(-(sm))))
    l=l+1
#create the poission distrinution using list R
plt.plot(R)
#setting a range for our x axis to our area of interest
plt.xlim(xmin=0, xmax=11)
plt.show()

#create scatter plot for data large
plt.subplot()
plt.plot(dl, 'ro')
#x axis title
plt.xlabel('Measurement Number')
#y axis title
plt.ylabel('Photon Count Rate')
plt.show()

#create histograph for data large
plt.subplot()
plt.hist(dl)
#x axis title
plt.xlabel('Photon Count Rate')
#y axis title
plt.ylabel('Times Measured')
#Create empty list for output of poission function
S=[]
#create new index p
p=0
#create while loop to model the poission function
while p < 30:
    #resets base value of factorial
    fact = 1
    #define factorial function using for loop
    for j in range(1, p+1):
        fact = fact*j
    #Add calculated values to empty set S, scaled by 325 to better suit the data
    S.append(325*((lm**(p+1)/fact)*np.exp(-(lm))))
    p=p+1
#create the poission distrinution using list S
plt.plot(S)
#setting a range for our x axis to our area of interest
plt.xlim(xmin=10, xmax=41)


    
        