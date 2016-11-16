import numpy as np
from kernel import kernel as K



def get_f(purpose,x,p):
    return np.matrix([(x-purpose)**(j) for j in range(p+1)]).T


def M(purpose,design,kernel,p,h):
    n=len(design)   
    M=np.zeros((p+1,p+1))
    Kui=[1/len(design)*K((design[i]-purpose),mode=kernel)/h for i in range (n)]
    
    for i in range(n):
        f_x=get_f(purpose,design[i],p)
        M+=Kui[i]*np.dot(f_x,f_x.T)
    return M

def newdx(purpose,dot,kernel,p,h):
    """count M for only one dot in design"""
    M=np.zeros((p+1,p+1))
    f_x=get_f(purpose,dot,p)
    Kui=K((dot-purpose),mode=kernel)/h
    M+=Kui*np.dot(f_x,f_x.T)
    print(M)
    D=np.linalg.inv(M)
    res=np.dot(f_x.T,D)
    res=np.dot(res,f_x)
    return res