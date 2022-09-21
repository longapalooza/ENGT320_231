#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


T_mi=Q_(20, 'degC')
T_mo=Q_(60, 'degC')
D_i=Q_(20, 'mm')
D_o=Q_(40, 'mm')
q=Q_(1E6, 'W/m**3')
m=Q_(0.1, 'kg/s')
T_so=Q_(70, 'degC')


# In[4]:


Tb_m=(T_mo.to('K')+T_mi.to('K'))/2
round(Tb_m.to('K'), 1)


# In[5]:


Ta=Q_(310, 'K')
Tb=Q_(315, 'K')
c_pa=Q_(4.178, 'kJ/(kg*K)')
c_pb=Q_(4.179, 'kJ/(kg*K)')
c_p=((Tb_m-Ta)/(Tb-Ta))*(c_pb-c_pa)+c_pa
round(c_p, 3)


# In[6]:


L=(4*m*c_p*(T_mo-T_mi))/(math.pi*q*(D_o**2-D_i**2))
round(L.to('m'), 2)    # answer to part 1


# In[7]:


qf_s=(q*(D_o**2-D_i**2))/(4*D_i)
round(qf_s.to('kW/m**2'), 2)


# In[8]:


h_o=qf_s/(T_so-T_mo)
round(h_o.to('kW/(m**2*K)'), 3)    # answer to part 2

