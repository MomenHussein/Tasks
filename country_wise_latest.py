#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[59]:


data = pd.read_csv("country_wise_latest.csv")
"""y = np.array(data[0:186])
x = np.array(['Country/Region','Confirmed','Deaths','Recovered','Active','New cases	New deaths','New recovered	Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','Confirmed last week','1 week change','1 week % increase','WHO Region'])"""


# In[24]:


data


# In[25]:


data.isnull().sum()


# In[26]:


x


# In[27]:


y


# In[62]:


column_names = ["Confirmed", "Deaths", "Recovered", "Active"]
data[column_names].sum().plot(kind="bar")


# In[63]:


data[column_names].sum().plot()


# In[71]:


country_deaths = data[['Country/Region', 'Deaths']].sort_values(by='Deaths', ascending=False)
plt.bar(country_deaths['Country/Region'].head(10), country_deaths['Deaths'].head(10))
plt.xticks(rotation=80)
plt.show()


# In[72]:


country_deaths = data[['Country/Region', 'Confirmed']].sort_values(by='Confirmed', ascending=False)
plt.bar(country_deaths['Country/Region'].head(10), country_deaths['Confirmed'].head(10))
plt.xticks(rotation=80)
plt.show()


# In[73]:


country_deaths = data[['Country/Region', 'Recovered']].sort_values(by='Recovered', ascending=False)
plt.bar(country_deaths['Country/Region'].head(10), country_deaths['Recovered'].head(10))
plt.xticks(rotation=80)
plt.show()


# In[74]:


country_deaths = data[['Country/Region', 'Active']].sort_values(by='Active', ascending=False)
plt.bar(country_deaths['Country/Region'].head(10), country_deaths['Active'].head(10))
plt.xticks(rotation=80)
plt.show()


# In[95]:


plt.hist(country_deaths['Active'].head(10))
plt.xticks(rotation=80)
plt.show()


# In[92]:


data = pd.read_csv('country_wise_latest.csv')
recovered = data["Recovered"].sum()
death = data["Deaths"].sum()

data = [recovered, death]
labels = ["Recovered cases", "Deaths"]

plt.pie(data, labels=labels, autopct="%.2f%%")


# In[1]:


from flask import Flask, render_template, request
app = Flask(import_name = __name__) # to return this current file to the flask application (__name__) means the name of current file

# creating routes
# first getting the html template
@app.route('/', methods=["GET"]) # '/' it's the beggining of the program(or hosting) , I am here telling flask when to call home function and slash is the default path for web application (like route in linux) , to let the key value appears in url because it's not private information and to save the conversation with the chatbot , post method doesn't save and hide the key value in the url from the user
def home():
  return render_template("i/home/momen/Downloads/files/corona-free-dark-bootstrap-admin-template-master/template/index.html") # index.htlm is the page which we will render and open in this function to put chatbot in it to run the chatbot in the page , it means print it to the user screen

@app.route('/get', methods=["GET"]) # to get the response from chatbot , because the method that made in template wich will print the chatbot response is called response
def get_response():
    return data[column_names].sum().plot() # to get the response from the chatbot to the user input

if __name__ == '__main__':
  app.run(debug = True)
  
get_response()


# In[ ]:




