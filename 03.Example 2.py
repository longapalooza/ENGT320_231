#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


qdot1 = Q_(5E7, 'W/m**3')
D = Q_(50, 'mm')
a = Q_(800, 'delta_degC')
b = Q_(-4.167E5, 'delta_degC/m**2')
k = Q_(30, 'W/(m*K)')
rho = Q_(1100, 'kg/m**3')
c_p = Q_(800, 'J/(kg*K)')
r_a1 = Q_(0, 'mm')
r_a2 = D/2
qdot2 = Q_(1E8, 'W/m**3')


# In[4]:


qp_0 = -4*k*math.pi*b*r_a1**2
round(qp_0.to('W/m'), 2)    # answer to part (a1)


# In[5]:


qp_25 = -4*k*math.pi*b*r_a2**2
round(qp_25.to('kW/m'), 2)    # answer to part (a2)


# In[6]:


pTpt = 4*b*k/(rho*c_p) + qdot2/(rho*c_p)
round(pTpt.to('K/s'), 2)    # answer to part (b)

