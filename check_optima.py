import numpy as np
from kernel import kernel as K
from M import M
'''def check_all(purpose,design,p,h,kernel):
    
    def check_one(purpose,design,dot,p,h,kernel):
        d=d_x(purpose,design,dot,p,h,kernel)
        weight=K((dot-purpose)/h,mode=kernel)/h
        return float(d*weight),float(d*weight)
    
    res=[check_one(purpose,design,dot,p,h,kernel)[0]for dot in design]
    
    res1=[len(design)*check_one(purpose,design,dot,p,h,kernel)[1]for dot in design]
        
    
    return res
    
#cond2=check_all(purpose=0,design=[-1,  0, 1],p=2,h=1,kernel='gauss')

#print(cond2)
'''


def d_x(purpose,design,dot,p,h,kernel):
   
    m=M(purpose,design,kernel,p,h)
    D=np.linalg.inv(m)
    f_x=np.matrix([(dot-purpose)**(j) for j in range(p+1)]).T
    d_x=np.dot(f_x.T,D)
    d_x=np.dot(d_x,f_x)
    d_x*=len(design)
    return float(d_x)

h=1  
kernl='unif'  
x_axe=np.linspace(-1,1,500)

y_axe=[K(x_axe[i]/h,mode=kernl)/h*d_x(purpose=0,design=[-0.999,0.8356540663993193, 0.5641572515850596,-0.564263395062234, 0.7821410588028485,0.2955600789475211,-0.29399672797215587,0.0005596857669483513,0.9376458913026472,-0.93614466888028,-0.7889649466036868,0.9999999983452569],\
dot=x_axe[i],p=10,h=h,kernel=kernl)for i in range(len(x_axe))]
y_axe=list(map(lambda y:float(y),y_axe))

import matplotlib.pyplot as plt
plt.plot(x_axe,y_axe,'.')
plt.show()
