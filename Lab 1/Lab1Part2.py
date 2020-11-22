# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:35:28 2019

@author: juanp
"""
import matplotlib.pyplot as plt
import numpy as np

#Create a set of all the measurement results
X=[38.91, 37.14, 38.19, 41.03, 34.86,
 37.33, 35.16, 37.96, 36.93, 40.41,
 29.50, 37.33, 41.84, 37.53, 34.12,
 34.11, 37.94, 34.43, 36.68, 41.31,
 39.61, 35.48, 34.98, 39.05, 39.62,
 37.96, 39.02, 37.47, 33.76, 36.51]
#Take the sum of all the elements of inside the measurement result set and divide by number of elements, in this case 30
M=sum(X)/30
#Show the mean
print("The mean is:", M)
#Formula for standard deviation 
#Create an index i to be the number of the element in the set
i=0
#Create an empty list to fill with the outputs of the while loops
S=[]
#Create a while loop that will calculate standard deviations. Setting i<30 as the set contains 30 elements
while i < 30:
    #Find the difference between the element in the the measurement set and the mean
    S.append((X[i]-M)**2)
    i = i + 1
#Calculate the standard deviation by taking the sum of the output set of the while loop and divide this by 29 and then take the square root
SD= (sum(S)/29)**(1/2)
#show the standard deviation 
print ("The Standard Deviation is:", SD)

#Create list with errors
Y=[1.41, 0.36, 0.69, 3.53, 2.64, 0.17, 2.34, 0.46, 0.57, 2.91, 8.00, 0.17, 4.34, 0.03, 3.38, 3.39, 0.44, 3.07, 0.82, 3.81, 2.11, 2.02, 2.52, 1.55, 2.12, 0.46, 1.52, 0.03, 3.74, 0.99]
#Calculate weighted mean using while loop
#Use j as an index
j=0
#Empty set to put outputs of numerator of weighted mean equation
N=[]
#Empty set to put outputs of denominator of weighted mean
D=[]
while j<30:
    #Numerator of weighted mean equation and put into list N
    N.append(X[j]/(Y[j])**2)
    #Denominator of weighted mean equation and put into list D
    D.append(1/Y[j]**2)
    j=j+1
#Take sum of N list and D list and divide to find weighted average 
WM=(sum(N)/sum(D))
print("This is the Weighted Mean:", WM)
#Calculate weighted standard deviation using formula
WS=(1/sum(D))**(1/2)
print("This is the Weighted Standard Deviation:", WS)

#Scatter plot of Distance(pc) vs Measurement
plt.subplot() 
plt.plot(X, 'go')
#X axis title
plt.xlabel('Number of Measurement')
#Y axis title
plt.ylabel('Distance (pc)')
#Title of graph
plt.title('Distance to a Nearby Star')
#Print graph
plt.show()

#Histrograph of number of measurements vs Distance (pc)
plt.subplot()
plt.hist(X, bins=7)
#X axis title
plt.xlabel('Distance (pc)')
#Y axis title
plt.ylabel('Number of Measurements')
#Title of graph
plt.title('Distance to a Nearby Star')
#Print Histograph
plt.show() 

#For Step 4 we calculate the mean 
#Create a new list of the photon count rate 
Z=[13, 17, 18, 14, 11, 8, 21, 18, 9, 12, 9, 17, 14, 6, 10, 16, 16, 11, 10, 12, 8, 20, 14, 10, 14, 17, 13, 16, 12, 10]
P=sum(Z)/30
print("This is the start of part 2")
print("The mean is:", P)

#Calculate Standard Deviation
k=0
#Create an empty list to fill with the outputs of the while loops
Q=[]
#Create a while loop that will calculate standard deviations. Setting i<30 as the set contains 30 elements
while k < 30:
    #Find the difference between the element in the the measurement set and the mean
    Q.append((Z[k]-P)**2)
    k = k + 1
#Calculate the standard deviation by taking the sum of the output set of the while loop and divide this by 29 and then take the square root
SD2= (sum(Q)/29)**(1/2)
print ("The Standard Deviation is:", SD2)

#Create Plot 5, histograph
plt.subplot()
plt.hist(Z, bins=7)
#X axis title
plt.xlabel('Number of Photons per Second')
#Y axis title
plt.ylabel('Number of Measurements')
#Title of graph
plt.title('Photon Count Rate with 1 Second Integration Time')
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
    #Add calculated values to empty set R, scaled by 5 to better suit the data, set mean to 12 as in figure 
    R.append(5*((12**(l+1)/fact)*np.exp(-(12))))
    l=l+1
#create the poission distrinution using list R
plt.plot(R)
    


    