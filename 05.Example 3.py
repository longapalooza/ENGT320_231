#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


rho = Q_(28, 'kg/m**3')
T = Q_(300, 'K')


# In[4]:


rho_s = Q_(2500, 'kg/m**3')
k_s = Q_(1.4, 'W/(m*K)')


# In[5]:


rho_f = Q_(1.1614, 'kg/m**3')
k_f = Q_(26.3E-3, 'W/(m*K)')


# In[6]:


eps = (rho-rho_s)/(rho_f-rho_s)
round(eps, 4)


# In[7]:


k_effmax = eps*k_f + (1 - eps)*k_s
round(k_effmax, 4)    # answer to first part


# In[8]:


k_effmin = 1/((1 - eps)/k_s + eps/k_f)
round(k_effmin, 4)    # answer to second part

