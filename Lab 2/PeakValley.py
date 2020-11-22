
#Peaks
k=1 #index for while loop
NP=[] #empty list for measured intensity of peaks to be placed in
NPL=[] #empty list for pixel positon of peak to be placed in
thresh2=7800 #threshold that should be slightly less than your lowest peak's 
             #measured intensity 
#While loop to find the peak's measured intensity and peak's pixel position             
while k<len(N)-1:
    if N[k]>N[k+1] and N[k]>N[k-1] and N[k]>thresh2: #defining conditions for a peak
        NP.append(N[k]) #Adding peaks' intensity to appropriate list
        NPL.append(k) #Adding peaks' pixel position to appropriate list
    k=k+1
print('These are peaks for this spectra:',NP)
print('These are peak positions for this spectra:',NPL)


#Define two functions that will help us find valleys

#Shift inputed value 7 units to the left
def LS1(z):
    LeShift1=z-7 
    return (LeShift1)

#Shift inputed value 8 units to the right
def RS1(o):
    LeShift2=o+7
    return (LeShift2)


#Valleys
NV=[] #empty list for measured intensity of valleys to be placed in
NVL=[] #empty list for pixel position of valleys to be placed in
i=0
while i<len(NPL):
    NV.append(N[LS1(NPL[i])]) #Shifts peak pixel position left and finds 
                              #corresponding measured intensity
    NV.append(N[RS1(NPL[i])]) #Shifts peak pixel position right 
                              #and finds corresponding measured intensity
    NVL.append(LS1(NPL[i])) #Shifts peak pixel position left
    NVL.append(RS1(NPL[i])) #Shifts peak pixel position right
    i=i+1

print('These are valleys for this spectra:',NV)
print('These are valley positions for this spectra:',NVL)