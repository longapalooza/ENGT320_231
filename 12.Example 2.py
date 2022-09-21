#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io #


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


U=Q_(100, 'W/(m**2*K)')
A=Q_(40, 'm**2')
m_c=Q_(1, 'kg/s')
T_ci=Q_(35, 'degC')
m_h=Q_(1.5, 'kg/s')
T_hi=Q_(250, 'degC')


# In[4]:


C_c=Q_(4.197, 'kW/K')
c_ph=Q_(1000, 'J/(kg*K)')


# In[5]:


C_h=m_h*c_ph
round(C_h.to('kW/K'), 3)


# In[6]:


C_min=min(C_c, C_h)
round(C_min.to('kW/K'), 2)


# In[7]:


C_max=max(C_c, C_h)
round(C_max.to('kW/K'), 2)


# In[8]:


C_r=C_min/C_max
round(C_r.to(''), 4)


# In[9]:


q_max=C_min*(T_hi-T_ci)
round(q_max.to('kW'), 1)


# In[10]:


NTU=U*A/C_min
round(NTU.to(''), 3)


# In[11]:


eps=1-math.exp((1/C_r.to(''))*NTU.to('')**0.22*(math.exp(-C_r.to('')*NTU.to('')**0.78)-1))
eps=Q_(eps, '')
round(eps, 4)


# In[12]:


q=eps*q_max
round(q.to('kW'), 1)    # answer to first part #


# In[13]:


T_ho=T_hi-q/C_h
round(T_ho.to('degC'), 1)    # answer to first part of the second part #


# In[14]:


T_co=T_ci+q/C_c
round(T_co.to('degC'), 1)    # answer to second part of the second part #

