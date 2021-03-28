import numpy as np
from matplotlib.pyplot import plot,savefig
import matplotlib.pyplot  as plt
import math
p0  =10**3
p   =7.85*(10**3)
n   =10**(-3)
R   =0.01
m   = (4/3) * p * math.pi * R**3  #质量
g   = 9.8
k   = 6*math.pi*n*R   #f=kv
F   =   (4/3) * math.pi * R**3 * p0 * g   #浮力
h   = 0.5              #时间间隔
step=5000
v=np.zeros((1,step+1))
x=np.zeros((1,step+1))
t=np.zeros((1,step+1))
y=np.zeros((1,step+1))
D=np.zeros((1,step+1))
v[0,0]=0.0
x[0,0]=0.0
y[0,0]=0.0
D[0,0]=0.0
for i in range(1,step):
    v[0,i+1]  = v[0,i] + h*(g- F/m - (k*v[0,i])/m)
    t[0,i]    = h*i
for i in range(1,step):
    x[0,i+1]  =x[0,i]+v[0,i]*h+(1/2)*(9.8-F/m-(k*v[0,i])/m)*h*h
for i in range(1,step):
    y= (m*g*t - F*t) / (m + k*t)
for i in range(1,step):
    D[0,i] = v[0,i]-y[0,i]
plt.xlim(0,1000)
plt.ylim(0,2000)
plt.xlabel("t")
plt.ylabel("v")
plt.plot(t,v,'.k')
plt.plot(t,y,'.b')
plt.plot(t,D,'.r')
plt.show()

