#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib as plt
import pandas as pd


# In[2]:


data = pd.read_csv("covid_19_clean_complete.csv")


# In[3]:


data


# In[4]:


data.isnull().sum()


# In[5]:


new_data = data


# In[14]:


new_data = new_data.drop('Province/State',axis = 1)


# In[15]:


new_data


# In[16]:


new_data.isnull().sum()


# In[ ]:




