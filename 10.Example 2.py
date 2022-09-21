#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


D=Q_(50, 'mm')
L=Q_(6, 'm')
T_s=Q_(100, 'degC')
m=Q_(0.25, 'kg/s')
T_mi=Q_(15, 'degC')
T_mo=Q_(57, 'degC')


# In[4]:


Tb_m=(T_mi.to('K')+T_mo.to('K'))/2
round(Tb_m, 1)


# In[5]:


c_p=Q_(4.178, 'kJ/(kg*K)')


# In[6]:


delT_lm=((T_s-T_mo) - (T_s-T_mi))/math.log((T_s-T_mo)/(T_s-T_mi))
round(delT_lm.to('K'), 2)


# In[7]:


A_s=math.pi*D*L
round(A_s.to('m**2'), 4)


# In[8]:


hb=(m*c_p*(T_mo-T_mi))/(A_s*delT_lm)
round(hb.to('W/(m**2*K)'), 1)    # answer

