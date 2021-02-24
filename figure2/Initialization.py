# -*- coding: utf-8 -*-


import numpy as np

def pz_theta_model(x, theta_r):
    # x can be np.array of size 2 or a list of two np.array x1 and x2
#    x = x[0]
    a = theta_r[0]
    b = theta_r[1]
    
    pyx = np.exp(x)/(1+np.exp(x))*0.6+0.2  #average center
    cx = a*np.exp(-x**2)+b*(np.exp(-(x-4)**2)+np.exp(-(x+4)**2));# additive uncertainty
#    pzx_theta = np.exp(x+cx)/(1+np.exp(x+cx))
    pzx_theta = pyx+cx
    return pzx_theta

py_eq_z = None

def Initialization(xnum = 101, thetanum = 21):
    xspace = np.linspace(-4, 4, xnum)
    yspace = None
    alist = np.linspace(-0.1, 0.1, thetanum)
    blist = np.linspace(-0.2, 0.2, thetanum)
    thetalist = [np.array([a, b]) for a in alist for b in blist]
    
    return xspace, yspace, thetalist

classnum = 2
multiclass = False