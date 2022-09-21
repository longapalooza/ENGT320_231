#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


P_gen = Q_(9, 'W')
T_c = Q_(56.4, 'degC')
q = Q_(11.25, 'W')
V = Q_(9.4, 'm/s')
T_inf = Q_(25, 'degC')
W = Q_(50, 'mm')
H = Q_(26, 'mm')
t_g = Q_(10, 'mm')
W_c = Q_(50, 'mm')
L_c = Q_(50, 'mm')
t_c = Q_(6, 'mm')
C = Q_(1000, 'W/(m**3/s)')
k_al = Q_(200, 'W/(m*K)')
t_b = Q_(2, 'mm')
L_f = Q_(8, 'mm')
t_f = Q_(1, 'mm')
L_c = Q_(50, 'mm')


# In[4]:


k_air = Q_(0.0263, 'W/(m*K)')


# In[5]:


A_c = W*(H - t_c)
A_c


# In[6]:


V_f = A_c*V
round(V_f.to('cm**3/s'), 0)


# In[7]:


P_f = C*V_f
round(P_f.to('W'), 1)


# In[8]:


P_net = P_gen - P_f
round(P_net.to('W'), 1)    # answer to part 1


# In[9]:


R_tbase = t_b/(k_al*2*L_c*W_c)
round(R_tbase.to('K/W'), 4)


# In[10]:


P = 2*(L_c + t_f)
P


# In[11]:


A_c = L_c*t_f
A_c


# In[12]:


N = 20


# In[13]:


a = (2*W_c - N*t_f)/N
round(a.to('mm'), 2)


# In[14]:


h = 1.78*k_air*((L_f + a)/(L_f*a))
round(h.to('W/(m**2*K)'), 2)


# In[15]:


m = ((h*P)/(k_al*A_c))**0.5
round(m.to('1/m'), 2)


# In[16]:


R_tf = 1/((h*P*k_al*A_c)**0.5*math.tanh(m*L_f))
round(R_tf.to('K/W'), 2)


# In[17]:


R_tfN = R_tf/N
round(R_tfN.to('K/W'), 2)


# In[18]:


R_tb = 1/(h*(2*W_c - N*t_f)*L_c)
round(R_tb.to('K/W'), 2)


# In[19]:


R_tot = R_tbase + 1/((1/R_tb) + (1/R_tfN))
round(R_tot.to('K/W'), 2)


# In[20]:


T_c = R_tot*q + T_inf.to('K')
round(T_c.to('degC'), 1)


# In[21]:


N = 22


# In[22]:


a = (2*W_c - N*t_f)/N
round(a.to('mm'), 2)


# In[23]:


h = 1.78*k_air*((L_f + a)/(L_f*a))
round(h.to('W/(m**2*K)'), 2)


# In[24]:


m = ((h*P)/(k_al*A_c))**0.5
round(m.to('1/m'), 2)


# In[25]:


R_tf = 1/((h*P*k_al*A_c)**0.5*math.tanh(m*L_f))
round(R_tf.to('K/W'), 2)


# In[26]:


R_tfN = R_tf/N
round(R_tfN.to('K/W'), 2)


# In[27]:


R_tb = 1/(h*(2*W_c - N*t_f)*L_c)
round(R_tb.to('K/W'), 2)


# In[28]:


R_tot = R_tbase + 1/((1/R_tb) + (1/R_tfN))
round(R_tot.to('K/W'), 2)


# In[29]:


T_c = R_tot*q + T_inf.to('K')
round(T_c.to('degC'), 1)


# In[30]:


N    # answer to part 2

