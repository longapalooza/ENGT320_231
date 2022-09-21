#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io #


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


T = Q_(2000, 'K')
F_1 = Q_(0.1, '')
F_2 = Q_(1-0.1, '')


# In[4]:


sigma = Q_(5.67*10**-8, 'W/(m^2*K^4)')    # Stefan-Boltzman constant #


# In[5]:


E = sigma*T**4
round(E.to('kW/m**2'), 1)    # answer #


# In[6]:


Fa = Q_(0.066730, '')
Fb = Q_(0.100890, '')
lambdaTa = Q_(2000, 'um*K')
lambdaTb = Q_(2200, 'um*K')
lambdaT_1 = ((F_1 - Fa)/(Fb - Fa))*(lambdaTb - lambdaTa) + lambdaTa
round(lambdaT_1.to('um*K'), 1)


# In[7]:


lambda_1 = lambdaT_1/T
round(lambda_1.to('um'), 3)    # answer #


# In[8]:


Fa = Q_(0.889989, '')
Fb = Q_(0.903044, '')
lambdaTa = Q_(9000, 'um*K')
lambdaTb = Q_(9500, 'um*K')
lambdaT_2 = ((F_2 - Fa)/(Fb - Fa))*(lambdaTb - lambdaTa) + lambdaTa
round(lambdaT_2.to('um*K'), 1)


# In[9]:


lambda_2 = lambdaT_2/T
round(lambda_2.to('um'), 3)    # answer #


# In[10]:


lambda_maxT = Q_(2898, 'um*K')
lambda_max = lambda_maxT/T
round(lambda_max.to('um'), 3)    # answer #


# In[11]:


IsigT = Q_(0.722318E-4, '1/(um*K*sr)')


# In[12]:


I = IsigT*sigma*T**5
round(I.to('kW/(m**2*sr*um)'), 1)


# In[13]:


E = Q_(math.pi, 'sr')*I
round(E.to('kW/(m**2*um)'), 1)    # answer #


# In[14]:


G = sigma*T**4
round(G.to('kW/m**2'), 1)    # answer #

