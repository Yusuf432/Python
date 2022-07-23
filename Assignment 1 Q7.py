#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


cars=pd.read_csv("Q7.csv")
cars=pd.DataFrame(cars)
cars


# In[31]:


print(cars.mean(numeric_only=True))


# In[32]:


print(cars.median(numeric_only=True))


# In[33]:


cars.Points.mode()


# In[34]:


cars.Score.mode()


# In[35]:


cars.Weigh.mode()


# In[36]:


#variance
print(cars.var(numeric_only=True))


# In[37]:


#standard deviation 
print(cars.std(numeric_only=True))


# In[38]:


#range
cars.describe()


# In[39]:


Points_Range=cars.Points.max()-cars.Points.min()
Points_Range


# In[41]:


Score_Range=cars.Score.max()-cars.Score.min()
Score_Range


# In[42]:


Weigh_Range=cars.Weigh.max()-cars.Weigh.min()
Weigh_Range


# In[46]:


f,ax=plt.subplots(figsize=(14,5))
plt.subplot(1,3,1)
plt.boxplot(cars.Points)
plt.title('Points')
plt.subplot(1,3,2)
plt.boxplot(cars.Score)
plt.title('Score')
plt.subplot(1,3,3)
plt.boxplot(cars.Weigh)
plt.title('Weigh')
plt.show()


# In[ ]:




