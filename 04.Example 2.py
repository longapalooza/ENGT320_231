#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


delV = Q_(0.1, 'mV')
S_Bi = Q_(-72, 'uV/K')
S_Sb = Q_(47, 'uV/K')
T_ref = Q_(22, 'degC')


# In[4]:


T_m = T_ref.to('K') + delV/(S_Sb - S_Bi)
round(T_m.to('degC'), 1)    # answer

