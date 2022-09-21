#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


D=Q_(12.7, 'mm')
L=Q_(94, 'mm')
V=Q_(10, 'm/s')
T_inf=Q_(26.2, 'degC')
P=Q_(46, 'W')
T_s=Q_(128.4, 'degC')
f_l=Q_(15/100, '')


# In[4]:


def interp(x, x1, x2, y1, y2):
    return ((x-x1)/(x2-x1))*(y2-y1)+y1


# In[5]:


q=(1-f_l)*P
q


# In[6]:


A_s=math.pi*D*L
round(A_s, 0)


# In[7]:


hb1=q/(A_s*(T_s-T_inf))
round(hb1.to('W/(m**2*K)'), 1)    # answer to part 1


# In[8]:


T_f=(T_s.to('K')+T_inf.to('K'))/2
round(T_f.to('K'), 1)


# In[9]:


Ta=Q_(350, 'K')
Tb=Q_(400, 'K')
nua=Q_(20.92E-6, 'm**2/s')
nub=Q_(26.41E-6, 'm**2/s')
nu=interp(T_f, Ta, Tb, nua, nub)
'{:~.3E}'.format(nu)


# In[10]:


ka=Q_(30E-3, 'W/(m*K)')
kb=Q_(33.8E-3, 'W/(m*K)')
k=interp(T_f, Ta, Tb, ka, kb)
'{:~.3E}'.format(k)


# In[11]:


Pra=0.7
Prb=0.69
Pr=interp(T_f, Ta, Tb, Pra, Prb)
round(Pr, 4)


# In[12]:


Re_D=V*D/nu
round(Re_D.to(''), 0)


# In[13]:


C=0.193
m=0.618
Nub_D=C*Re_D**m*Pr**(1/3)
round(Nub_D.to(''), 2)


# In[14]:


hb2=Nub_D*k/D
round(hb2.to('W/(m**2*K)'), 2)    # answer to part 2


# In[15]:


pDiff=abs((hb2-hb1)/((hb2+hb1)/2))
round(pDiff, 4)

