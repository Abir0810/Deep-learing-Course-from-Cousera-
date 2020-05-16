#!/usr/bin/env python
# coding: utf-8

# # Broadcasting

# In[27]:


import numpy as np


# In[28]:


a=np.array([[56.0,0.0,4.4,68.0],
            [1.2,104.0,52.0,8.0],
            [1.8,135.0,99.0,0.9]])

print(a)
   


# In[29]:


cal=a.sum(axis=0)
print(cal)


# In[30]:


percentage=100*a/cal.reshape(1,4)
print(percentage)


# In[ ]:




