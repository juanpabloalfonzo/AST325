# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:54:40 2019

@author: juanp
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:18:33 2019

@author: juanp
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import astropy as at
from astropy.io import fits
#import aplpy as ap
 

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
SU=data['Sun'] 

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
def LS(x):
    LeShift=x-30
    return (LeShift)

def RS(y):
    RiShift=y+30
    return(RiShift)

def LS1(z):
    LeShift1=z-7
    return (LeShift1)

def RS1(o):
    LeShift2=o+7
    return (LeShift2)

def ValleyR(DataList1,x):
        VR=DataList1[x+30]
        return (VR)

#Function to find index value of valleys
def minPosition(DataList,Value):
    j=0
    global position
    while j<len(DataList)-1:
        if DataList[j]==Value: position=j
        j=j+1
    return(position)

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

def plot_vert(x):
    plt.axvline(x, color='red', ls='-.')  


#To find min simpy use the function on the Hydrogen List
#in the desired regions between the peaks
HV=[]
HVL=[]
i=0
while i<len(HPL):
    HV.append(H[LS(HPL[i])])
    HV.append(H[RS(HPL[i])])
    HVL.append(LS(HPL[i]))
    HVL.append(RS(HPL[i]))
    i=i+1

print('These are the Valleys for Hydrogen:',HV)
print('These are the locations of the Valleys of Hydrogen', HVL)

#Weighted Mean for Hydrogen
d=0#Create an index
Centroids=[]
while d<len(HV):
    Centroids.append(((HV[d]*HVL[d])+(HV[d+1]*HVL[d+1]))/(HV[d]+HV[d+1]))
    d=d+2
print('These are centroids of Hydrogen:', Centroids)

WH=[486.1, 656.2]
#plt.subplot
#plt.plot(H)
#plt.plot(HPL,HP, 'ro')
#plt.plot(HVL,HV,'bo')
#i=0
#while i<len(Centroids):
#    plot_vert(Centroids[i])
#    i=i+1
#plt.show()






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
NV=[]
NVL=[]
i=0
while i<len(NPL):
    NV.append(N[LS1(NPL[i])])
    NV.append(N[RS1(NPL[i])])
    NVL.append(LS1(NPL[i]))
    NVL.append(RS1(NPL[i]))
    i=i+1

print('These are valleys for Neon:',NV)
print('These are valley positions for Neon:',NVL)

d=0
CentroidsN=[]
while d<len(NV):
    CentroidsN.append(((NV[d]*NVL[d])+(NV[d+1]*NVL[d+1]))/(NV[d]+NV[d+1]))
    d=d+2
print('These are centroids of Neon:', CentroidsN)

CentroidsN2=[]
i=0
while i<len(CentroidsN):
    CentroidsN2.append((CentroidsN[i])**2)
    i=i+1
print('These are centroids of Neon Squared:', CentroidsN2)

NW=[585.294, 588.189, 594.483, 597.553, 602.999, 607.434, 609.616, 
    614.306, 614.306, 621.728, 626.310, 630.479, 633.433, 638.299, 640.225, 
    650.653, 650.653, 659.895, 667.828, 671.704, 692.947, 703.241]

#if len(NW)==len(CentroidsN):
#    print('Yay')

CentroidsNXY=[]
i=0
while i<len(CentroidsN):
    CentroidsNXY.append(NW[i]*CentroidsN[i])
    i=i+1
print('These are the Centroids of Neon with y value:', CentroidsNXY)


#plt.plot(N)
#plt.plot(NPL,NP,'ro')
#plt.plot(NVL,NV, 'bo')
#plt.xlim(xmin=1200,xmax=len(N))
#i=0
#while i<len(CentroidsN):
#    plot_vert(CentroidsN[i])
#    i=i+1
#plt.show()

#Define Matricies for Linear Fitting
ma=np.array([[sum(CentroidsN2),sum(CentroidsN)],[sum(CentroidsN),len(NW)]])
mc=np.array([[sum(CentroidsNXY)],[sum(NW)]])
#Inverse of ma
mai=np.linalg.inv(ma)
#Slope and y-intercept
md=np.dot(mai,mc)


# Overplot the best fit
m = md[0,0]
c = md[1,0]

i=0
LB=[]
while i<len(CentroidsN):
    LB.append(m*CentroidsN[i] + c)
    i=i+1

#plt.plot(CentroidsN,NW,'ro')
#plt.plot(CentroidsN,LB)
##plt.plot(Centroids,WH,'bo')
#plt.text(1500,680,'m = {:.3f}\nc = {:.3f}'.format(m,c))
#plt.title('Line of Best Fit of Neon Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Wavlenghts (nm)')
#plt.plot()
#plt.show()

#R Squared Value Calculation
averageY=sum(LB)

w=0
ExpPred=[]
while w<len(LB):
    ExpPred.append((LB[w]-NW[w])**2)
    w=w+1
    
w=0
PredAv=[]
while w<len(LB):
    PredAv.append((NW[w]-averageY)**2)
    w=w+1
    
rSquared=1-(sum(ExpPred)/sum(PredAv))
print("")
print("")
print("The R-Squared value for the Line Of Best Fit is",rSquared)





#Error Propogation for Line Of Best Fit
ErrorList=[]
g=0
while g<len(LB):
    ErrorList.append((LB[g]-NW[g])**2)
    g=g+1
    
sigmaSquared=(1/(len(LB)-2))*sum(ErrorList)
sigma=(sigmaSquared)**(1/2)
print("")
print("")  
print("The Error Propogation Value (sigma) is", sigma)

#Sigma M
sigmaM2=((len(CentroidsN))*(sigmaSquared))/((len(CentroidsN))*(sum(CentroidsN2))-(sum(CentroidsN))**2)
sigmaM=(sigmaM2)**(1/2)
print('This is the error of m:',sigmaM)

#Sigma C
sigmaC2=((sigmaSquared)*(sum(CentroidsN2)))/((len(CentroidsN))*(sum(CentroidsN2))-(sum(CentroidsN))**2)
sigmaC=(sigmaC2)**(1/2)
print("This is the error of c:", sigmaC)

TNR=at.io.fits.getdata(r'C:\Users\juanp\Documents\U of T\3rd Year\AST325\Lab 2\NeonCalibration.fit')
TND=TNR[250,:]

TN=[]
i=0
while i<len(TND):
    TN.append(TND[i])
    i=i+1

#plt.plot(TN)

i=0
TNP=[]
TNPL=[]
while i< len(TN)-1:
    if TN[i]>TN[i+1] and TN[i]>TN[i-1] and TN[i]>1200:
        TNP.append(TN[i])
        TNPL.append(i)
    i=i+1
#plt.plot(TNPL,TNP, 'ro')

#Valleys
TNV=[]
TNVL=[]
i=0
while i<len(TNPL):
    TNV.append(TN[LS1(TNPL[i])])
    TNV.append(TN[RS1(TNPL[i])])
    TNVL.append(LS1(TNPL[i]))
    TNVL.append(RS1(TNPL[i]))
    i=i+1

print('These are valleys for Telescope Neon:',TNV)
print('These are valley positions for Telescope Neon:',TNVL)

d=0
CentroidsTN=[]
while d<len(TNV):
    CentroidsTN.append(((TNV[d]*TNVL[d])+(TNV[d+1]*TNVL[d+1]))/(TNV[d]+TNV[d+1]))
    d=d+2
print('These are centroids of Telescope Neon:', CentroidsTN)

CentroidsTN2=[]
i=0
while i<len(CentroidsTN):
    CentroidsTN2.append((CentroidsTN[i])**2)
    i=i+1
print('These are centroids of Neon Squared:', CentroidsTN2)


TNW=[NW[0], NW[1], NW[3], NW[4], NW[5], NW[6], NW[7], NW[8], NW[10], NW[11], NW[12], 
     NW[13], NW[14]]

CentroidsTNXY=[]
i=0
while i<len(CentroidsTN):
    CentroidsTNXY.append(TNW[i]*CentroidsTN[i])
    i=i+1
print('These are the Centroids of Neon with y value:', CentroidsTNXY)

#Define Matricies for Linear Fitting
mat=np.array([[sum(CentroidsTN2),sum(CentroidsTN)],[sum(CentroidsTN),len(TNW)]])
mct=np.array([[sum(CentroidsTNXY)],[sum(TNW)]])
#Inverse of ma
Tmai=np.linalg.inv(mat)
#Slope and y-intercept
Tmd=np.dot(Tmai,mct)



# Overplot the best fit
Tm = Tmd[0,0]
Tc = Tmd[1,0]

i=0
TLB=[]
while i<len(CentroidsTN):
    TLB.append(Tm*CentroidsTN[i] + Tc)
    i=i+1

plt.subplot()
plt.plot(CentroidsTN,TNW,'ro')
plt.plot(CentroidsTN,TLB)
plt.plot(CentroidsTN,TNW, 'ro')
plt.text(100,630,'m = {:.3f}\nc = {:.3f}'.format(Tm,Tc))
plt.title('Line of Best Fit of Telescope Neon Spectrum')
plt.xlabel('Pixel Number')
plt.ylabel('Wavlenghts (nm)')
plt.show()

#R Squared Value Calculation
averageTY=sum(TLB)

w=0
TExpPred=[]
while w<len(TLB):
    TExpPred.append((TLB[w]-TNW[w])**2)
    w=w+1
    
w=0
TPredAv=[]
while w<len(TLB):
    TPredAv.append((TNW[w]-averageTY)**2)
    w=w+1
    
TrSquared=1-(sum(TExpPred)/sum(TPredAv))
print("")
print("")
print("The R-Squared value for the Line Of Best Fit (Telescope) is",TrSquared)

#Error Propogation for Line Of Best Fit
ErrorListT=[]
g=0
while g<len(TLB):
    ErrorListT.append((TLB[g]-TNW[g])**2)
    g=g+1
    
TsigmaSquared=(1/(len(TLB)-2))*sum(ErrorListT)
Tsigma=(TsigmaSquared)**(1/2)
print("")
print("")  
print("The Error Propogation Value (Tsigma) is", Tsigma)

#Sigma M
sigmaTM2=((len(CentroidsTN))*(TsigmaSquared))/((len(CentroidsTN))*(sum(CentroidsTN2))-(sum(CentroidsTN))**2)
sigmaTM=(sigmaTM2)**(1/2)
print('This is the error of m in telescope:',sigmaTM)

#Sigma C
sigmaTC2=((TsigmaSquared)*(sum(CentroidsTN2)))/((len(CentroidsTN))*(sum(CentroidsTN2))-(sum(CentroidsTN))**2)
sigmaTC=(sigmaTC2)**(1/2)
print("This is the error of c in telescope:", sigmaTC)

VR=at.io.fits.getdata(r'C:\Users\juanp\Documents\U of T\3rd Year\AST325\Lab 2\Vega.fit')
VA=VR[220,:] #Hydrogen and Hellium
ER=at.io.fits.getdata(r'C:\Users\juanp\Documents\U of T\3rd Year\AST325\Lab 2\EnifSpec.fit')
EA=ER[400,:] #Magnesium Iron Silicon 
NAR=at.io.fits.getdata(r'C:\Users\juanp\Documents\U of T\3rd Year\AST325\Lab 2\NaviSpec.fit')
NAA=NAR[250,:] #Hydrogen Hellium 
SR=at.io.fits.getdata(r'C:\Users\juanp\Documents\U of T\3rd Year\AST325\Lab 2\ScheatSpec.fit')
SRA=SR[370,:] #Oxygen 

i=0
V=[]
while i<len(VA):
    V.append(VA[i])
    i=i+1
    
i=0
E=[]
while i<len(EA):
    E.append(EA[i])
    i=i+1
    
i=0
NA=[]
while i<len(NAA):
    NA.append(NAA[i])
    i=i+1
    
i=0
S=[]
while i<len(SRA):
    S.append(SRA[i])
    i=i+1

i=1
VP=[]
VPL=[]
while i<200 :
    if V[i]<V[i+1] and V[i]<V[i-1] and V[i]<2500:
        VP.append(V[i])
        VPL.append(i)
    i=i+1
i=510
while i<515:
    if V[i]<V[i+1] and V[i]<V[i-1] and V[i]<1500:
        VP.append(V[i])
        VPL.append(i)
    i=i+1
plt.subplot()
plt.title('Vega Spectrum')
plt.xlabel('Pixel Number')
plt.ylabel('Measurred Signal')
plt.plot(VPL,VP,'ro')
plt.plot(V)
plt.show()
print(VPL)
i=100 
NAP=[]
NAPL=[]
while i<200:
    if NA[i]>NA[i+1] and NA[i]>NA[i-1] and NA[i]>2500:
        NAP.append(NA[i])
        NAPL.append(i)
    i=i+1

i=500
while i<600:
    if NA[i]>NA[i+1] and NA[i]>NA[i-1] and NA[i]>2200:
        NAP.append(NA[i])
        NAPL.append(i)
    i=i+1

#plt.plot(NA)
#plt.plot(NAPL,NAP,'ro')
    
EP=[] #Create an emplty list to store peaks
EPL=[]#Create an empty list to store where the peaks are from the data set are
i=50 #Create an index
while i<100: #Create a while loop to determine all peaks of the Hydrogen data set
    if E[i]<E[i+1] and E[i]<E[i-1] and E[i]<3500:
        EP.append(E[i])
        EPL.append(i)
    i=i+1
    
i=100 #Create an index
while i<175: #Create a while loop to determine all peaks of the Hydrogen data set
    if E[i]<E[i+1] and E[i]<E[i-1] and E[i]<4200:
        EP.append(E[i])
        EPL.append(i)
    i=i+1
    
i=200 #Create an index
while i<250: #Create a while loop to determine all peaks of the Hydrogen data set
    if E[i]<E[i+1] and E[i]<E[i-1] and E[i]<3700:
        EP.append(E[i])
        EPL.append(i)
    i=i+1
    
i=270 #Create an index
while i<310: #Create a while loop to determine all peaks of the Hydrogen data set
    if E[i]<E[i+1] and E[i]<E[i-1] and E[i]<3500:
        EP.append(E[i])
        EPL.append(i)
    i=i+1

#plt.plot(E)
#plt.plot(EPL,EP,'ro')

SV=[]
SVL=[]
i=1
while i<10:
    if S[i]<S[i+1] and S[i]<S[i-1] and S[i]<3000:
        SV.append(S[i])
        SVL.append(i)
    i=i+1

i=50
while i<110:
    if S[i]<S[i+1] and S[i]<S[i-1] and S[i]<3300:
        SV.append(S[i])
        SVL.append(i)
    i=i+1
    
i=210
while i<250:
    if S[i]<S[i+1] and S[i]<S[i-1] and S[i]<2600:
        SV.append(S[i])
        SVL.append(i)
    i=i+1
    
i=290
while i<300:
    if S[i]<S[i+1] and S[i]<S[i-1] and S[i]<2700:
        SV.append(S[i])
        SVL.append(i)
    i=i+1
    
i=320
while i<360:
    if S[i]<S[i+1] and S[i]<S[i-1] and S[i]<2600:
        SV.append(S[i])
        SVL.append(i)
    i=i+1
    
i=380
while i<400:
    if S[i]<S[i+1] and S[i]<S[i-1] and S[i]<2300:
        SV.append(S[i])
        SVL.append(i)
    i=i+1
    
i=450
while i<520:
    if S[i]<S[i+1] and S[i]<S[i-1] and S[i]<1400:
        SV.append(S[i])
        SVL.append(i)
    i=i+1
#plt.plot(S)
#plt.plot(SVL,SV,'ro')    

PS=[]
w=0
while w<len(SV):
    PS.append((Tm*SVL[w])+Tc)
    w=w+1
print('These are the wavelenghts of Scheat:', PS)


FP=[]
FPL=[]
i=0
while i< len(F)-1:
    if F[i]>F[i+1] and F[i]>F[i-1] and F[i]>15000:
        FP.append(F[i])
        FPL.append(i)
    i=i+1

plt.subplot(222)
plt.title('Fluorescent Light Spectrum')
plt.xlabel('Pixel Number')
plt.ylabel('Measured Signal')
plt.plot(F)
plt.plot(FPL,FP,'ro')
plt.show()
#
#plt.subplot()
#plt.plot(I)
#plt.title('Incandescent Light Bulb Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measured Signal')
#plt.show()
#
#plt.subplot()
#plt.plot(N)
#plt.title('Neon Light Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measured Signal')
#plt.show()
#
#plt.subplot()
#plt.plot(H)
#plt.title('Hydrogen Light Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measured Signal')
#plt.show()
#
#plt.subplot()
#plt.plot(F)
#plt.title('Fluorescent Light Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measured Signal')
#plt.show()
#
plt.subplot(221)
plt.plot(SU)
plt.title('Sun Spectrum')
plt.xlabel('Pixel Number')
plt.ylabel('Measured Signal')
plt.show()

#plt.subplot()
#plt.plot(V)
#plt.title('Vega Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measurred Signal')
#plt.show()
#
#plt.subplot()
#plt.plot(E)
#plt.title('Enif Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measurred Signal')
#plt.show()
#
#plt.subplot()
#plt.plot(NA)
#plt.title('Navi Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measurred Signal')
#plt.show()
#
#plt.subplot()
#plt.plot(S)
#plt.title('Scheat Spectrum')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measurred Signal')
#plt.show()
#
#plt.subplot()
#plt.plot(TN)
#plt.title('SGBI Spectrograph Neon')
#plt.xlabel('Pixel Number')
#plt.ylabel('Measurred Signal')
#plt.show()
#
#

plt.subplot(224)
plt.imshow(VR)
plt.plot()