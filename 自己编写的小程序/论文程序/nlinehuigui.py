# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:29:34 2018

@author: liyang
"""

import numpy as np  # 引入numpy
np.random.seed(314)
N=100
alpha_real=2.5
beta_real=[0.9,1.5]
eps_real=np.random.normal(0,0.5,size=N)
X=np.array([np.random.normal(i,j,N) for i,j in zip([10,2],[1,1.5])])
X_mean=X.mean(axis=1,keepdims=True)
X_centered=X-X_mean
y=alpha_real+np.dot(beta_real,X)+eps_real

import matplotlib.pyplot as plt
def scatter_plot(x,y):
    plt.figure(figsize=(10,10))
    for idx,x_i in enumerate(x):
        plt.subplot(2,2,idx+1)
        plt.scatter(x_i,y)
        plt.xlabel('$x_{}$'.format(idx),fontsize=16)
        plt.ylabel('$y$',rotation=0,fontsize=16)
    plt.subplot(2,2,idx+2)
    plt.scatter(x[0],x[1])
    plt.xlabel('$x_{}$'.format(idx-1),fontsize=16)
    plt.ylabel('$x_{}$'.format(idx),rotation=0,fontsize=16)
scatter_plot(X_centered,y)