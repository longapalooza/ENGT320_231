#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


L_H2=Q_(40, 'mm')
p_H2=Q_(2, 'atm')
V_H2=Q_(8.1, 'm/s')
T_infH2=Q_(-30, 'degC')
T_sH2=Q_(-15, 'degC')
T_infAir=Q_(23, 'degC')
L_Air=Q_(60, 'mm')
P=Q_(150, 'mm')
T_sAir=Q_(30, 'degC')
qp_Air=Q_(50, 'W/m')


# In[4]:


Tb_H2=(T_sH2.to('K')+T_infH2.to('K'))/2
round(Tb_H2, 1)


# In[5]:


Tb_Air=(T_sAir.to('K')+T_infAir.to('K'))/2
round(Tb_Air, 1)


# In[6]:


TA=Q_(250, 'K')
TB=Q_(300, 'K')
nuA=Q_(81.4E-6, 'm**2/s')
nuB=Q_(111E-6, 'm**2/s')
kA=Q_(157E-3, 'W/(m*K)')
kB=Q_(183E-3, 'W/(m*K)')
PrA=Q_(0.707, '')
PrB=Q_(0.701, '')

nu_H2=((Tb_H2-TB)/(TA-TB))*(nuA-nuB)+nuB
'{:.3E}'.format(nu_H2)


# In[7]:


k_H2=((Tb_H2-TB)/(TA-TB))*(kA-kB)+kB
round(k_H2.to('mW/(m*K)'), 1)


# In[8]:


Pr_H2=((Tb_H2-TB)/(TA-TB))*(PrA-PrB)+PrB
'{:.3E}'.format(Pr_H2)


# In[9]:


TA=Q_(250, 'K')
TB=Q_(300, 'K')
nuA=Q_(11.44E-6, 'm**2/s')
nuB=Q_(15.89E-6, 'm**2/s')
kA=Q_(22.3E-3, 'W/(m*K)')
kB=Q_(26.3E-3, 'W/(m*K)')
PrA=Q_(0.720, '')
PrB=Q_(0.707, '')

nu_Air=((Tb_Air-TB)/(TA-TB))*(nuA-nuB)+nuB
'{:.3E}'.format(nu_Air)


# In[10]:


k_Air=((Tb_Air-TB)/(TA-TB))*(kA-kB)+kB
round(k_Air.to('W/(m*K)'), 2)


# In[11]:


Pr_Air=((Tb_Air-TB)/(TA-TB))*(PrA-PrB)+PrB
'{:.3E}'.format(Pr_Air)


# In[12]:


nu_H2=(Q_(1, 'atm')/p_H2)*nu_H2
'{:.3E}'.format(nu_H2)


# In[13]:


V_Air=V_H2*(L_H2/L_Air)*(nu_Air/nu_H2)
round(V_Air, 3)    # answer to first part


# In[14]:


qbf_Air=qp_Air/P
round(qbf_Air.to('W/m**2'), 1)


# In[15]:


hb_Air=qbf_Air/(T_sAir-T_infAir)
round(hb_Air.to('W/(m**2*K)'), 2)


# In[16]:


hb_H2=hb_Air*(L_Air/L_H2)*(k_H2/k_Air)
round(hb_H2.to('W/(m**2*K)'), 1)    # answer to second part

