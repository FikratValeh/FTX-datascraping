#!/usr/bin/env python
# coding: utf-8

# In[240]:


import numpy as np
import requests
import json
url = 'https://ftx.com/api/markets/{}/candles?resolution={}&start_time={}&end_time={}' # parantheses are marketname, 
                                                            #resolution, start_date, and end_date, accordingly
#getting market names
name_url = 'https://ftx.com/api/futures'
market_name_data = requests.get(name_url)
market_name_data = market_name_data.json()
market_name_data = market_name_data['result']
market_name = []
for i in market_name_data:
        market_name.append(i['name'])
#getting historical prices of the indicated futures
resolution = '86400'
start_date = '1483260044'
end_date = '1624056044'
close_values_markets = []
for k in range(0,(len(market_name))):
    url_new = url.format(market_name[k], resolution, start_date, end_date)
    data = requests.get(url_new)
    data = data.json()
    data = data['result']
    close_values = []
    for j in data:
        if len(data) == 700:
            close_values.append(j['close'])
        else:
            for h in range (0, 700 - len(data)):
                close_values.append('-')
            for g in data:
                close_values.append(g['close'])
    close_values_markets.append(close_values)    

close_values_markets

np.savetxt("FTX_DATA.csv", close_values_markets, delimiter=", ", fmt="% s")
np.savetxt("ftx_market_names.csv", market_name, delimiter=", ", fmt="% s")


# In[243]:


np.savetxt("shows.csv", close_values_markets, delimiter=", ", fmt="% s")


# In[228]:


np.savetxt("adlar.csv", market_name, delimiter=", ", fmt="% s")


# In[232]:


len(data)


# In[182]:


import numpy as np
import requests
import json
url = 'https://ftx.com/api/indexes/{}/candles?resolution={}&start_time={}&end_time={}' # parantheses are marketname, 
                                                            #resolution, start_date, and end_date, accordingly
market_name = 'BTC'
resolution = '86400'
start_date = '1483260044'
end_date = '1624056044'
url = url.format(market_name, resolution, start_date, end_date)
data = requests.get(url)
data = data.json()
data = data['result']
data


# In[175]:


data


# In[185]:


name_url = 'https://ftx.com/api/futures'
market_name_data = requests.get(name_url)
market_name_data = market_name_data.json()
market_name_data = market_name_data['result']
market_name_data


# In[139]:


type(data)


# In[141]:


data = data.json()
data


# In[166]:


name_url = 'https://ftx.com/api/futures'
market_name_data = requests.get(name_url)
market_name_data = market_name_data.json()
market_name_data = market_name_data['result']
market_name = []
for i in market_name_data:
        market_name.append(i['name'])

market_name


# In[238]:


lst = [1, 2]
lst.extend(range(0))
lst

