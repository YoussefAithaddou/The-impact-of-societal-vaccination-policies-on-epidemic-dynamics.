#!/usr/bin/env python
# coding: utf-8

# In[34]:


from matplotlib import pyplot as plt
import math
from pylab import *
from scipy.integrate import quad

b=1.6e-5
G = 1e-8
R=1581.9

r = 0.1
u=b/r-b
T = 200

y=[0]*T
w=[0]*T
k=[0]*T

a=1-1/(R*(1-r))
P= [[a]*(T+2)]*1001
h=[[1]*(T+1)]*1001
F=[[1]*(T+1)]*1001
F1=[[0]*(T+1)]*1001
S= [[1500]*(T+1)]*1001
o=7.4e-6*R/(1-7.4e-6)

I = [[200]*(T+1)]*1001
R = [[700]*(T+1)]*1001

l=0.1
E=[[0]*(T+1)]*1001



#Calculate S, I and R
for j in range (0,1000):
    
    for i in range (1,T+1):
       
        S[j][i]=u*(1-P[j][i-1])-b*S[j][i-1]*I[j][i-1]-u*S[j][i-1]+ S[j][i-1]
        I[j][i]=(b*S[j][i-1]-G-u)*I[j][i-1]+I[j][i-1]
        F[j][i]=-(u+b*I[j][i-1])*F[j][i-1]+F[j][i-1]
        F1[j][i]=u*F[j][i-1]+ F1[j][i-1]
        R[j][i] = u*P[j][i-1] +(1-u)*R[j][i-1]
  
    for i in range (0,T+1):
    
        #print(P[j][i])
        h[j][i]=(1/F[j][i])*(F1[j][T]+ u*F[j][T]/(u+b*I[j][T])-F1[j][i])
        
        m=P[j][i]-l*(r-h[j][i])
        
        #calculate the probability of vaccination p
        P[j+1][i]= max([min([m,1]),0])
       
    
   

    
for n in range (10):
    for t in range (T+1):
        E[n][t]= P[n][t]*r + (1-P[n][t])* h[n][t] - min(r, h[j][i])
        
        


# In[29]:


k


# In[ ]:




