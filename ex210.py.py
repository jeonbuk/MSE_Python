#!/usr/bin/env python
# coding: utf-8

# In[1]:


def message1():
    print("A")
#message1을 A출력으로 정의
def message2():
    print("B")
#message2를 B출력으로 정의
def message3():
    for i in range (3) :
#아래명령을 3번실행
        message2()
        print("C")
    message1()
#A를 한번출력
message3()


# In[ ]:


ex210.py

