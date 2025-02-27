#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


a1d=np.array([1,2,3,89,900,78])


# In[4]:


a1d


# In[5]:


a1d.ndim


# In[6]:


a2d=np.array([[1,2,3,89],[4,5,6,98]])



# In[7]:


a2d.shape
a2d.ndim


# In[7]:


a2d.size


# In[8]:


a3d=np.array([[[1,2,3,9],[4,5,6,7],[6,7,8,4]],[[1,2,3,2],[4,5,6,78],[6,7,8,90]]])


# In[9]:


a3d.size


# In[10]:


a3d.dtype


# In[11]:


type(a3d)


# In[12]:


a3d.size


# In[13]:


import pandas as pd


# In[14]:


df=pd.DataFrame(a2d)


# In[15]:


df


# In[ ]:





# #Creating numpy Arrays

# In[16]:


#ones arrays creat 
ones=np.ones((3,2))


# In[17]:


ones.dtype


# #zeroes
zeros=np.zeros((2,3))
# In[18]:


zeros


# In[ ]:




