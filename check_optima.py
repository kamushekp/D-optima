import numpy as np
from kernel import kernel as K
from d_x import d_x
def check_all(purpose,design,p,h,kernel):
    
    def check_one(purpose,design,dot,p,h,kernel):
        d=d_x(purpose,design,dot,p,h,kernel)
        weight=K((dot-purpose)/h,mode=kernel)/h
        return float(d*weight),float(d*weight)
    
    res=[check_one(purpose,design,dot,p,h,kernel)[0]for dot in design]
    
    res1=[len(design)*check_one(purpose,design,dot,p,h,kernel)[1]for dot in design]
        
    
    return res
    
cond2=check_all(purpose=0,\
design=[-2.33441426,  0, -0.1,  0.74196372],\
p=3,h=1,kernel='gauss')

print(cond2)

x_axe=[0+i*0.005 for i in range(200)]
y_axe=[0.5*d_x(purpose=0,design=[-1 ,  x_axe[i]],\
dot=x_axe[i],p=1,h=1,kernel='unif')for i in range(200)]
y_axe=list(map(lambda y:float(y),y_axe))

import matplotlib.pyplot as plt
plt.plot(x_axe,y_axe)
plt.show()
