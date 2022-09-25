#!/usr/bin/env python
# coding: utf-8

# # DATA ANALYSIS OF GOOGLE APP'S RATINGS
# Import the Required Modules

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


google = pd.read_csv('C:\\Users\\arunc\\Desktop\\data cleaning\\googleplaystore.csv')
google.head() #Inspecting the first 5 rows


# In[3]:


google.describe()   # Summary Statistics


# In[4]:


google.boxplot();


# In[5]:


google.hist();


# # Data Cleaning
# Count the number of missing values in the Dataframe

# In[6]:


google.isnull()


# In[7]:


# Count the number of missing values in each column
google.isnull().sum()


# In[8]:


google[google['Rating']>5]


# In[9]:


google.drop([10472],inplace=True)


# In[10]:


google[10470:10475]


# In[11]:


google.boxplot();


# In[12]:


google.hist();


# # Data Imputation and Manipulation
# Fill the null values with appropriate values using aggregate functions such as mean, median or mode.

# In[13]:


#Define a function impute_median
def impute_median(series):
    return series.fillna(series.median())


# In[14]:


google['Rating']=google['Rating'].transform(impute_median)


# In[15]:


#count the number of null values in each column
google.isnull().sum()


# In[16]:


# modes of categorical values
print(google['Current Ver'].mode())
print(google['Android Ver'].mode())
print(google['Type'].mode())


# In[17]:


# Fill the missing categorical values with mode
google['Current Ver'].fillna(str(google['Current Ver'].mode().values[0]),inplace=True)
google['Android Ver'].fillna(str(google['Current Ver'].mode().values[0]),inplace=True)
google['Type'].fillna(str(google['Current Ver'].mode().values[0]),inplace=True)


# In[18]:


#count the number of null values in each column
google.isnull().sum()


# In[19]:


### Let's convert Price, Reviews and Installs into Numerical Values
google['Reviews']=google['Reviews'].apply(lambda x:float(x))
google['Installs'] = google['Installs'].apply(lambda x: str(x).replace('+','').replace(',','')).astype('int')
google['Price'] = google['Price'].apply(lambda x: str(x).replace('$','')).astype('float')


# In[20]:


google.head(10) 


# In[21]:


google.describe()


# # Data Visualization

# In[22]:


grp = google.groupby('Category')
x=grp['Rating'].mean()
y=grp['Price'].sum()
z=grp['Reviews'].max()
print(x)
print(y)
print(z)


# In[23]:


plt.figure(figsize=(12,6))
plt.plot(x,'ro',color='g');
plt.xticks(rotation=90);
plt.title('Category wise Rating');
plt.xlabel('Categories');
plt.ylabel('Rating-->');


# In[24]:


plt.figure(figsize=(12,6))
plt.plot(y,'r--',color='b');
plt.xticks(rotation=90);
plt.title('Category wise Rating');
plt.xlabel('Categories');
plt.ylabel('Price-->');


# In[25]:


plt.figure(figsize=(12,6))
plt.plot(z,'g^',color='b');
plt.xticks(rotation=90);
plt.title('Category wise Rating');
plt.xlabel('Categories');
plt.ylabel('Max-->');


# In[ ]:




