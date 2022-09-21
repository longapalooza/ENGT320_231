#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io #


# In[2]:


ureg=pint.UnitRegistry()
Q_=ureg.Quantity


# In[3]:


D_i=Q_(25, 'mm')
m_c=Q_(0.2, 'kg/s')
D_o=Q_(45, 'mm')
m_h=Q_(0.1, 'kg/s')
T_hi=Q_(100, 'degC')
T_ci=Q_(30, 'degC')
T_ho=Q_(60, 'degC')


# In[4]:


Tbar_h=(T_hi.to('K')+T_ho.to('K'))/2
round(Tbar_h.to('K'), 1)


# In[5]:


Ta=Q_(350, 'K')
Tb=Q_(360, 'K')
c_pa=Q_(2.118, 'kJ/(kg*K)')
c_pb=Q_(2.161, 'kJ/(kg*K)')
c_ph=((Tbar_h-Ta)/(Tb-Ta))*(c_pb-c_pa)+c_pa
round(c_ph.to('kJ/(kg*K)'), 3)


# In[6]:


mua=Q_(3.56E-2, 'N*s/m**2')
mub=Q_(2.52E-2, 'N*s/m**2')
mu_h=((Tbar_h-Ta)/(Tb-Ta))*(mub-mua)+mua
'{:~.3E}'.format(mu_h.to('N*s/m**2'))


# In[7]:


k_h=Q_(138E-3, 'W/(m*K)')


# In[8]:


T_co=Q_(35, 'degC')


# In[9]:


Tbar_c=(T_ci.to('K')+T_co.to('K'))/2
round(Tbar_c.to('K'), 1)


# In[10]:


c_pc=Q_(4.178, 'kJ/(kg*K)')


# In[11]:


T_co=T_ci+(m_h*c_ph*(T_hi-T_ho))/(m_c*c_ph)
round(T_co.to('degC'), 1)


# In[12]:


Tbar_c=(T_ci.to('K')+T_co.to('K'))/2
round(Tbar_c.to('K'), 1)


# In[13]:


Ta=Q_(310, 'K')
Tb=Q_(315, 'K')
c_pa=Q_(4.178, 'kJ/(kg*K)')
c_pb=Q_(4.179, 'kJ/(kg*K)')
c_pc=((Tbar_c-Ta)/(Tb-Ta))*(c_pb-c_pa)+c_pa
round(c_pc.to('kJ/(kg*K)'), 3)


# In[14]:


T_co=T_ci+(m_h*c_ph*(T_hi-T_ho))/(m_c*c_ph)
round(T_co.to('degC'), 1)


# In[15]:


mua=Q_(695E-6, 'N*s/m**2')
mub=Q_(631E-6, 'N*s/m**2')
mu_c=((Tbar_c-Ta)/(Tb-Ta))*(mub-mua)+mua
'{:~.3E}'.format(mu_c.to('N*s/m**2'))


# In[16]:


ka=Q_(628E-3, 'W/(m*K)')
kb=Q_(634E-3, 'W/(m*K)')
k_c=((Tbar_c-Ta)/(Tb-Ta))*(kb-ka)+ka
'{:~.3E}'.format(k_c.to('W/(m*K)'))


# In[17]:


Pra=Q_(4.62, '')
Prb=Q_(4.16, '')
Pr_c=((Tbar_c-Ta)/(Tb-Ta))*(Prb-Pra)+Pra
round(Pr_c.to(''), 3)


# In[18]:


delT_1=T_hi-T_co
round(delT_1.to('K'), 1)


# In[19]:


delT_2=T_ho-T_ci
round(delT_2.to('K'), 1)


# In[20]:


delT_lm=(delT_2-delT_1)/math.log(delT_2/delT_1)
round(delT_lm.to('K'), 1)


# In[21]:


q=m_c*c_pc*(T_co-T_ci)
round(q.to('kW'), 2)


# In[22]:


Re_D=4*m_c/(math.pi*D_i*mu_c)
'{:~.3E}'.format(Re_D.to(''))


# In[23]:


Nu_D=0.023*Re_D**(4/5)*Pr_c**0.4
round(Nu_D.to(''), 2)


# In[24]:


h_i=Nu_D*k_c/D_i
round(h_i.to('W/(m**2*K)'), 1)


# In[25]:


D_h=D_o-D_i
round(D_h.to('mm'), 2)


# In[26]:


Re_D=4*m_h/(math.pi*(D_o+D_i)*mu_h)
round(Re_D.to(''), 2)


# In[27]:


Dr=D_i/D_o
round(Dr, 3)


# In[28]:


Dra=0.5
Drb=1
Nua=4.43
Nub=4.86
Nu_D=((Dr-Dra)/(Drb-Dra))*(Nub-Nua)+Nua
round(Nu_D, 3)


# In[29]:


h_o=Nu_D*k_h/D_h
round(h_o.to('W/(m**2*K)'), 2)


# In[30]:


U=1/(1/h_i+1/h_o)
U=U.to('W/(m**2*K)').magnitude   # NOTE: This is done beceause there appears to be a bug in pint. #
U=Q_(U, 'W/(m**2*K)')
round(U.to('W/(m**2*K)'), 2)


# In[31]:


L=q/(U*math.pi*D_i*delT_lm)
round(L.to('m'), 1)    # answer #

