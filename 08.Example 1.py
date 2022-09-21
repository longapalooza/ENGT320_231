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


def h_xFunc(x):
    return x**(-0.1)

def hb_xFunc(x):
    return (1/0.9)*h_xFunc(x)


# In[4]:


x=np.linspace(0.1, 4, 100)*ureg.m

h_x=h_xFunc(x)*(ureg.W/(ureg.m**(1.9)*ureg.K))
hb_x=hb_xFunc(x)*(ureg.W/(ureg.m**(1.9)*ureg.K))


# In[5]:


x=x.to('m').magnitude
h_x=h_x.to('W/(m**2*K)').magnitude
hb_x=hb_x.to('W/(m**2*K)').magnitude


# In[6]:


fig, ax=plt.subplots(1, 1)

ax.plot(x, h_x, color='k', label='$h_x$')
ax.plot(x, hb_x, color='k', linestyle='dashed', label='$\\bar{h}_x$')

ax.set_xlabel('x $\\left(m\\right)$')
ax.set_ylabel('$h\\ \\left( \\frac{W}{m^2 K}\\right)$')

ax.set_yticks([0, 0.5, 1, 1.5])
ax.set_yticklabels(['', '$0.5a$', '$a$', '$1.5a$'])

ax.legend()

plt.show()

