#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


T_1=Q_(1200, 'K')
T_2=Q_(500, 'K')
W=Q_(1, 'm')
eps_1=Q_(0.8, '')
eps_R=Q_(0.8, '')
eps_2=Q_(0.4, '')


# In[4]:


sigma=Q_(5.67*10**-8, 'W/(m^2*K^4)')    # Stefan-Boltzman constant #


# In[5]:


F_12=0.5
F_1R=0.5
F_2R=0.5


# In[6]:


R_totL=((1-eps_1)/(eps_1*W)
        +1/(W*F_12+(1/(1/(W*F_1R)+1/(W*F_2R))))
        +(1-eps_2)/(eps_2*W))
round(R_totL.to('1/m'), 3)


# In[7]:


qp_1=sigma*(T_1**4-T_2**4)/R_totL
round(qp_1.to('kW/m'), 2)    # answer #


# In[8]:


qp_2=-qp_1
round(qp_2.to('kW/m'), 2)


# In[9]:


J_1=sigma*T_1**4-((1-eps_1)/(eps_1*W))*qp_1
round(J_1.to('kW/m**2'), 1)


# In[10]:


J_2=sigma*T_2**4-((1-eps_2)/(eps_2*W))*qp_2
round(J_2.to('kW/m**2'), 1)


# In[11]:


qp_12=(J_1-J_2)/(1/(W*F_12))
round(qp_12.to('kW/m'), 2)


# In[12]:


qp_1R=qp_1-qp_12
round(qp_1R.to('kW/m'), 2)


# In[13]:


J_R=J_1-(1/(W*F_1R))*qp_1R
round(J_R.to('kW/m**2'), 2)


# In[14]:


T_R=(J_R/sigma)**(1/4)
round(T_R, 1)    # answer #

