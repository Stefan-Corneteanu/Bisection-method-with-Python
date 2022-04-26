import numpy as np
import matplotlib.pyplot as plt

def myf(x):
    return x**2-2

a=0
b=3
step = 0.001
x = np.arange(a,b+step,step)
y = myf(x)

plt.close('all')
plt.plot(x,y)
plt.plot(x,np.zeros(len(x)))
plt.plot(a,myf(a),'g*')
plt.plot(b,myf(b),'g*')
plt.text(a, myf(a)+0.1, 'a')
plt.text(b, myf(b)+0.1, 'b')
plt.grid('on')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Bisection method")

err = 1

m = (a+b)/2
fm = myf(m)
if (fm>0):
    b=m
else:
    a=m

while err>0.01:
    plt.plot(m,fm,'r*')
    mold=m
    m = (a+b)/2
    fm = myf(m)
    if (fm>0):
        b=m
    else:
        a=m
    err = abs(m-mold)/m*100
     
plt.plot(m,fm,'m*')
    
