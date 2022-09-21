#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io
import scipy.optimize as sp


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


T_hi=Q_(300, 'degC')
T_ho=Q_(100, 'degC')
m_c=Q_(1, 'kg/s')
T_ci=Q_(35, 'degC')
T_co=Q_(125, 'degC')
U_h=Q_(100, 'W/(m**2*K)')


# In[4]:


Tbar_c=(T_co.to('K')+T_ci.to('K'))/2
round(Tbar_c.to('K'), 1)


# In[5]:


Ta=Q_(350, 'K')
Tb=Q_(355, 'K')
c_pa=Q_(4.195, 'kJ/(kg*K)')
c_pb=Q_(4.199, 'kJ/(kg*K)')
c_pc=((Tbar_c-Ta)/(Tb-Ta))*(c_pb-c_pa)+c_pa
round(c_pc.to('kJ/(kg*K)'), 3)


# In[6]:


C_c=m_c*c_pc
round(C_c.to('kW/K'), 3)


# In[7]:


C_h=C_c*(T_co-T_ci)/(T_hi-T_ho)
round(C_h.to('kW/K'), 3)


# In[8]:


C_min=min(C_c, C_h)
round(C_min.to('kW/K'), 3)


# In[9]:


C_max=max(C_c, C_h)
round(C_max.to('kW/K'), 3)


# In[10]:


C_r=C_min/C_max
round(C_r.to(''), 4)


# In[11]:


q_max=C_min*(T_hi-T_ci)
round(q_max.to('kW'), 1)


# In[12]:


q=C_c*(T_co-T_ci)
round(q.to('kW'), 1)


# In[13]:


eps=q/q_max
round(eps.to(''), 4)


# In[14]:


def eps_relation(NTU, C_r):
    return 1-math.exp((1/C_r)*NTU**0.22*(math.exp(-C_r*NTU**0.78)-1))


# In[15]:


def g(NTU):
    return eps_relation(NTU, C_r.to('').magnitude)-eps.to('').magnitude


# In[16]:


solution=sp.fsolve(g, 1)
NTU=Q_(solution[0], '')
round(NTU, 3)


# In[17]:


A=NTU*C_min/U_h
round(A.to('m**2'), 2)    # answer

