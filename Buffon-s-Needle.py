import random
import math
import numpy as np



L=2 #Needle length
wintimes=0 #times that Needle has been found
beggining_of_needle=0
end_of_needle=0
n=0 #number of Needle we gonna test
d=5 # lines distance

n=int(input("how many test do want?"))

for i in range(1, n+1):

    center_of_needle=10*random.random()
    theta=((L/2)*math.cos(math.pi*(random.random()-0.5)))
    end_of_needle         =   center_of_needle   +   theta
    beggining_of_needle   =   center_of_needle   -   theta
  
    if end_of_needle <5 and beggining_of_needle>5:
        wintimes=wintimes+1
    if beggining_of_needle <5 and end_of_needle>5:
        wintimes=wintimes+1
    if beggining_of_needle >10 or end_of_needle >10:
        wintimes=wintimes+1
    if beggining_of_needle <0 or end_of_needle <0:
        wintimes=wintimes+1
    

P=wintimes/n
pi_from_exprience=(2*L/d/P)
pi_relative_error=abs((pi_from_exprience-math.pi)/math.pi)
print("pi from exprience = "  + str(pi_from_exprience))
print("pi relative error = "  + str(pi_relative_error))
print("times the needles have been found "  + str(wintimes)  + "  from  " + str(n))   
print("probablity = "  + str(P))
