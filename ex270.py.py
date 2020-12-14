#!/usr/bin/env python
# coding: utf-8

# In[5]:


종목 = []
#종목이라는 리스트 작성
삼성   = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)
#종목이라는 리스트에 삼성,현대차,lg전자가 기리키는 객체추가

for i in 종목:
    print(i.code, i.per)
#종목코드는 code를 통하여 per은 per로 접근


# In[ ]:


ex270.py

