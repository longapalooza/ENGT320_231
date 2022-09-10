#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


N_gb = 0.93    # gear box efficiency
N_gen = 0.95    # generator efficiency
L = Q_(6, 'm')    # nacelle length
D = Q_(3, 'm')    # nacelle diameter
P = Q_(2.5, 'MW')    # turbine power produced
T_inf = Q_(25, 'degC')    # far field temperature
T_sur = Q_(20, 'degC')    # surrounding temperature
es = 0.83    # surface emissivity
h = Q_(35, 'W/(m^2*K)')    # convection coefficient


# In[4]:


sig = Q_(5.67*10**-8, 'W/(m^2*K^4)')    # Stefan-Boltzman constant


# In[5]:


Q_tot = P*(1/(N_gb*N_gen) - 1)
print(round(Q_tot.to('kW'), 2))


# In[6]:


A = math.pi*L*D + (math.pi/4)*D**2
print(round(A.to('m^2'), 2))


# In[7]:


def newton_raphson(f, x, tol=0.001):
    h = 0.000000001
    while(abs(f(x)) > tol):
        df = (f(x + h) - f(x))/h
        x = x - f(x)/df
    return x


# In[8]:


def hx_expr(T_s):
    Q_tot_ = Q_tot.to_base_units().magnitude
    h_ = h.to_base_units().magnitude
    A_ = A.to_base_units().magnitude
    T_inf_ = T_inf.to('K').magnitude
    sig_ = sig.to_base_units().magnitude
    T_sur_ = T_sur.to('K').magnitude
    return Q_tot_ - h_*A_*(T_s - T_inf_) - es*sig_*A_*(T_s**4 - T_sur_**4)


# In[9]:


T_s = Q_(newton_raphson(hx_expr, 100), 'K')
print(round(T_s, 1))
print(round(T_s.to('degC'), 1))    # answer

