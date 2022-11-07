#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io #


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


T = Q_(1600, 'K')
eps_1 = 0.4
eps_2 = 0.8
eps_3 = 0
lambda_1 = Q_(2, 'um')
lambda_2 = Q_(5, 'um')


# In[4]:


sigma = Q_(5.67*10**-8, 'W/(m^2*K^4)')    # Stefan-Boltzman constant #


# In[5]:


lamT_1 = lambda_1*T
print(lamT_1)


# In[6]:


lamT_2 = lambda_2*T
print(lamT_2)


# In[7]:


lamT_a = Q_(3000, 'um*K')
lamT_b = Q_(3400, 'um*K')
F_a = 0.273232
F_b = 0.361735
F_0lam1 = ((lamT_1 - lamT_a)/(lamT_b - lamT_a))*(F_b - F_a) + F_a
print(F_0lam1)


# In[8]:


F_0lam2 = 0.856288


# In[9]:


eps = eps_1*F_0lam1 + eps_2*(F_0lam2 - F_0lam1)
print(eps)    # answer #


# In[10]:


E = eps * sigma * T**4
print(E.to('kW/m**2'))    # answer #

