import matplotlib.pyplot as plt
import numpy as np

R1=476.18
# R1=9000
R2=10000
A=R1/R2
B=2*R1*0.01
nV=10
R_0=50
L=0.22
C=5
y=[1]
y2=[0]
h=0.0001
def gInv(x): return A*x+B*np.sinh(x/nV)
def gInvDer(x): return A+(B/nV)*np.cosh(x/nV)
def gPrime(w):
    x=10
    for i in range(10):
        x=x-(gInv(x)-w)/gInvDer(x)
    return 1/gInvDer(x)
def g(w):
    x=10
    for i in range(10):
        x=x-(gInv(x)-w)/gInvDer(x)
    return x
xx=[]
gg=[]
for i in range(2000000):
    # xx.append(h*i)
    # gg.append(g(h*i))
    y.append(y[-1]+h*y2[-1])
    y2.append(y2[-1]+h*(-y[-1]/(L*C)-(1-gPrime(y[-1]))*R_0*y2[-1]/L))
# plt.plot(xx,gg)
# plt.plot(xx,xx)
plt.plot(y, y2)
# plt.axis([-1, 1, -1, 1])
