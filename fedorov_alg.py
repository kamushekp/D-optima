from kernel import kernel as K
from scipy.optimize import minimize
import numpy as np
from Design import Design
from dx_norm import d_x as dx
from M import M

def round_design(design,prec):
    design=list(map(lambda x:float(round(x,prec)),design))
    return design
    

def fed_alg(purpose,x0_design,kernel,p,h):
    design=Design(x0_design)
    
    def minimax(dot):
        dot=float(dot)
        d=dx(purpose,design,dot,p,h,kernel)
        w=K((dot-purpose)/h,mode=kernel)/h
        return float(-w*d)

    sig=1
    for i in  range(2000):  
        #a=np.random.rand()*(-1)**np.random.randint(1,3)
        
        f=minimize(minimax,a,method='Nelder-Mead',\
        tol=1e-6,options={'maxiter': 1e+8, 'maxfev': 1e+8})
        sig=-f.fun-p-1
        alfa=sig/(sig+p)/(p+1) 
        print(alfa)
        design.anpcow(float(f.x),alfa)
        design.set_control(2,0.01)
        design.find_nonc(0.01)
        print ('iteration')
    print(design.points)
    print(design.weights)
    design.set_control(2,0.01)
    design.set_control(2,0.01)
    design.find_nonc(0.01)
    p=list(zip(design.points,design.weights))
    def s(elem):
        return elem[1]
    
    p=sorted(p,key=s)
    print(p)
 
fed_alg(0,[0,0.1,-0.1,0.4,0.5,-0.5],'epanech',5,1)