#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


q = Q_(2000, 'W')
V_s = Q_(90, 'V')
rho = Q_(1.10E-6, 'ohm*m')
d = Q_(0.4, 'mm')


# In[4]:


R = V_s**2/q
R.to('ohm')


# In[5]:


L = R*(math.pi/4*d**2)/rho
round(L.to('m'), 4)    # answer

