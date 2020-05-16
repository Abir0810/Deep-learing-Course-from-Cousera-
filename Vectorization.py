#!/usr/bin/env python
# coding: utf-8

# # Vectorize

# In[28]:


#It mainly calculate matrix or calculate vector 
# to use computation efficient we use vectorize
#used python code for faster code without loop
# we used numpy see the vectorization 


# In[29]:


import numpy as np


# In[30]:


import time


# In[31]:


num=1000000


# In[32]:


a=np.random.random(num)
b=np.random.random(num)


# In[33]:


start=time.time()
c=np.dot(a,b)
end=time.time()
print(c)
print("vectorize :"    +    str((end-start)*1000)+'ms')


# # Non Vectorize

# In[34]:


start=time.time()
c=0
for i in range(num):
    c += a[i]*b[i]
end=time.time()
print(c)
print("Loop :"    +    str((end-start)*1000)+'ms')


# In[ ]:




