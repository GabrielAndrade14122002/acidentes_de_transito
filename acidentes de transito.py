#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('cat_acidentes.csv', sep = ';')


# In[2]:


df


# In[1]:


get_ipython().system('pip install folium')


# In[6]:


import folium
from folium.plugins import HeatMap

mapa = folium.Map(location=[-30.1, -51.15], zoom_start=11)
coordenadas = list(zip(df.latitude, df.longitude))
mapa_calor = HeatMap(coordenadas, radius=9, blur=10)
mapa.add_child(mapa_calor)
mapa


# In[4]:


df = df.dropna(subset=['latitude', 'longitude'], how='any')
df


# In[8]:


from folium.plugins import MarkerCluster

mapa = folium.Map(location=[-30.1, -51.15], zoom_start=11)
mapa_cluster = MarkerCluster(coordenadas)
mapa.add_child(mapa_cluster)

mapa


# In[9]:


df.data


# In[10]:


df['data'] = pd.to_datetime(df['data'], errors='coerce')
df_ano = df['data'].dt.year.value_counts()
df_ano


# In[11]:


df_ano = df_ano.drop(2202)
df_ano


# In[12]:


import matplotlib.pyplot as plt

plt.bar(df_ano.index, df_ano.values)
plt.show()


# In[13]:


df_ano/df_ano.max()


# In[14]:


gradiente = df_ano/df_ano.max()
cores = plt.cm.Blues(gradiente)

plt.bar(df_ano.index, df_ano.values, color = cores)
plt.show()


# In[ ]:




