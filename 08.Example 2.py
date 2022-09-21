#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
ureg.setup_matplotlib()
Q_=ureg.Quantity


# In[3]:


u_inf=Q_(1, 'm/s')
L=Q_(0.6, 'm')
C_lam300=Q_(395, 'W/(m**1.5*K)')
C_tur300=Q_(2330, 'W/(m**1.8*K)')
C_lam350=Q_(477, 'W/(m**1.5*K)')
C_tur350=Q_(3600, 'W/(m**1.8*K)')


# In[4]:


def h_lamFunc(C, x):
    return C*x**-0.5

def h_turFunc(C, x):
    return C*x**-0.2


# In[5]:


v_f300=Q_(1.003E-3, 'm**3/kg')
mu_300=Q_(855E-6, 'N*s/m**2')
v_f350=Q_(1.027E-3, 'm**3/kg')
mu_350=Q_(365E-6, 'N*s/m**2')


# In[6]:


rho_300=1/v_f300
round(rho_300, 1)


# In[7]:


rho_350=1/v_f350
round(rho_350, 1)


# In[8]:


Re_xc=5E5


# In[9]:


x_c300=Re_xc*mu_300/(rho_300*u_inf)
round(x_c300.to('m'), 4)


# In[10]:


x_c350=Re_xc*mu_350/(rho_350*u_inf)
round(x_c350.to('m'), 4)


# In[11]:


hb_300=(1/L)*((C_lam300/0.5)*x_c300**0.5+(C_tur300/0.8)*(L**0.8-x_c300**0.8))
round(hb_300.to('kW/(m**2*K)'), 3)    # answer to first part 


# In[12]:


hb_350=(1/L)*((C_lam350/0.5)*x_c350**0.5+(C_tur350/0.8)*(L**0.8-x_c350**0.8))
round(hb_350.to('kW/(m**2*K)'), 3)    # answer to first part


# In[13]:


x_lam300=np.linspace(0.01, x_c300.to('m').magnitude, 100)*ureg.m
x_tur300=np.linspace(x_c300.to('m').magnitude, L.to('m').magnitude, 100)*ureg.m
x_300=np.concatenate([x_lam300.to('m').magnitude, x_tur300.to('m').magnitude])*ureg.m

x_lam350=np.linspace(0.01, x_c350.to('m').magnitude, 100)*ureg.m
x_tur350=np.linspace(x_c350.to('m').magnitude, L.to('m').magnitude, 100)*ureg.m
x_350=np.concatenate([x_lam350.to('m').magnitude, x_tur350.to('m').magnitude])*ureg.m

h_lam300=h_lamFunc(C_lam300, x_lam300)
h_tur300=h_turFunc(C_tur300, x_tur300)
h_300=np.concatenate([h_lam300.to('W/(m**2*K)').magnitude, h_tur300.to('W/(m**2*K)').magnitude])
h_300=h_300*(ureg.W)/(ureg.m**2*ureg.K)

h_lam350=h_lamFunc(C_lam350, x_lam350)
h_tur350=h_turFunc(C_tur350, x_tur350)
h_350=np.concatenate([h_lam350.to('W/(m**2*K)').magnitude, h_tur350.to('W/(m**2*K)').magnitude])
h_350=h_350*(ureg.W)/(ureg.m**2*ureg.K)


# In[14]:


x_300=x_300.to('m').magnitude
h_300=h_300.to('W/(m**2*K)').magnitude

x_350=x_350.to('m').magnitude
h_350=h_350.to('W/(m**2*K)').magnitude


# In[15]:


fig, ax=plt.subplots(1, 1)

ax.plot(x_300, h_300, color='k', label='$h$ at $300 K$')
ax.plot(x_350, h_350, color='k', linestyle='dashed', label='$h$ at $350 K$')

ax.set_xlabel('x $\\left(m\\right)$')
ax.set_ylabel('$h\\ \\left( \\frac{W}{m^2 K}\\right)$')

ax.axhline(hb_300.to('W/(m**2*K)').magnitude, color='k', linestyle='dotted', label='$\\bar{h}$ at $300 K$')
ax.axhline(hb_350.to('W/(m**2*K)').magnitude, color='k', linestyle='dashdot', label='$\\bar{h}$ at $350 K$')

ax.legend()

plt.show()

