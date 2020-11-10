#!/usr/bin/env python
# coding: utf-8

# In[132]:


import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns


# In[133]:


cd C:\Users\Krutarth\Desktop\Datasets


# In[134]:


data = pd.read_csv('covid_19_data.csv')
data.drop(["Last Update","SNo"], axis=1, inplace=True)
data.isnull().sum()


# In[135]:


data.head()


# In[136]:


data['Country/Region'].value_counts()


# In[137]:


data['Country/Region'].value_counts()
data.shape


# In[138]:


top_countries=data['Country/Region'].value_counts().loc[lambda x : x > 200].index


# In[139]:


data=data[data['Country/Region'].isin(top_countries)]
data.columns


# In[140]:


data.shape


# In[141]:


data.isnull().sum()


# In[142]:


data.drop('Province/State',axis=1,  inplace=True)


# In[143]:


data.head()
data.columns


# In[144]:


data["timeseries"] = pd.to_datetime(data['ObservationDate'])
data.drop('ObservationDate', inplace=True, axis=1)


# In[145]:


data['month']=data['timeseries'].dt.month
data.month.unique()


# In[146]:


lis_confirmed = []
for i in range(1,10):
    lis_confirmed.append(sum(data[data['month'] == i]['Confirmed']))


# In[147]:


lis_confirmed


# In[149]:


sns.barplot(data.month.unique(), lis_confirmed, palette="rainbow")
plt.show()
plt.savefig('data_covid.png')


# In[42]:


plot_all = pd.DataFrame(index=range(1,10))
list_countries = []
for x in data['Country/Region'].unique():
    for i in range(1,10):
        data2 = data[data['Country/Region'] == x]
        list_countries.append(sum(data2[data2['month'] == i]['Confirmed']))
    plot_all[x] = list_countries
    list_countries.clear()


# In[43]:


len(plot_all.columns)


# In[44]:


plot_all


# In[150]:


plt.figure(figsize=(10,10))
sns.lineplot(data=plot_all,dashes=False)
plt.legend(ncol=3, bbox_to_anchor=(1,1))
plt.show()
plt.savefig('rate.png')


# In[162]:


cd C:\Users\Krutarth\Desktop\Datasets


# In[163]:


lat_long = pd.read_csv("time_series_covid_19_recovered.csv")


# In[164]:


uk = lat_long[lat_long['Country/Region'] == 'United Kingdom'][['Country/Region','Lat','Long']]
china = lat_long[lat_long['Country/Region'] == 'China'][['Country/Region','Lat','Long']]


# In[165]:


lat_longi = lat_long[lat_long['Country/Region'].isin(plot_all.columns)][['Country/Region', 'Lat', 'Long']]
lat_longi.reset_index(drop=True, inplace=True)
lat_longi=lat_longi.append(uk)
lat_longi=lat_longi.append(china)


# In[166]:


plot_all.columns.isin(lat_longi['Country/Region'].unique())


# In[167]:


plot_all


# In[168]:


lat_longi.loc[lat_longi['Country/Region']=='China', 'Country/Region'] = 'Mainland China'
lat_longi.loc[lat_longi['Country/Region']=='United Kingdom', 'Country/Region'] = 'UK'
lat_longi


# In[169]:


lat_longi['Country/Region'].value_counts()
lat_longi = lat_longi.drop_duplicates('Country/Region')


# In[170]:


pd.merge(data,lat_longi, on='Country/Region')


# In[171]:


lat_longi


# In[172]:


total = pd.DataFrame(np.array(plot_all[8:]).reshape(94,1))
total['Country/Region'] = plot_all.columns
lat_longi = pd.merge(lat_longi, total, on='Country/Region')
lat_longi


# In[110]:


import geopandas as gpd


# In[111]:


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


# In[112]:


from shapely.geometry import Point, Polygon


# In[113]:


a=zip(lat_longi['Long'],lat_longi['Lat'])
x= np.array(tuple(a))
x


# In[114]:


lst=[]
for z in x:
    lst.append(Point(z))


# In[115]:


geo_plot = gpd.GeoDataFrame(geometry=lst)
fig, ax = plt.subplots(figsize=(10,10))
world.plot(ax=ax)
geo_plot.plot(ax=ax, color='red')


# In[116]:


size_count = lat_longi[0].apply(lambda x: x/10**7)


# In[117]:


for i in range(0, len(geo_plot)):
    geo_plot['geometry'][i] = geo_plot['geometry'][i].buffer(size_count[i])


# In[118]:


from mpl_toolkits.axes_grid1 import make_axes_locatable
fig, ax = plt.subplots(1,1, figsize=(15,15))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
world.plot(ax=ax,column='pop_est', cax=cax, legend=True, cmap='icefire')
geo_plot.plot(ax=ax, color='red', cmap='gnuplot')
plt.show()


# In[ ]:




