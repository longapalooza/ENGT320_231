#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


W_in = Q_(50, 'W')
Q_L = Q_(500, 'W')
T_H = Q_(85, 'degF')


# In[4]:


COP_R = Q_L/W_in
COP_R


# In[5]:


T_L = COP_R*T_H.to('degR')/(COP_R + 1)
round(T_L.to('degF'), 1)

