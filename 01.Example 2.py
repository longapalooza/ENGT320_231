#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as plt
import numpy as np
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
ureg.setup_matplotlib(True)
Q_ = ureg.Quantity


# In[3]:


D = Q_(1, 'mm')
L = Q_(1, 'm')
R_e = Q_(0.4, 'ohm/m')
T_inf = Q_(300, 'K')
T_sur = Q_(300, 'K')
h = Q_(100, 'W/(m^2 K)')
es = 0.8


# In[4]:


sig = Q_(5.67*10**-8, 'W/(m^2 K^4)')


# In[5]:


def newton_raphson(f, x, xFixed, tol = 0.001):
    h = 0.000000001
    while(abs(f(x, xFixed)) > tol):
        df = (f(x + h, xFixed) - f(x, xFixed))/h
        x = x - f(x, xFixed)/df
    return x


# In[6]:


def hx_expr(T_s, I):
    I_ = I.to_base_units().magnitude
    R_e_ = R_e.to_base_units().magnitude
    L_ = L.to_base_units().magnitude
    h_ = h.to_base_units().magnitude
    D_ = D.to_base_units().magnitude
    T_inf_ = T_inf.to('K').magnitude
    sig_ = sig.to_base_units().magnitude
    T_sur_ = T_sur.to('K').magnitude
    return I_**2*R_e_*L_ - h_*math.pi*D_*L_*(T_s - T_inf_) - es*sig_*math.pi*D_*L_*(T_s**4 - T_sur_**4)


# In[7]:


I = np.linspace(0, 10, 50)*ureg.A


# In[8]:


T_s = []
for Ie in I:
    T_s.append(newton_raphson(hx_expr, 100, Ie))
T_s = T_s*ureg.K


# In[9]:


fig, ax = plt.subplots(1, 1)
ax.plot(I, T_s)
ax.set_xlabel('Current, $I\\ \\left(A \\right)$')
ax.set_ylabel('Surface Temperature, $T_s \\ \\left( K \\right)$')
ax.set_title('Rod Surface Temperature versus Current Flow')
plt.show()

