#!/usr/bin/env python
# coding: utf-8

# In[4]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
#volatility를 리스트로 정하고
for i in range(len(low_prices)) :
    diff=high_prices[i]-low_prices[i]
#변동폭을 최고가와 최저가의 차로 정한다
    volatility.append(high_prices[i] - low_prices[i])
#volatility리스트에 변동폭을 추가한다.
print (volatility)


# In[ ]:


ex180.py

