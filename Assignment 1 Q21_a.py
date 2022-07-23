#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


cars=pd.read_csv("Cars.csv")


# In[3]:


cars


# In[8]:


sns.distplot(cars.MPG,label="Cars")
plt.xlabel("mpg")
plt.ylabel("Density")
plt.legend();


# In[9]:


cars.MPG.mean()


# In[10]:


cars.MPG.median()


# In[12]:


cars.MPG.std()


# In[ ]:




