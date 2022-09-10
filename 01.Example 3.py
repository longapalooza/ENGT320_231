#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


ureg.define('USD = 1')


# In[4]:


H = Q_(50, 'mm')
W = Q_(45, 'mm')
D = Q_(20, 'mm')
T_s = Q_(33, 'degC')
e = 0.92
h = Q_(4.5, 'W/(m**2*K)')
T_inf = Q_(22, 'degC')
T_sur = Q_(20, 'degC')
C = Q_(0.18, 'USD/(kW*hr)')


# In[5]:


sig = Q_(5.67*10**-8, 'W/(m^2 K^4)')


# In[6]:


A_s = H*W + 2*H*D + 2*W*D
'{:0.3E}'.format(A_s.to('m**2'))


# In[7]:


q_conv = h*A_s*(T_s - T_inf)
'{:0.3E}'.format(q_conv.to('W'))


# In[8]:


q_rad = e*sig*A_s*(T_s.to('K')**4 - T_inf.to('K')**4)
'{:0.3E}'.format(q_rad.to('W'))


# In[9]:


Edot_tot = q_conv + q_rad
'{:0.3E}'.format(Edot_tot.to('W'))


# In[10]:


C_tot = C*Edot_tot
'{:0.6F}'.format(C_tot.to('USD/day'))     # answer

