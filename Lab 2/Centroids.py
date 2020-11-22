#Weighted Mean for Some Spectra
d=0 #Create an index
Centroids=[] #Empty list to record centroid pixel positons
#While loop that excecutes the weighted mean calculation 
#Refer to Appendix A to see what the NV and NVL list contain 
while d<len(NV):
    #Weighted mean calculation with the valley positions being the x values
    #and their measured intensity being the weights
    Centroids.append(((NV[d]*NVL[d])+(NV[d+1]*NVL[d+1]))/(NV[d]+NV[d+1]))
    d=d+2 #pairing of valleys to find only one centroid per pair
print('These are centroids of this spectra:', Centroids)