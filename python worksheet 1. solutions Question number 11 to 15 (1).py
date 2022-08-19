#!/usr/bin/env python
# coding: utf-8

# # python worksheet 1 (solutions Q.11 to Q.15)

# ## Q.11
# 

# #### solution

# In[49]:


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


# # Q.12

# ### solution

# In[55]:


num=int(input("enter any number:"))
count=0
for a in range(2,num):
    if num%a==0:
        count+=1
if count>=1:
        print(num,"is composite number")
    
else:
    print(num,"is prime number")


# # 

# # Q.13

# ### solution

# In[14]:


#python programme to check if a string is palindrome or not

x = "abhilasha"

w = " "

for i in x:
    w = i + w

    
if (x == w):
    
    print("no")

    
else:
    print("yes")
    


# # Q.14

# ### solution

# In[17]:



import math


a = float(input("Enter base:"))

b = float(input("Enter height:"))


c = math.sqrt(a**2+b**2)

print("hypotenuse=", c)


# # Q.15

# ### solution

# In[18]:


s = input()

t = s.lower()

for i in range(len(s)):
    
    b = t.count(t[i])
    
    print("{}--{}".format(s[i], b))


# In[ ]:





# In[ ]:




