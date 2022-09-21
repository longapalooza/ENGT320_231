#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


m_fuel = Q_(4.8, 'kg')
q_fuel = Q_(0.54, 'W/g')
T_H = Q_(550, 'degC')
T_L = Q_(230, 'degC')
W_outrtg = Q_(110, 'W')
Q_Lrtg = Q_(2, 'kW')


# In[4]:


N_threv = 1 - T_L.to('K')/T_H.to('K')
N_threv


# In[5]:


Q_Hfuel = m_fuel*q_fuel
Q_Hfuel.to('kW')


# In[6]:


W_outmax = N_threv*Q_Hfuel
round(W_outmax.to('kW'), 3)    # answer to first part


# In[7]:


Q_Hrtg = W_outrtg + Q_Lrtg
Q_Hrtg.to('kW')


# In[8]:


N_thrtg = W_outrtg/Q_Hrtg
'{:1.2f}%'.format(100*N_thrtg.magnitude)    # answer to second part

