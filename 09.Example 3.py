#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as plt
import numpy as np
import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


T_inf=Q_(25, 'degC')
D=Q_(10, 'mm')
V=Q_(15, 'm/s')
T_s=Q_(75, 'degC')


# In[4]:


def interp(x, x1, x2, y1, y2):
    return ((x-x1)/(x2-x1))*(y2-y1)+y1


# In[5]:


T_f=(T_inf.to('K')+T_s.to('K'))/2
round(T_f.to('K'), 1)


# In[6]:


Ta=Q_(250, 'K')
Tb=Q_(300, 'K')
Tc=Q_(350, 'K')
rhob=Q_(1.1614, 'kg/m**3')
rhoc=Q_(0.995, 'kg/m**3')
rho_f=interp(T_f, Tb, Tc, rhob, rhoc)
round(rho_f, 3)


# In[7]:


mua=Q_(159.6E-7, 'N*s/m')
mub=Q_(185.6E-7, 'N*s/m')
muc=Q_(208.2E-7, 'N*s/m')
mu_inf=interp(T_inf, Ta, Tb, mua, mub)
'{:~.3E}'.format(mu_inf)


# In[8]:


mu_s=interp(T_s, Tb, Tc, mub, muc)
'{:~.3E}'.format(mu_s)


# In[9]:


nua=Q_(11.44E-6, 'm**2/s')
nub=Q_(15.89E-6, 'm**2/s')
nuc=Q_(20.92E-6, 'm**2/s')
nu_inf=interp(T_inf, Ta, Tb, nua, nub)
'{:~.3E}'.format(nu_inf)


# In[10]:


nu_f=interp(T_f, Tb, Tc, nub, nuc)
'{:~.3E}'.format(nu_f)


# In[11]:


ka=Q_(22.3E-3, 'W/(m*K)')
kb=Q_(26.3E-3, 'W/(m*K)')
k_inf=interp(T_inf, Ta, Tb, ka, kb)
'{:~.3E}'.format(k_inf)


# In[12]:


Pra=Q_(0.72, '')
Prb=Q_(0.707, '')
Pr_inf=interp(T_inf, Ta, Tb, Pra, Prb)
round(Pr_inf, 4)


# In[13]:


Re_D=V*D/nu_f
round(Re_D.to(''), 0)


# In[14]:


C_D=0.4


# In[15]:


A_f=(math.pi/4)*D**2
round(A_f.to('mm**2'), 2)


# In[16]:


F_D=(C_D*A_f*rho_f*V**2)/2
round(F_D.to('mN'), 3)    # answer to part 1


# In[17]:


Re_D=V*D/nu_inf
round(Re_D.to(''), 0)


# In[18]:


round(Pr_inf, 2)


# In[19]:


round(mu_inf/mu_s, 1)


# In[20]:


Nub_D=2+(0.4*Re_D**(1/2)+0.06*Re_D**(2/3))*Pr_inf**(0.4)*(mu_inf/mu_s)**(1/4)
round(Nub_D, 2)


# In[21]:


hb=Nub_D*k_inf/D
round(hb.to('W/(m**2*K)'), 1)


# In[22]:


A_s=math.pi*D**2
round(A_s.to('mm**2'), 1)


# In[23]:


q=hb*A_s*(T_s-T_inf)
round(q.to('W'), 3)    # answer to part 2


# In[24]:


def heat_rate(V):
    Re_D=V*D/nu_inf
    Nub_D=2+(0.4*Re_D**(1/2)+0.06*Re_D**(2/3))*Pr_inf**(0.4)*(mu_inf/mu_s)**(1/4)
    hb=Nub_D*k_inf/D
    q=hb*A_s*(T_s-T_inf)
    return q


# In[25]:


Vvals=np.linspace(1, 25, 100)*ureg.m/ureg.s
qvals=heat_rate(Vvals)


# In[26]:


Vvals=Vvals.to('m/s').magnitude
qvals=qvals.to('W').magnitude


# In[27]:


fig, ax=plt.subplots(1, 1)

ax.plot(Vvals, qvals, color='k')

ax.set_xlabel('V $\\left(m/s\\right)$')
ax.set_ylabel('$q\\ \\left( W \\right)$')

ax.set_title('Heat rate vs. Velocity')

plt.show()

