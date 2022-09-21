#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io #


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


D_1=Q_(20, 'mm')
eps_1=Q_(0.02, '')
T_1=Q_(77, 'K')
D_2=Q_(50, 'mm')
eps_2=Q_(0.05, '')
T_2=Q_(300, 'K')
D_3=Q_(35, 'mm')
eps_3=Q_(0.02, '')


# In[4]:


sigma=Q_(5.67*10**-8, 'W/(m^2*K^4)')    # Stefan-Boltzman constant #


# In[5]:


qp_wo=(sigma*math.pi*D_1*(T_1**4-T_2**4))/((1/eps_1)+((1-eps_2)/eps_2)*(D_1/D_2))
round(qp_wo.to('W/m'), 4)    # answer #


# In[6]:


R_totL=((1-eps_1)/(eps_1*math.pi*D_1)
       +1/(math.pi*D_1)
       +2*((1-eps_3)/(eps_3*math.pi*D_3))
       +1/(math.pi*D_3)
       +(1-eps_2)/(eps_2*math.pi*D_2))
round(R_totL.to('1/m'), 0)


# In[7]:


qp_w=sigma*(T_1**4-T_2**4)/R_totL
round(qp_w.to('W/m'), 4)


# In[8]:


pDiff=abs((qp_w-qp_wo)/qp_wo)
round(pDiff.to(''), 4)    # answer #

