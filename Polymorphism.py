#!/usr/bin/env python
# coding: utf-8

# In[1]:


def test (a,b):
    return a+b


# In[2]:


test(3,4)


# In[6]:


test("sudh  " , "Kumar")


# In[8]:


test([3,4,5,6],[34,56,78])


# In[9]:


class data_science:
    
    def syllabus(self):
        print("this is my syllabus for data science")


# In[10]:


class web_dev:
    def syllabus(self):
        print("this is my web_dev syllabus")


# In[11]:


class web_dev:
    def syllabus(self):
        print("this is syllabus for web dev")


# In[12]:


def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()


# In[13]:


data_science= data_science()


# In[17]:


web_dev = web_dev()


# In[18]:


class_obj = [data_science , web_dev]


# In[20]:


class_parcer(class_obj)


# learning phase of polymorphism
# 

# In[ ]:




