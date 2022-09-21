#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


P=Q_(6, 'kPa')
T_inf=Q_(300, 'degC')
u_inf=Q_(10, 'm/s')
L=Q_(0.5, 'm')
T_s=Q_(27, 'degC')


# In[4]:


def interp(x, x1, x2, y1, y2):
    return ((x-x1)/(x2-x1))*(y2-y1)+y1


# In[5]:


T_f=(T_inf.to('K')+T_s.to('K'))/2
round(T_f.to('K'), 1)


# In[6]:


Ta=Q_(400, 'K')
Tb=Q_(450, 'K')
nua=Q_(26.41E-6, 'm**2/s')
nub=Q_(32.39E-6, 'm**2/s')
nu_1=interp(T_f, Ta, Tb, nua, nub)
'{:~.3E}'.format(nu_1)


# In[7]:


ka=Q_(33.8E-3, 'W/(m*K)')
kb=Q_(37.3E-3, 'W/(m*K)')
k=interp(T_f, Ta, Tb, ka, kb)
'{:~.3E}'.format(k)


# In[8]:


Pra=0.69
Prb=0.686
Pr=interp(T_f, Ta, Tb, Pra, Prb)
round(Pr, 4)


# In[9]:


nu=nu_1*Q_(1, 'atm')/P
'{:~.3E}'.format(nu.to('m**2/s'))


# In[10]:


Re_L=u_inf*L/nu
round(Re_L.to(''), 0)


# In[11]:


Nub_L=0.664*Re_L**(1/2)*Pr**(1/3)
round(Nub_L.to(''), 2)


# In[12]:


hb=Nub_L*k/L
round(hb.to('W/(m**2*K)'), 3)


# In[13]:


qp=hb*L*(T_inf-T_s)
round(qp.to('W/m'), 1)    # answer

