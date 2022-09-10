#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


L = Q_(1, 'm')    # wall thickness
a = Q_(800, 'delta_degC')
b = Q_(-300, 'delta_degC/m')
c = Q_(-50, 'delta_degC/m**2')
qdot = Q_(1000, 'W/m**3')
A = Q_(10, 'm**2')    # wall cross sectional area
k = Q_(40, 'W/(m*K)')
rho = Q_(1600, 'kg/m**3')
c_p = Q_(4, 'kJ/(kg*K)')
x_a1 = Q_(0, 'm')    # first position of interest in first part
x_a2 = Q_(1, 'm')    # second position of interest in first part
x_c1 = Q_(0, 'm')    # first position of interest in third part
x_c2 = Q_(0.25, 'm')    # second position of interest in third part
x_c3 = Q_(0.5, 'm')    # third position of interest in third part


# In[4]:


q_in = -k*A*(b + 2*c*x_a1)
round(q_in.to('kW'), 2)    # answer to first position in first part


# In[5]:


q_out = -k*A*(b + 2*c*x_a2)
round(q_out.to('kW'), 2)    # answer to second position in first part


# In[6]:


E_st = q_in + A*L*qdot - q_out
round(E_st.to('kW'), 2)    # answer to second part


# In[7]:


dTdt = k*2*c/(rho*c_p) + qdot/(rho*c_p)
'{:0.2E}'.format(dTdt.to('degC/s'))    # answer to third part

