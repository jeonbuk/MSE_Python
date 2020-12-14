#!/usr/bin/env python
# coding: utf-8

# In[8]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    split = 변수.split(".")
#변수들의 문자열을 . 을 기준으로 분리한다.
    if (split[1] == "h") or (split[1] == "c"):
#그때 확장자가 h나 c라면 
        print(변수)
#출력한다


# In[ ]:


ex160.py

