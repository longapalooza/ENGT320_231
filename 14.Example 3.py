#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io #


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


T_s = Q_(500, 'K')
T_c = Q_(2000, 'K')
eps_1 = 0.1
eps_2 = 0.5
eps_3 = 0.8
lambda_1 = Q_(1.5, 'um')
lambda_2 = Q_(10, 'um')


# In[4]:


sigma = Q_(5.67*10**-8, 'W/(m^2*K^4)')    # Stefan-Boltzman constant #


# In[5]:


lamT_1 = lambda_1 * T_s
print(lamT_1)


# In[6]:


lamT_2 = lambda_2 * T_s
print(lamT_2)


# In[7]:


lamT_a = Q_(600, 'um*K')
lamT_b = Q_(800, 'um*K')
F_a = 0.000000
F_b = 0.000016
F_0lam1 = ((lamT_1 - lamT_a)/(lamT_b - lamT_a))*(F_b - F_a) + F_a
print(F_0lam1)


# In[8]:


F_0lam2 = 0.633726


# In[9]:


eps_s = eps_1*F_0lam1 + eps_2*(F_0lam2 - F_0lam1) + eps_3*(1 - F_0lam2)
print(eps_s)    # answer #


# In[10]:


E_s = eps_s*sigma*T_s**4
print(E_s.to('kW/m**2'))    # answer #


# In[11]:


lamT_1 = lambda_1*T_c
print(lamT_1)


# In[12]:


lamT_2 = lambda_2*T_c
print(lamT_2)


# In[13]:


F_0lam1 = 0.273229
F_0lam2 = 0.985554


# In[14]:


alpha = eps_1*F_0lam1 + eps_2*(F_0lam2 - F_0lam1) + eps_3*(1 - F_0lam2)
print(alpha)    # answer #

