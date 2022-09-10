#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


T_a = Q_(550, 'K')
T_b = Q_(800, 'K')
T_c = Q_(375, 'K')


# In[4]:


k_B = Q_(1.381*10**-23, 'J/K')    # Boltzman's constant
N_a = Q_(6.022*10**23, '1/mol')    # Avogadro's Number


# In[5]:


Mw_a = Q_(28.97, 'kg/kmol')
Mw_b = Q_(44.01, 'kg/kmol')
Mw_c = Q_(2.016, 'kg/kmol')
d_a = Q_(0.372, 'nm')
d_b = Q_(0.464, 'nm')
d_c = Q_(0.274, 'nm')


# In[6]:


cp_a = Q_(1.040, 'kJ/(kg*K)')
k_a = Q_(43.9*10**-3, 'W/(m*K)')
cp_b = Q_(1.17, 'kJ/(kg*K)')
k_b = Q_(55.1*10**-3, 'W/(m*K)')
cp_c = Q_(((375 - 350)/(400 - 350))*(14.48 - 14.43) + 14.43, 'kJ/(kg*K)')
k_c = Q_(((375 - 350)/(400 - 350))*(226*10**-3 - 204*10**-3) + 204*10**-3, 'W/(m*K)')


# In[7]:


cp_c


# In[8]:


k_c


# In[9]:


def cv(cp, d, k, Mw, T):
    part1 = 9*cp
    part2 = 4*math.pi*d**2*k
    part3 = (Mw*k_B*T)/(N_a*math.pi)
    part4 = part1 - part2/(part3)**0.5    # pint does not like math.sqrt so **0.5 is used here
    return part4/5


# In[10]:


cv_a = cv(cp_a, d_a, k_a, Mw_a, T_a)
cv_b = cv(cp_b, d_b, k_b, Mw_b, T_b)
cv_c = cv(cp_c, d_c, k_c, Mw_c, T_c)


# In[11]:


cv_a


# In[12]:


cv_b


# In[13]:


cv_c


# In[14]:


g_a = cp_a/cv_a
g_b = cp_b/cv_b
g_c = cp_c/cv_c


# In[15]:


round(g_a.magnitude, 2)    # part (a) answer


# In[16]:


round(g_b.magnitude, 2)    # part (b) answer


# In[17]:


round(g_c.magnitude, 2)    # part (c) answer

