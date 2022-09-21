#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


H = Q_(0.15, 'm')
D = Q_(50, 'mm')
T_b = Q_(500, 'K')
T_inf = Q_(300, 'K')
h = Q_(50, 'W/(m**2*K)')
N = 5
t = Q_(6, 'mm')
L = Q_(20, 'mm')


# In[4]:


r_1 = D/2
r_1


# In[5]:


r_2 = r_1 + L
r_2


# In[6]:


k = Q_(186, 'W/(m*K)')


# In[7]:


A_f = 2*math.pi*(r_2**2 - r_1**2) + 2*math.pi*r_2*t
round(A_f.to('m**2'), 5)


# In[8]:


A_t = N*A_f + 2*math.pi*r_1*(H - N*t)
round(A_t.to('m**2'), 4)


# In[9]:


theta_b = T_b - T_inf
theta_b


# In[10]:


L_c = L + t/2
L_c


# In[11]:


A_p = L_c*t
A_p


# In[12]:


xAxisValue = L_c**(3/2)*(h/(k*A_p))**(1/2)
round(xAxisValue.to(''), 2)


# In[13]:


r_2c = r_2 + t/2
r_2c


# In[14]:


radiusRatio = r_2c/r_1
radiusRatio


# In[15]:


eta_f = 0.95


# In[16]:


q_t = h*A_t*(1 - ((N*A_f)/A_t)*(1 - eta_f))*theta_b
round(q_t.to('W'), 1)


# In[17]:


q_wo = h*2*math.pi*r_1*H*theta_b
round(q_wo.to('W'), 1)


# In[18]:


delq = q_t - q_wo
round(delq.to('W'), 1)    # answer

