#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


T_a1 = Q_(300, 'K')
T_a2 = Q_(700, 'K')
T_b = Q_(1000, 'K')
T_c = Q_(300, 'K')


# In[4]:


rho_a1 = Q_(2702, 'kg/m**3')
cp_a1 = Q_(903, 'J/(kg*K)')
k_a1 = Q_(237, 'W/(m*K)')


# In[5]:


a_a1 = k_a1/(rho_a1*cp_a1)
'{:0.2E}'.format(a_a1.to('m**2/s'))    # part (a1) answer


# In[6]:


rho_a2 = Q_(2702, 'kg/m**3')    # at 300 K because table is inadequate
k_a2 = Q_(((700-600)/(800-600))*(218-231)+231, 'W/(m*K)')
cp_a2 = Q_(((700-600)/(800-600))*(1146-1033)+1033, 'J/(kg*K)')


# In[7]:


k_a2


# In[8]:


cp_a2


# In[9]:


a_a2 = k_a2/(rho_a2*cp_a2)
'{:0.2E}'.format(a_a2.to('m**2/s'))    # part (a2) answer


# In[10]:


rho_b = Q_(3160, 'kg/m**3')    # at 300 K because table is inadequate
k_b = Q_(87, 'W/(m*K)')
cp_b = Q_(1195, 'J/(kg*K)')


# In[11]:


a_b = k_b/(rho_b*cp_b)
'{:0.2E}'.format(a_b.to('m**2/s'))    # part (b) answer


# In[12]:


rho_c = Q_(900, 'kg/m**3')
k_c = Q_(0.240, 'W/(m*K)')
cp_c = Q_(2890, 'J/(kg*K)')


# In[13]:


a_c = k_c/(rho_c*cp_c)
'{:0.2E}'.format(a_c.to('m**2/s'))    # part (c) answer

