#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


k = Q_(25, 'W/(m*K)')
t = Q_(6, 'mm')
W = Q_(6, 'mm')
H = Q_(2, 'mm')
S = Q_(4, 'mm')
h_o = Q_(1000, 'W/(m**2*K)')
T_inf_o = Q_(1700, 'K')
h_i = Q_(200, 'W/(m**2*K)')
T_inf_i = Q_(400, 'K')


# In[4]:


delx = Q_(1, 'mm')


# In[5]:


a = 2 + h_o*delx/k
b = 2*(2 + h_o*delx/k)
c = 2*(3 + h_i*delx/k)
d = 2*(2 + h_i*delx/k)
e = 2 + h_i*delx/k
f = (h_o*delx/k)*T_inf_o
g = (h_i*delx/k)*T_inf_i


# In[6]:


a = a.to_base_units().magnitude
b = b.to_base_units().magnitude
c = c.to_base_units().magnitude
d = d.to_base_units().magnitude
e = e.to_base_units().magnitude
f = f.to_base_units().magnitude
g = g.to_base_units().magnitude


# In[7]:


A = [[-a, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, -b, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, -b, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, -b, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, -b, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, -a, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, -4, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1, -4, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 1, -4, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 1, -4, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -4, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, -4, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -4, 2, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -4, 1, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, -c, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, -d, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, -d, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -e, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -2, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, -4, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -e]]
A = np.array(A)


# In[8]:


C = [-f, -2*f, -2*f, -2*f, -2*f, -f, 0, 0, 0, 0, 0, 0, 0, 0, -2*g, -2*g, -2*g, -g, 0, 0, -g]
C = np.array(C)


# In[9]:


T = np.matmul(np.linalg.inv(A), C) # answer to first part
print(T)


# In[10]:


T = list(T)
T_max = max(T)
T_max_location = T.index(T_max) + 1

print('Max temperature:', round(T_max, 1))
print('Node with max temperature:', T_max_location) # answer to second part

