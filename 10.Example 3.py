#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


m=Q_(0.05, 'kg/s')
D=Q_(0.15, 'm')
T_m0=Q_(103, 'degC')
L=Q_(5, 'm')
T_mL=Q_(85, 'degC')
T_inf=Q_(0, 'degC')
h_o=Q_(6, 'W/(m**2*K)')


# In[4]:


def interp(x, x1, x2, y1, y2):
    return ((x-x1)/(x2-x1))*(y2-y1)+y1


# In[5]:


Tb_m=(T_m0.to('K')+T_mL.to('K'))/2
Tb_m


# In[6]:


Ta=Q_(350, 'K')
Tb=Q_(400, 'K')
c_pa=Q_(1.009, 'kJ/(kg*K)')
c_pb=Q_(1.014, 'kJ/(kg*K)')
c_p=interp(Tb_m, Ta, Tb, c_pa, c_pb)
round(c_p, 3)


# In[7]:


mua=Q_(208.2E-7, 'N*s/m**2')
mub=Q_(230.1E-7, 'N*s/m**2')
mu=interp(T_mL, Ta, Tb, mua, mub)
'{:~.3E}'.format(mu)


# In[8]:


ka=Q_(30E-3, 'W/(m*K)')
kb=Q_(33.8E-3, 'W/(m*K)')
k=interp(T_mL, Ta, Tb, ka, kb)
'{:~.3E}'.format(k)


# In[9]:


Pra=0.7
Prb=0.69
Pr=interp(T_mL, Ta, Tb, Pra, Prb)
round(Pr, 4)


# In[10]:


q=m*c_p*(T_mL-T_m0)
round(q.to('W'), 1)    # answer to part 1


# In[11]:


Re_D=4*m/(math.pi*D*mu)
'{:.3E}'.format(Re_D.to(''))


# In[12]:


round(L/D, 2)


# In[13]:


Nu_D=0.023*Re_D**(4/5)*Pr**(0.3)
round(Nu_D.to(''), 2)


# In[14]:


h_i=Nu_D*k/D
round(h_i.to('W/(m**2*K)'), 2)


# In[15]:


qf_s=(T_mL-T_inf)/(1/h_i+1/h_o)
round(qf_s.to('W/m**2'), 1)


# In[16]:


T_sL=T_mL-qf_s/h_i
round(T_sL, 1)    # answer to part 2

