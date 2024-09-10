#funciona!!!!
import numpy as np
import matplotlib.pyplot as plt
from itertools import product 


def mbrot (c,cantiter):
    z=list(range(cantiter+1))
    z[0]=c
    for n in range(1,cantiter+1):
        z[n]=z[n-1]**2+c
        if abs(z[n])>2:
          break  
    return n



ultiter=100 #maxima iteracion
dx=0.01 #variacion entre un numero y el siguiente

xmin=-2.2
xmax=1.1
rax=np.arange(xmin,xmax,dx) #reales
nx=len(rax)

ymin=-1.5
ymax=1.5
ray=np.arange(ymin,ymax,dx)
ny=len(ray)
ray=ray[::-1] #imaginarios,asi se hace para girar una lista
nums= list(product(ray,rax))
nc=len(nums) #cantidad de numeros complejos a evaluar

c=np.zeros((nc),dtype=complex)
for i in range(nc):
    c[i]=complex(nums[i][1],nums[i][0]) #queda lista el array de complejos
    
ni=np.zeros(nc)
for k in range(nc):
    ni[k]=mbrot(c[k],ultiter)
    
ni=ni.reshape(ny,nx) #este es el array de dimensiones nx,ny, que hace la grafica


fig=plt.figure('''figsize=(13,10),dpi=1500''')
ax = fig.add_axes([0.0 , 0.0 , 1.0 , 1.0],frameon=False) #para quitar el cuadro que la encierra



im=plt.imshow(ni,cmap=plt.cm.autumn,interpolation='bicubic',vmin=0,vmax=ultiter,extent=[xmin,xmax,ymin,ymax])
ax.set_xticks([])
ax.set_yticks([]) #para quitar los valores de los ejes, es decir,los numeros


plt.show()

