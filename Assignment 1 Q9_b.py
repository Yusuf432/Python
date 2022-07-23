#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv("Q9_b.csv")
data


# In[3]:


data2=data.iloc[:,1:]
data2


# In[4]:


data2.skew()


# In[5]:


data2.kurt()


# In[ ]:




