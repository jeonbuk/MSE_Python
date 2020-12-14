#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']


변동폭 = float(btc['max_price']) - float(btc['min_price'])
#변동폭은 최고가와 최저가의 차이로 정의 
시가 = float(btc['opening_price'])
#시작가를 opening_price로 함
최고가 = float(btc['max_price'])
#최고가를 max_price 로함 

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
# 시가와 변동폭의 합이 최고가 보다 클때는 상승장 출력 아니라면 하락장 출력


# In[ ]:


ex130.py

