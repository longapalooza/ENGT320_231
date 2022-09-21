#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


T_inf1 = Q_(2600, 'degC')
T_inf2 = Q_(100, 'degC')
h_1 = Q_(50, 'W/(m**2*K)')
h_2 = Q_(1000, 'W/(m**2*K)')
L_A = Q_(10, 'mm')
L_B = Q_(20, 'mm')
R_tc_flux = Q_(0.05, '(m**2*K)/W')


# In[4]:


Tbar = (T_inf1.to('K') + T_inf2.to('K'))/2
Tbar


# In[5]:


T_1 = Q_(1500, 'K')
T_2 = Q_(2000, 'K')
k_1 = Q_(21.5, 'W/(m*K)')
k_2 = Q_(15, 'W/(m*K)')
k_A = ((Tbar - T_1)/(T_2 - T_1))*(k_2 - k_1) + k_1
round(k_A, 2)


# In[6]:


k_B = Q_(31.7, 'W/(m*K)')


# In[7]:


R_tot_flux = 1/h_1 + L_A/k_A + R_tc_flux + L_B/k_B + 1/h_2
round(R_tot_flux, 5)


# In[8]:


q_flux =(T_inf1 - T_inf2)/R_tot_flux
round(q_flux.to('kW/m**2'), 2)    # answer to first part


# In[9]:


T_1 = T_inf1 - q_flux/h_1
round(T_1, 1)


# In[10]:


T_iA = T_1 - q_flux*L_A/k_A
round(T_iA, 1)


# In[11]:


T_iB = T_iA - q_flux*R_tc_flux
round(T_iB, 1)


# In[12]:


T_2 = T_iB - q_flux*L_B/k_B
round(T_2, 1)

