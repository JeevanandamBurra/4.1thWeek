
# coding: utf-8

# ## 1. Write a function so that the columns of the output matrix are powers of the input                vector.  
# The order of the powers is determined by the increasing boolean argument. Specifically,             when increasing is False, the i-th output column is the input vector raised element-wise              to the power of N - i - 1.  
#  
# HINT: Such a matrix with a geometric progression in each row is named for Alexandre               Theophile Vandermonde. 

# In[1]:


import numpy as np


# In[93]:


# Vandm function which accepts one dimensional array i.e x and power and v indicates increasing value
def vandm(x,n,v):
    x_arr=np.array(x)
    # empty array
    x=[]
    # Here to check wether it is having atleast one dimentione or not
    if x_arr.ndim != 1:
        raise ValueError("x must be a one-dimensional array or sequence.")
    # Here we will be checking wether user has passed power number or not of not will set len() array will be n value
    if n is None:
        n = len(x_arr)
    # If Increasing if True will loop through and reshape the array
    if v is True:
        for i in x_arr:
            for j in range(n):
                x1=pow(i,int(j))
                x.append(x1)
                                    
        return np.array(x).reshape(len(x_arr),n)
    else:# If Increasing if Flase will loop through and reshape the array
        for i in x_arr:
            for j in range(n):
                x1=pow(i,int(n-j-1))
                x.append(x1)
                                    
        return np.array(x).reshape(len(x_arr),n)
    


# In[94]:


x=[1,2,3,4]
x1=np.array(x)
vandm(x1,2,False)


# In[90]:


x=[1,2,3,4]
x1=np.array(x)
np.vander(x1,2)

