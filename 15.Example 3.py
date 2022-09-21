#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


T_1 = Q_(1000, 'K')
r_o = Q_(20, 'mm')
eps = Q_(0.8, '')
mdot = Q_(0.01, 'kg/s')
T_m = Q_(400, 'K')


# In[4]:


sigma = Q_(5.67*10**-8, 'W/(m^2*K^4)')    # Stefan-Boltzman constant #


# In[5]:


A_1 = 2*r_o
A_1


# In[6]:


A_2 = math.pi*r_o
A_2


# In[7]:


F_12 = 1


# In[8]:


R_tot = (1 - eps)/(eps*A_1) + 1/(A_1*F_12) + (1 - eps)/(eps*A_2)
R_tot


# In[9]:


A_c = (math.pi*r_o**2)/2
A_c


# In[10]:


P = math.pi*r_o + 2*r_o
P


# In[11]:


D_h = 4*A_c/P
D_h


# In[12]:


cp = Q_(1.014, 'kJ/(kg*K)')
mu = Q_(230.1E-7, 'N*s/m**2')
k = Q_(33.8E-3, 'W/(m*K)')
Pr = 0.690


# In[13]:


Re_D = mdot*D_h/(A_c*mu)
Re_D.to('')


# In[14]:


Nu_D = 0.023*Re_D**(4/5)*Pr**0.4
Nu_D.to('')


# In[15]:


h = k*Nu_D.to('')/D_h
h.to('W/(m**2*K)')


# In[16]:


T_2 = Q_(1000, 'K')


# In[17]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[18]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[19]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[20]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[21]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[22]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[23]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[24]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[25]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[26]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[27]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[28]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[29]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[30]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')


# In[31]:


T_2 = (sigma*(T_1**4 - T_2**4)/R_tot + h*A_2*T_m)/(h*A_2)
T_2.to('K')    # answer #

