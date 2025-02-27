#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


phone_data=pd.read_csv('phone_dataset.csv')


# In[5]:


phone_data


# In[6]:


type(phone_data['Price'][0])


# In[7]:


phone_data['Price'] = phone_data['Price'].str.replace(r'\$', '', regex=True)

phone_data


# In[8]:


type(phone_data['Price'][0])


# In[9]:


phone_data['Price']=phone_data['Price'].str[:-2]


# In[10]:


phone_data


# In[11]:


phone_data['TotalPrice']=phone_data['Price'].astype(int).cumsum()


# In[12]:


phone_data


# # creating a new column date

# In[13]:


phone_data['Date']=pd.date_range('01/01/2024' , periods=len(phone_data))


# In[14]:


phone_data


# In[15]:


#lets plot these both columns now
phone_data.plot(x='Date',y='TotalPrice',kind='scatter');
plt.show()




# In[16]:


phone_data.plot(x='Rating',y='Price',kind='scatter');
plt.show()



# In[17]:


phone_data.plot(x='Price',y='Date',kind='scatter');
plt.show()


# In[18]:


phone_data.plot(x='Storage (GB)',y='Price',kind='scatter');
plt.show()


# In[19]:


phone_data.plot(x='Brand',y='Battery (mAh)',kind='bar',cmap='gist_heat',)
plt.show()


# # Create Random Data Frame 

# In[20]:


x=np.random.rand(10,4)
x
#convert in to data frames
df= pd.DataFrame(x,columns=['a','b','c','d'])
df


# In[21]:


df.plot(kind='bar')
plt.show()


# In[22]:


df.plot.bar()
plt.show()


# In[23]:


phone_data['Storage (GB)'].plot.hist(bins=20)
plt.show()


# # pyplot vs object Oriented Method

# In[24]:


heart=pd.read_csv('heart.csv')
heart.head()


# In[25]:


over_48=heart[heart['age']>55]
over_48


# In[26]:


#pyplot method
over_48.plot(kind='scatter',x='age',y='chol',c='oldpeak')
plt.show()#quickly small work


# In[27]:


#object Oriented approach
fig,ax=plt.subplots(figsize=(6,5))
over_48.plot(kind='scatter',
            x='age',
            y='chol',
            c='oldpeak',
            ax=ax)
plt.show()#pakka km  kerny ky liy


# # Entire life cycle of object oriented 

# In[28]:


# create figure and graph  area 
fig ,ax=plt.subplots(figsize=(10,6))
#plot data
scatter_plot=ax.scatter(x=over_48['age'],
                       y=over_48['chol'],
                       c=over_48['oldpeak'])
#customization 
ax.set(title='suspectability of Heart disease ',
      xlabel='Age' ,
      ylabel='cholestrol')
#set the legend
ax.legend(*scatter_plot.legend_elements(),title='oldpeak')

scatter_plot
plt.show()


# # Entire life cycle of object Oriented Plot Advanced
# 

# In[29]:


#create plot area 
#similar axes ko share kerna 
fig,(plot_1,plot_2)= plt.subplots(nrows=2,ncols=1,figsize=(10,10), sharex=True)
#add to plot_1
scatter_plot=plot_1.scatter(x=over_48['age'],
                           y=over_48['chol'],
                           c=over_48['oldpeak'],
                           cmap='gist_heat' ,) #change the color data
#customize
plot_1.set(title='Heart diease Problem with cholestrol',
          #xlabel='Age',
          ylabel='cholestrol')
plot_1 .legend(*scatter_plot.legend_elements(),title='survived or not')
#now plots second graph
scatter_plot=plot_2.scatter(x=over_48['age'],
                           y=over_48['trestbps'],
                           c=over_48['oldpeak'],
                           cmap='plasma',)
plot_2.set(title='Heart dieases problem with Resting blood pressure',
           xlabel='Age',
           ylabel='Resting Blood Pressure')
plot_2.legend(*scatter_plot.legend_elements(),title='survived or Not')
#Mealine
plot_2.axhline(y=over_48['trestbps'].mean(),linestyle="--")
plot_1.axhline(y=over_48['chol'].mean(),linestyle="--")
#coloring data 
#coloring plots
plt.style.use('seaborn-v0_8-darkgrid',)
#naming figure
fig.suptitle('Patient Data',fontsize=32,fontweight='bold')
#saving the figure
fig.savefig('Patients data Report.png')
plt.show()


# # Customize plots

# In[30]:


plt.style.available


# # Naming graph plot

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




