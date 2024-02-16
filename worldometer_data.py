#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import matplotlib as plt
import pandas as pd
from random import randint as rd


# In[2]:


data = pd.read_csv("worldometer_data.csv")


# In[3]:


data


# In[4]:


data.isnull().sum()


# In[5]:


new_data = data


# In[6]:


new_data['Continent'] = new_data['Continent'].fillna(value='missed')


# In[16]:


new_data['Population'] = new_data['Population'].fillna(value=new_data['Population'].mean())


# In[18]:


new_data['TotalRecovered'] = new_data['TotalRecovered'].fillna(method='bfill')


# In[19]:


new_data['ActiveCases'] = new_data['ActiveCases'].fillna(method='bfill')


# In[21]:


new_data['Tot Cases/1M pop'] = new_data['Tot Cases/1M pop'].fillna(value=((new_data['TotalCases']/new_data['Population'])*1000000))


# In[22]:


new_data['TotalDeaths'] = new_data['TotalDeaths'].fillna(method='bfill')


# In[23]:


new_data['Deaths/1M pop'] = new_data['Deaths/1M pop'].fillna(value=((new_data['TotalDeaths']/new_data['Population'])*1000000))


# In[32]:


new_data['TotalTests'] = new_data['TotalTests'].fillna(value=rd(new_data['TotalTests'].min(),new_data['TotalTests'].max()))


# In[33]:


new_data['Tests/1M pop'] = new_data['Tests/1M pop'].fillna(value=((new_data['TotalTests']/new_data['Population'])*1000000))


# In[37]:


new_data['NewCases'] = new_data['NewCases'].fillna(value=rd(new_data['NewCases'].min(),new_data['NewCases'].max()))


# In[39]:


new_data['NewDeaths'] = new_data['NewDeaths'].fillna(value=rd(new_data['NewDeaths'].min(),new_data['NewDeaths'].max()))


# In[44]:


new_data['NewRecovered'] = new_data['NewRecovered'].fillna(value=rd(new_data['NewRecovered'].min(),new_data['NewRecovered'].max()))


# In[47]:


new_data['NewRecovered'] = new_data['NewRecovered'].fillna(value=rd(new_data['NewRecovered'].min(),new_data['NewRecovered'].max()))


# In[48]:


new_data['Serious,Critical'] = new_data['Serious,Critical'].fillna(method='pad')


# In[49]:


new_data['WHO Region'] = new_data['WHO Region'].fillna(method='pad')


# In[50]:


new_data.isnull().sum()


# In[ ]:




