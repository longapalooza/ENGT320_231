#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io #


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


A_1=Q_(1E-3, 'm**2')
I_n=Q_(7000, 'W/(m**2*sr)')
A_2=A_1
A_3=A_2
A_4=A_3
r=Q_(0.5, 'm')


# In[4]:


theta_2=Q_(60, 'deg')
theta_3=Q_(0, 'deg')
theta_4=Q_(45, 'deg')


# In[5]:


A_2n=A_2*math.sin(theta_2)
'{:~.3E}'.format(A_2n)


# In[6]:


omega_21=A_2n/r**2
'{:~.3E}'.format(omega_21.to('sr'))    # answer #


# In[7]:


omega_31=A_3/r**2
'{:~.3E}'.format(omega_31.to('sr'))    # answer #


# In[8]:


omega_41=A_4/r**2
'{:~.3E}'.format(omega_41.to('sr'))    # answer #


# In[9]:


q_12=I_n*A_1*math.cos(theta_2)*omega_21
round(q_12.to('mW'), 2)    # answer #


# In[10]:


q_13=I_n*A_1*math.cos(theta_3)*omega_31
round(q_13.to('mW'), 2)    # answer #


# In[11]:


q_14=I_n*A_1*math.cos(theta_4)*omega_41
round(q_14.to('mW'), 2)    # answer #

