#!/usr/bin/env python
# coding: utf-8

# In[3]:


def print_max(a, b, c) :
    if a > b and a>c:
        print(a)
#a가b보다크고 c보다도크면 a가 가장크기때문에 a출력
    elif b>c and b>a:
        print(b)
#그렇지 않고 b가 가장크면 b출력
    else:
        print(c)
#그렇지 않으면 c출력
print_max(11,2,3)


# In[ ]:


ex220.py

