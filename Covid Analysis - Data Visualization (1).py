#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns


# In[15]:


#Loading The Dataset
dataset_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(dataset_url)


# In[16]:


#Check The DataFrame
df.head()
df.tail()


# In[ ]:


#Check The Shape Of DataFrame
df.shape  #(rows,columns)


# In[23]:


#Pre Processing
df = df[df.Confirmed > 0]
df.head()
df[df.Country == 'India']


# In[24]:


#Global Spread Of COVID-19
fig = px.choropleth(df,locations = 'Country',locationmode= 'country names',color='Confirmed',animation_frame='Date')
fig.update_layout(title_text="Global Spread Of Covid19")
fig.show()


# In[25]:


#Global Deaths From Covid 19
fig = px.choropleth(df,locations='Country',locationmode='country names',color='Deaths',animation_frame='Date')
fig.update_layout(title_text="Global Death From Covid19")
fig.show()


# In[26]:


#Visualizing Infection Rate
df_india = df[df.Country == 'India']
df_india = df_india[['Date','Confirmed']]
df_india['Infection Rate'] = df_india['Confirmed'].diff()
px.line(df_india,x='Date',y = ['Confirmed','Infection Rate'])
#df_india['Infection Rate'].max()


# In[28]:


#Maximum Infection Rate For All Countries
countries = list(df['Country'].unique())
max_infection_rate = []

for i in countries: 
    MIR = df[df.Country == i].Confirmed.diff().max()
    max_infection_rate.append(MIR)
df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['Max Infection Rate']= max_infection_rate

px.bar(df_MIR,x='Country',y='Max Infection Rate',color='Country',title='Global Infection Rate',log_y=True)


# In[29]:


# Nation Wide Lockdown Impact
india_lockdown_start = '25-03-2020'
india_lockdown_month_later = '25-04-2020'
df_india = df[df.Country == 'India']
df_india['Infection Rate'] = df_india.Confirmed.diff()
fig = px.line(df_india,x='Date',y='Infection Rate',title='Before And After Lockdown')
fig.show()


# In[30]:


#Adding Lines
# Nation Wide Lockdown Impact
india_lockdown_start = '25-03-2020'
india_lockdown_month_later = '25-04-2020'
df_india = df[df.Country == 'India']
df_india['Infection Rate'] = df_india.Confirmed.diff()
fig = px.line(df_india,x='Date',y='Infection Rate',title='Before And After Lockdown')
fig.add_shape(
    dict(
        type="line",x0 = india_lockdown_start,y0=0,x1=india_lockdown_month_later,y1=df_india['Infection Rate'].max() ,line = dict(color='black',width=2)
))
fig.add_annotation(
    dict(
    x = india_lockdown_start,y = df_india['Infection Rate'].max(),text='Starting date of the lockdown in India')
)

fig.add_shape(dict(type = 'line',x0 = india_lockdown_month_later,y0=0,x1=india_lockdown_month_later,y1=df_india['Infection Rate'].max(),line = dict(color='orange',width=2)))
fig.add_annotation(
    dict(
    x = india_lockdown_month_later,y=0,text='A Month Later')
)
fig.show()


# In[31]:


#Impact Of Nationwide Lockdown On Death Rate
df_india['Deaths Rate'] = df_india.Deaths.diff()
fig = px.line(df_india,x = 'Date',y = ['Infection Rate','Deaths Rate'])
df_india['Infection Rate'] = df_india['Infection Rate']/df_india['Infection Rate'].max()
df_india['Deaths Rate'] = df_india['Deaths Rate']/df_india['Deaths Rate'].max()
fig = px.line(df_india,x='Date',y = ['Infection Rate','Deaths Rate'])
fig.show()


# In[4]:


df.head()


# In[18]:


sns.relplot(x="Deaths",y="Recovered",hue="Confirmed",data=df)
plt.ylim(0, 5000000)
plt.xlim(0, 150000)


# In[17]:


sns.boxplot(data=df)


# In[15]:


sns.violinplot(x='Deaths', y='Country', data=df.tail())


# In[14]:



# Density Plot
sns.kdeplot(df.Deaths, df.Recovered)


# In[3]:


df_india = df[df.Country == 'India']


# In[28]:


sns.violinplot(x='Deaths', y='Country', data=df_india)


# In[22]:


sns.set(style="dark") 
sns.lineplot(x="Deaths", 
             y="Recovered", 
              
             data=df)


# In[43]:


sns.boxplot(x ='Deaths', y ='Country', data = df_india)


# In[5]:


sns.jointplot(x ='Deaths', y ='Recovered', data = df_india)


# In[12]:


sns.rugplot(df['Deaths'])

