import numpy as np
from kernel import kernel as K



def get_f(purpose,x,p):
    return np.matrix([(x-purpose)**(j) for j in range(p+1)]).T


def M(purpose,design,kernel,p,h):
    n=len(design)   
    M=np.zeros((p+1,p+1))
    Kui=[K((design[i]-purpose)/h,mode=kernel)/h for i in range (n)]
    
    for i in range(n):
        f_x=get_f(purpose,design[i],p)
        M+=Kui[i]*np.dot(f_x,f_x.T)/len(design)
    return M

def plot_M(purpose,kernel,p,h):
    x=np.arange(-2,2,0.00005)
    y=[]
    for i in range(len(x)):
        res=M(purpose,[-1,x[i]],kernel,p,h)
        res=np.linalg.det(res)
        y.append(res)
        from matplotlib import pyplot as pl
    print(len(x))
    print(len(y))
    pl.plot(x,y,'.')
    pl.show()

#plot_M(purpose=0,kernel='gauss',p=1,h=1)
#print(M(-1,[-10,-6,4,8,-4,-2,0,2,-1],'epanech',3,10))
        
