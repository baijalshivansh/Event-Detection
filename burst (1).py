#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 00:15:21 2018

@author: shivansh
"""
import numpy as np
import pandas as pd

# Still have to write the code for finding the interval x between the tweets by storing tweets in dataframe
#have to ask sir about the choice of values of p a1 and a2

#finding a sequence of states
q=[]
p=0.3
a1=0.1
a2=0.2
n=5
x=[2,5,1,10,7]
mat=np.zeros((2,n))
for j in range(0,n) :
    if (j==0) :
        mat[0][j]=(1-p)*(a1*(2.7**(-a1*x[j])));
        mat[1][j]=p*(a2*(2.7**(-a2*x[j])))
    else :
        mat[0][j]=max((mat[0][j-1]*(1-p)),(mat[1][j-1]*p))*(a1*(2.7**(-a1*x[j])));
        mat[1][j]=max((mat[0][j-1]*p),(mat[1][j-1]*(1-p)))*(a2*(2.7**(-a2*x[j])));
    if(mat[0][j]>=mat[1][j]) :
        q=q+["L"]
    else :
        q=q+["H"]
        

