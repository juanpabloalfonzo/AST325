#R Squared Value Calculation
averageY=sum(LB) #Using Line of Best Fit to Calculate Average Y

w=0 
ExpPred=[] #Empty List where numerator of line of R^2 eqaution will be put
while w<len(LB):
    #Wavelenght is the same list defined in the previous appendix
    ExpPred.append((LB[w]-Wavelenght[w])**2) 
    w=w+1
    
w=0
PredAv=[] #Empty List where denominator of line of R^2 eqaution will be put
while w<len(LB):
    PredAv.append((Wavelenght[w]-averageY)**2)
    w=w+1
    
rSquared=1-(sum(ExpPred)/sum(PredAv))
print("The R-Squared value for the Line Of Best Fit is",rSquared)