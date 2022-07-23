#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import stats
from scipy.stats import norm


# In[2]:


#Z scores of  90% confidence interval
stats.norm.ppf(0.95)


# In[4]:


#Z scores of 94% confidence interval
stats.norm.ppf(0.97)


# In[5]:


# Z score of 60% confidence interval
stats.norm.ppf(0.8)


# In[ ]:




