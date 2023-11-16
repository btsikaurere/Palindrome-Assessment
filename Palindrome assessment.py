#!/usr/bin/env python
# coding: utf-8

# In[34]:


#Import Libraries

import numpy as np

import pandas as pd

#load data

dataset=pd.read_excel("C:/Users/bless/Desktop/palindrom assessment/pone.0212445.s004.xlsx", skiprows=[0])

#data preview 
dataset


# In[6]:


#Check for Duplicates (I confirmed the data had no duplicates by below code) 
dataset_cleaned=dataset.drop_duplicates()
dataset_cleaned


# In[14]:


#Que 2(a)
total_PLHIV = dataset.loc[dataset['Estimate']=='Survey', 'NoPLHIV'].sum()
total_PLHIV


# In[39]:


#Que 2(b)
#Check if Xhariep is among districts
#dataset['District'].unique()

AVG_NoPLHIV=dataset.query("District == 'Xhariep'").groupby(["Estimate"]).agg({"NoPLHIV": "sum"}).reset_index()
AVG_NoPLHIV


# In[43]:


#Que 2(c) HIV free people
dataset['HIV_free_NoP'] = dataset['NoPLHIV']/(dataset['Prevalence_%']/100)
dataset.head()


# In[71]:


#Que 2(d)
dataset[dataset['District'].str.contains("City|Metro|city|metro", na=False)].groupby('District').agg({"NoPLHIV":"sum"}).reset_index()


# In[102]:


#Que 3

import pdb
import pandas as pd 
import re 

dataset.rename(columns=lambda c: re.sub('[^a-zA-Z0-9 ]', '', c), inplace=True)
dataset.head()


# In[81]:


#Que 4
districts_i=dataset[dataset['District'].str.endswith("i", na=False)].reset_index()
districts_i


# In[90]:


plot_data=districts_i[(districts_i["Estimate"] == "Fay-Heriott")]
plot_data


# In[93]:


plot_data_final=plot_data[['District','PrevalenceLCL','PrevalenceUCL']]


# In[101]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

data1 = [11.18,9.29,7.81,16.85,12.01,7.92,8.16,10.64,11.79]
data2 = [17.58,14.17,12.79,19.42,20.55,15.86,14.77,17.41,17.80]
width =0.3
plt.bar(np.arange(len(data1)), data1, width=width)
plt.bar(np.arange(len(data2))+ width, data2, width=width)
plt.show()

