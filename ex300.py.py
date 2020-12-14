#!/usr/bin/env python
# coding: utf-8

# In[1]:


per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
#실행할 코드
    except:
        print(0)
#예외가 발생하면 0으로 print 
    else:
        print("clean data")
#예외가 발생하지않으면 clean data print
    finally:
        print("변환 완료")
#예외와 상관없이 변환완료 print


# In[ ]:


ex300.py

