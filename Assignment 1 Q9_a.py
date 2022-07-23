#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


data=pd.read_csv("Q9_a.csv")
data


# In[5]:


#skewness
data.skew()


# In[6]:


data.kurt()


# In[ ]:




