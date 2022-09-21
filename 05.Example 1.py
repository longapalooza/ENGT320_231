#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


T_inf = Q_(10, 'degC')
h = Q_(2, 'W/(m**2*K)')
T_i = Q_(35, 'degC')
L_sf = Q_(3, 'mm')
k_sf = Q_(0.3, 'W/(m*K)')
A = Q_(1.8, 'm**2')
k_ins = Q_(0.014, 'W/(m*K)')
eps = 0.95
q = Q_(100, 'W')


# In[4]:


T_sur = T_inf


# In[5]:


sig = Q_(5.67*10**-8, 'W/(m^2*K^4)')    # Stefan-Boltzman constant


# In[6]:


T_s = T_i - q*L_sf/(k_sf*A)
round(T_s.to('degC'), 1)    # answer to second part


# In[7]:


R_tot = (T_i - T_inf)/q
R_tot


# In[8]:


T_1 = (T_i.to('K') + T_inf.to('K'))/2
T_1.to('degC')


# In[9]:


h_r = eps*sig*(T_1.to('K') + T_sur.to('K'))*(T_1.to('K')**2 + T_sur.to('K')**2)
round(h_r, 2)


# In[10]:


L_ins = k_ins*(A*R_tot - L_sf/k_sf - 1/(h + h_r))
round(L_ins, 2)


# In[11]:


T_1_check = T_s - q*L_ins/(k_ins*A)
round(T_1_check.to('degC'), 1)


# In[12]:


T_1 = T_1_check


# In[13]:


h_r = eps*sig*(T_1.to('K') + T_sur.to('K'))*(T_1.to('K')**2 + T_sur.to('K')**2)
round(h_r, 2)


# In[14]:


L_ins = k_ins*(A*R_tot - L_sf/k_sf - 1/(h + h_r))
round(L_ins, 2)


# In[15]:


T_1_check = T_s - q*L_ins/(k_ins*A)
round(T_1_check.to('degC'), 1)


# In[16]:


T_1 = T_1_check
h_r = eps*sig*(T_1.to('K') + T_sur.to('K'))*(T_1.to('K')**2 + T_sur.to('K')**2)
round(h_r, 2)


# In[17]:


L_ins = k_ins*(A*R_tot - L_sf/k_sf - 1/(h + h_r))
round(L_ins, 2)


# In[18]:


T_1_check = T_s - q*L_ins/(k_ins*A)
round(T_1_check.to('degC'), 1)


# In[19]:


round(L_ins, 2)    # answer to first part

