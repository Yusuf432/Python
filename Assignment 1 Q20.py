#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm


# In[10]:


cars=pd.read_csv("Cars.csv")


# In[11]:


cars


# In[12]:


sns.boxplot(cars.MPG)


# In[13]:


#P(MPG>38)
1-stats.norm.cdf(38,cars.MPG.mean(),cars.MPG.std())


# In[14]:


#P(MPG<40)
stats.norm.cdf(40,cars.MPG.mean(),cars.MPG.std())


# In[15]:


# P (20<MPG<50)
stats.norm.cdf(0.50,cars.MPG.mean(),cars.MPG.std())-stats.norm.cdf(0.20,cars.MPG.mean(),cars.MPG.std())     


# In[ ]:




