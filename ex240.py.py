#!/usr/bin/env python
# coding: utf-8

# In[1]:


def 함수0(num) :
    return num * 2
#num은 28
def 함수1(num) :
    return 함수0(num + 2)
#함수 0의 num은 14, 함수 0호출
def 함수2(num) :
    num = num + 10
    return 함수1(num)
#첫번째 작업 num은 12, 함수 1로 return
c = 함수2(2)
#출력값은 28
print(c)


# In[ ]:


ex240.py

