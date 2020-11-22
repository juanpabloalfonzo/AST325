#Error Propogation for Line Of Best Fit
ErrorList=[] #Empty list for calculated error to go into
g=0
while g<len(LB):
    ErrorList.append((LB[g]-NW[g])**2)
    g=g+1

#Computation for sigma that appears in equation 3    
sigmaSquared=(1/(len(LB)-2))*sum(ErrorList)
sigma=(sigmaSquared)**(1/2)
print("The Error Propogation Value (sigma) is", sigma)

#Computation for sigma M that appears in equation 4
#Sigma M
sigmaM2=((len(CentroidsN))*(sigmaSquared))/((len(Centroids))
*(sum(CentroidsSquared))-(sum(Centroids))**2)
sigmaM=(sigmaM2)**(1/2)
print('This is the error of m:',sigmaM)

#Computation for sigma C that appears in equation 5
#Sigma C
sigmaC2=((sigmaSquared)*(sum(Centroids)))/((len(Centroids))
*(sum(CentroidsSquared))-(sum(Centroids))**2)
sigmaC=(sigmaC2)**(1/2)
print("This is the error of c:", sigmaC)