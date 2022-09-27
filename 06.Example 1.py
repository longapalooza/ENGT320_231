#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as plt
import numpy as np
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


D = Q_(5, 'mm')
T_b = Q_(100, 'degC')
T_inf = Q_(25, 'degC')
h = Q_(100, 'W/(m**2*K)')


# In[4]:


Tbar = (T_b.to('K') + T_inf.to('K'))/2
Tbar.to('K')


# In[5]:


T_A = Q_(200, 'K')
T_B = Q_(400, 'K')
k_A = Q_(413, 'W/(m*K)')
k_B = Q_(393, 'W/(m*K)')
k_cu = ((Tbar - T_A)/(T_B - T_A))*(k_B - k_A) + k_A
round(k_cu, 2)


# In[6]:


T_A = Q_(200, 'K')
T_B = Q_(400, 'K')
k_A = Q_(163, 'W/(m*K)')
k_B = Q_(186, 'W/(m*K)')
k_al = ((Tbar - T_A)/(T_B - T_A))*(k_B - k_A) + k_A
round(k_al, 2)


# In[7]:


T_A = Q_(300, 'K')
T_B = Q_(400, 'K')
k_A = Q_(13.4, 'W/(m*K)')
k_B = Q_(15.2, 'W/(m*K)')
k_ss = ((Tbar - T_A)/(T_B - T_A))*(k_B - k_A) + k_A
round(k_ss, 2)


# In[8]:


m_cu = (4*h/(k_cu*D))**0.5
round(m_cu.to('1/m'), 2)


# In[9]:


m_al = (4*h/(k_al*D))**0.5
round(m_al.to('1/m'), 2)


# In[10]:


m_ss = (4*h/(k_ss*D))**0.5
round(m_ss.to('1/m'), 2)


# In[11]:


def Tdist(x, m):
    return (T_b.to('K') - T_inf.to('K'))*math.e**(-m*x) + T_inf.to('K')


# In[12]:


x = np.linspace(0, 350)*ureg.mm


# In[13]:


T_cu = Tdist(x, m_cu)
T_al = Tdist(x, m_al)
T_ss = Tdist(x, m_ss)


# In[14]:


fig, ax = plt.subplots(1, 1)

ax.plot(x.to('mm').magnitude, T_cu.to('degC').magnitude, label = 'Copper')
ax.plot(x.to('mm').magnitude, T_al.to('degC').magnitude, label = 'Aluminum')
ax.plot(x.to('mm').magnitude, T_ss.to('degC').magnitude, label = 'Stainless Steel')

ax.set_xlabel('Position along fin (mm)')
ax.set_ylabel('Fin temperature ($^\\circ C$)')
ax.set_title('Fin temperature distribution')

ax.axhline(y = T_b.to('degC').magnitude, color = 'k')
ax.axhline(y = T_inf.to('degC').magnitude, color = 'k')

ax.set_ylim([20, 105])
ax.set_yticks(range(25, 110, 10))

ax.legend()
plt.show()


# In[15]:


q_cu = ((math.pi**2*h*k_cu*D**3)/4)**0.5*(T_b - T_inf)
round(q_cu.to('W'), 2)    # answer to second portion of part (a)


# In[16]:


q_al = ((math.pi**2*h*k_al*D**3)/4)**0.5*(T_b - T_inf)
round(q_al.to('W'), 2)    # answer to second portion of part (a)


# In[17]:


q_ss = ((math.pi**2*h*k_ss*D**3)/4)**0.5*(T_b - T_inf)
round(q_ss.to('W'), 2)    # answer to second portion of part (a)


# In[18]:


math.atanh(0.99)


# In[19]:


L_cu = math.atanh(0.99)/((4*h)/(k_cu*D))**0.5
round(L_cu.to('mm'), 1)    # answer to part (b)


# In[20]:


L_al = math.atanh(0.99)/((4*h)/(k_al*D))**0.5
round(L_al.to('mm'), 1)    # answer to part (b)


# In[21]:


L_ss = math.atanh(0.99)/((4*h)/(k_ss*D))**0.5
round(L_ss.to('mm'), 1)    # answer to part (b)

