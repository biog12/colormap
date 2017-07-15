# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:05:17 2017

@author: vigh
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as mtp

def map_x(x,y,z,vmin,vmax,step):
    vmin=vmin
    vmax=vmax
    step=step
    cmap = plt.cm.rainbow
    cmap.set_over('k')
    cmap.set_under('r')
    bounds = np.arange(vmin,vmax+step,step)
    plt.scatter(x,y,c=z,cmap = cmap,s=100,marker=',',vmin=vmin,vmax=vmax)
    plt.colorbar(extend='both',ticks=bounds)
    

def map_a(path):
    t=pd.read_csv(path,skiprows=11)
    x = t['XADR']
    y = t['YADR']
    vf=t['VF1']
    iv=t['IV']
    wld=t['WD']
    ir=t['IR'] 
    plt.figure(figsize=(10,10))
    mtp.subplot(2,2,1)
    map_x(x,y,vf,2,3,0.1)
    mtp.title("VF")
    mtp.subplot(2,2,2)
    map_x(x,y,iv,500,550,5)
    mtp.title("IV")
    mtp.subplot(2,2,3)
    map_x(x,y,wld,450,465,1)
    mtp.title("WLD")
    mtp.subplot(2,2,4)
    map_x(x,y,ir,0,1,0.5)
    mtp.title("IR")
    plt.savefig(os.path.splitext(list[i])[0]+".png")
 
rootdir = 'D:\\123'
list = os.listdir(rootdir)
for i in range(0,len(list)):
      path = os.path.join(rootdir,list[i])
      map_a(path) 
      
      
      