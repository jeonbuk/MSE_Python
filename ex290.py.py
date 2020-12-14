#!/usr/bin/env python
# coding: utf-8

# In[2]:


class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
#자식class는 부모class를 받음
    def __init__(self):
        print("자식생성")
#자식class가 생성될때 자식생성이 print
        super().__init__()
#부모class에 접근후 생성자호출->부모생성print
나 = 자식()
#자식class에 객체를 생성


# In[ ]:


ex290.py

