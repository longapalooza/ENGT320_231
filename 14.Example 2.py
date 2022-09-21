#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io #


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


tau_1 = 0.9
lambda_1 = Q_(0.3, 'um')
lambda_2 = Q_(2.5,'um')


# In[4]:


T = Q_(5800, 'K')
lamT_1 = lambda_1 * T
print(lamT_1)


# In[5]:


lamT_2 = lambda_2 * T
print(lamT_2)


# In[6]:


lamT_a = Q_(1600, 'um*K')
lamT_b = Q_(1800, 'um*K')
F_a = 0.019719
F_b = 0.039342
F_0lam1 = ((lamT_1 - lamT_a)/(lamT_b - lamT_a))*(F_b - F_a) + F_a
print(F_0lam1)


# In[7]:


lamT_a = Q_(10000, 'um*K')
lamT_b = Q_(20000, 'um*K')
F_a = 0.914157
F_b = 0.985554
F_0lam2 = ((lamT_2 - lamT_a)/(lamT_b - lamT_a))*(F_b - F_a) + F_a
print(F_0lam2)


# In[8]:


tau = tau_1*(F_0lam2 - F_0lam1)
print(tau)    # answer #

