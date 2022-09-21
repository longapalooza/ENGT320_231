#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


T_ci=Q_(30, 'degC')
T_co=Q_(80, 'degC')
m_c=Q_(3, 'kg/s')
T_hi=Q_(225, 'degC')
T_ho=Q_(100, 'degC')
D=Q_(100, 'mm')
U=Q_(200, 'W/(m**2*K)')


# In[4]:


Tbar_c=(T_ci.to('K')+T_co.to('K'))/2
round(Tbar_c, 1)


# In[5]:


Ta=Q_(325, 'K')
Tb=Q_(330, 'K')
c_pa=Q_(4.182, 'kJ/(kg*K)')
c_pb=Q_(4.184, 'kJ/(kg*K)')
c_pc=((Tbar_c-Ta)/(Tb-Ta))*(c_pb-c_pa)+c_pa
round(c_pc, 3)


# In[6]:


Tbar_h=(T_hi.to('K')+T_ho.to('K'))/2
round(Tbar_h, 1)


# In[7]:


Ta=Q_(400, 'K')
Tb=Q_(450, 'K')
c_pa=Q_(1.014, 'kJ/(kg*K)')
c_pb=Q_(1.021, 'kJ/(kg*K)')
c_ph=((Tbar_h-Ta)/(Tb-Ta))*(c_pb-c_pa)+c_pa
round(c_ph, 3)


# In[8]:


q=m_c*c_pc*(T_co-T_ci)
round(q.to('kW'), 1)


# In[9]:


delT_1=T_hi-T_ci
round(delT_1.to('K'), 1)


# In[10]:


delT_2=T_ho-T_co
round(delT_2.to('K'), 1)


# In[11]:


delT_lm=(delT_2-delT_1)/math.log(delT_2/delT_1)
round(delT_lm.to('K'), 1)


# In[12]:


A=q/(U*delT_lm)
round(A.to('m**2'), 2)    # answer to first part


# In[13]:


L=A/(math.pi*D)
round(L.to('m'), 1)    # answer to second part

