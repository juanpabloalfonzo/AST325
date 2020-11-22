import numpy as np
import matplotlib.pyplot as plt

#Define a List with Centroids Pixel Position called "Centroids"     
#Define a List that has every element in Centroids but squared called CentroidsSquared 
#Define a List that contains all the corresponding wavlengths of the centroids 
#called "Wavelengths"



#Define Matricies for Linear Fitting
ma=np.array([[sum(CentroidsSquared),sum(Centroids)],[sum(Centroids),len(Wavelength)]])
mc=np.array([[sum(CentroidsWavlenght)],[sum(Wavelength)]])
#Inverse of ma
mai=np.linalg.inv(ma)
#Slope and y-intercept
md=np.dot(mai,mc)

# Overplot the best fit
#Extract m and c using their matrix element
m = md[0,0]
c = md[1,0]

#While loop that generates the line of best fit
i=0
TLB=[] #empty list where y values of line will go
while i<len(Centroids):
    TLB.append(m*Centroids[i] +c) #Generating y values for the line
    i=i+1

#Creating Plot for Line of Best Fit
plt.subplot()
plt.plot(Centroids,LB) #Plots line of best fit
plt.plot(Centroids,Wavelength, 'ro') #Plots points of centroids versus wavelength
#Prints m and c value on the graph
plt.text(100,630,'m = {:.3f}\nc = {:.3f}'.format(m,c))
plt.title('Line of Best Fit of Neon Spectrum')
plt.xlabel('Pixel Number')
plt.ylabel('Wavlenghts (nm)')
plt.show()