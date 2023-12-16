#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[2]:


df = pd.read_excel('hotel_bookings 2.xlsx')


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[6]:


df.info()


# In[7]:


df.describe(include = 'object')


# In[8]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[9]:


df.isnull().sum()


# In[10]:


df.drop(['agent','company'], axis = 1, inplace = True)


# In[11]:


df.dropna(inplace = True)


# In[12]:


df.isnull().sum()


# In[13]:


df.describe()


# In[14]:


df = df[df['adr'] < 5000]


# In[15]:


Canceled_perc = df['is_canceled'].value_counts(normalize = True)
print(Canceled_perc)


# In[16]:


plt.figure(figsize = (5,4))
plt.title('Reservation Status counts')
plt.bar(['Not canceled','canceled'],df['is_canceled'].value_counts(),edgecolor = 'k', width = 0.6)
plt.show()


# In[17]:


plt.figure(figsize = (7,5))
ax1 = sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'dark')
plt.title('Reservation count hotels wise', size = 20)
plt.xlabel('hotel')
plt.ylabel('Number of reservation')
plt.legend(['not canceled','canceled'])
plt.show()


# In[18]:


Resort_Hotel = df[df['hotel'] == 'Resort Hotel']
Resort_Hotel['is_canceled'].value_counts(normalize = True)


# In[19]:


City_Hotel = df[df['hotel'] == 'City Hotel']
City_Hotel['is_canceled'].value_counts(normalize = True)


# In[20]:


Resort_Hotel = Resort_Hotel.groupby('reservation_status_date')[['adr']].mean()
City_Hotel = City_Hotel.groupby('reservation_status_date')[['adr']].mean()


# In[21]:


plt.figure(figsize = (20,8))
plt.title('ADR in hotels', size = 30)
plt.plot(Resort_Hotel.index, Resort_Hotel['adr'], label= 'Resort hotel')
plt.plot(City_Hotel.index, City_Hotel['adr'], label= 'City hotel')
plt.legend(fontsize = 20)
plt.show()


# In[22]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (20,8))
ax1 = sns.countplot(x = 'month' , hue = 'is_canceled', data = df)
plt.xlabel('months')
plt.ylabel('No of reservation')
plt.legend('Not canceled', 'canceled')
plt.show()


# In[23]:


plt.figure(figsize = (20,8))
sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.legend(fontsize = 20)
plt.show()


# In[32]:


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (6,8))
plt.title('Top 10 country with highest canceled')
plt.pie(top_10_country, autopct ='%.2f' , labels = top_10_country.index)
plt.show()


# In[25]:


df['market_segment'].value_counts(normalize = True)


# In[26]:


cancelled_data['market_segment'].value_counts(normalize = True)


# In[27]:


cancelled_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_adr.reset_index(inplace = True)
cancelled_adr.sort_values('reservation_status_date', inplace = True)

not_cancelled_data =  df[df['is_canceled'] == 0]
not_cancelled_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_adr.reset_index(inplace = True)
not_cancelled_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_adr['reservation_status_date'],not_cancelled_adr['adr'], label = 'Not canceled')
plt.plot(cancelled_adr['reservation_status_date'],cancelled_adr['adr'], label = 'cancelled')
plt.legend()


# In[28]:


cancelled_adr = cancelled_adr[(cancelled_adr['reservation_status_date'] > '2016') & (cancelled_adr['reservation_status_date'] < '2017-09')]
not_cancelled_adr = not_cancelled_adr[(not_cancelled_adr['reservation_status_date'] > '2016') & (not_cancelled_adr['reservation_status_date'] < '2017-09')] 


# In[29]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate', fontsize = 30)
plt.plot(not_cancelled_adr['reservation_status_date'],not_cancelled_adr['adr'], label = 'Not canceled')
plt.plot(cancelled_adr['reservation_status_date'],cancelled_adr['adr'], label = 'cancelled')
plt.legend(fontsize = 20)


# In[ ]:




