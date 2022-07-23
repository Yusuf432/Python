#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


wcat=pd.read_csv("wc-at.csv")


# In[4]:


wcat


# In[7]:


#plotting for waist circumference
sns.distplot(wcat.Waist)
plt.ylabel("density");


# In[8]:


#plotting for Adipose Tissue
sns.distplot(wcat.AT)
plt.ylabel("Density");


# In[9]:


# WC
wcat.Waist.mean() , wcat.Waist.median()


# In[10]:


# AT
wcat.AT.mean() , wcat.AT.median()


# In[ ]:




