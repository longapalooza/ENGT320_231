#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


qf=Q_(95000, 'W/m**2')
V=Q_(160, 'm/s')
T_inf=Q_(1150, 'degC')
T_s=Q_(800, 'degC')
L=Q_(40, 'mm')
T_s1=Q_(700, 'degC')
L_2=Q_(80, 'mm')
V_2=Q_(80, 'm/s')


# In[4]:


h=qf/(T_inf-T_s)
round(h.to('W/(m**2*K)'), 1)


# In[5]:


h_1=h
round(h_1.to('W/(m**2*K)'), 1)


# In[6]:


qf_1=h_1*(T_inf-T_s1)
round(qf_1.to('kW/(m**2)'), 1)    # answer to first part


# In[7]:


h_2=h*L/L_2
round(h_2.to('W/(m**2*K)'), 1)


# In[8]:


qf_2=h_2*(T_inf-T_s)
round(qf_2.to('kW/m**2'), 2)    # answer to the second part


# In[9]:


Tb=(T_s.to('K')+T_inf.to('K'))/2
round(Tb.to('degC'), 1)


# In[10]:


TA=Q_(1200, 'K')
TB=Q_(1300, 'K')
kA=Q_(76.3E-3, 'W/(m*K)')
kB=Q_(82E-3, 'W/(m*K)')
k=((Tb-TB)/(TA-TB))*(kA-kB)+kB
round(k.to('mW/(m*K)'), 2)


# In[11]:


Tb_1=(T_s1.to('K')+T_inf.to('K'))/2
round(Tb_1.to('degC'), 1)


# In[12]:


TA=Q_(1200, 'K')
TB=Q_(1300, 'K')
kA=Q_(76.3E-3, 'W/(m*K)')
kB=Q_(82E-3, 'W/(m*K)')
k_1=((Tb_1-TB)/(TA-TB))*(kA-kB)+kB
round(k_1.to('mW/(m*K)'), 2)


# In[13]:


h_1=h*k_1/k
round(h_1.to('W/(m**2*K)'), 1)


# In[14]:


qf_1=h_1*(T_inf-T_s1)
round(qf_1.to('kW/m**2'), 1)    # alternative answer to the first part

