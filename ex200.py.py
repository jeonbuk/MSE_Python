#!/usr/bin/env python
# coding: utf-8

# In[4]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
total_profit = 0
#시작금 0원
for day_price in ohlc[1:]:
    profit= (day_price[0] - day_price[3])
#수익금은 시가-종가 
    total_profit+=profit
#총수익금은 수익금들의 누적 
    print(profit)


# In[ ]:


ex200.py

