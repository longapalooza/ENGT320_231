#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint # https://pint.readthedocs.io


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


lambda_0=Q_(0, 'um')
G_0=Q_(0, 'W/(m**2*um)')
lambda_1=Q_(5, 'um')
G_1=Q_(1000, 'W/(m**2*um)')
lambda_2=Q_(20, 'um')
G_2=G_1
lambda_3=Q_(25, 'um')
G_3=G_0


# In[4]:


G=0.5*(G_1-G_0)*(lambda_1-lambda_0)+G_1*(lambda_2-lambda_1)+0.5*(G_2-G_3)*(lambda_3-lambda_2)
round(G.to('kW/m**2'), 2)    # answer #

