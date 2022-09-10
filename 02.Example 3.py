#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


k = Q_(0.029, 'W/(m*K)')
L = Q_(20, 'mm')
delT = Q_(10, 'delta_degC')
W = Q_(2, 'm')
H = Q_(2, 'm')


# In[4]:


qpp_x = k*delT/L
'{:0.2F}'.format(qpp_x.to('W/m**2'))     # part (a) answer


# In[5]:


A = W*H
'{:0.2E}'.format(A.to('m**2'))


# In[6]:


q_x = A*qpp_x
'{:0.2F}'.format(q_x.to('W'))     # part (b) answer

