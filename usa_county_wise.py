#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import matplotlib as plt
import pandas as pd


# In[56]:


data = pd.read_csv("usa_county_wise.csv")


# In[57]:


data


# In[58]:


data.isnull().sum()


# In[59]:


new_data = data


# In[60]:


new_data


# In[61]:


new_data['FIPS'] = new_data['FIPS'].fillna(method='pad')


# In[63]:


new_data.isnull().sum()


# In[64]:


new_data['Admin2'] = new_data['Admin2'].fillna(value='Unassigned')


# In[65]:


new_data.isnull().sum()


# In[ ]:




