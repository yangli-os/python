# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:32:23 2018

@author: liyang
"""
import numpy as np
import matplotlib.pylab  as plt
import scipy.stats as st 
theta_real=0.35
trials=[0,1,2,3,4,8,16,32,50,150]
data=[0,1,1,1,1,4,6,9,13,48]
beta_params=[(1,1),(0.5,0.5),(20,20)]
dist=st.beta
x=np.linspace(0,1,100)
for idx,N in enumerate(trials):
    if idx==0:
        plt.subplot(4,3,2)
    else:
        plt.subplot(4,3,idx+3)
    y=data[idx]
    for (a_prior,b_prior),c in zip(beta_params,('b','r','g')):
        p_theta_given_y=dist.pdf(x,a_prior+y,b_prior+N-y)
        plt.plot(x,p_theta_given_y,color=c,alpha=0.6)
    plt.axvline(theta_real,ymax=0.3,color='k')
    plt.plot(0,0,label="{:d} experiments\n{:d} heads".format(N,y),alpha=0)
    plt.xlim(0,1)
    plt.ylim(0,12)
    plt.xlabel(r"$\theta$")
    plt.legend()
    plt.gca().axes.get_yaxis().set_visible(False)
plt.tight_layout()
plt.savefig('B04958_01_05.png',dpi=300,figsize=(5.5,5.5))