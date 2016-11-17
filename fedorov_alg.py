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
    sig_last=42
    sig=1
    for i in  range(10):    
        f=minimize(minimax,purpose,method='Nelder-Mead',\
        tol=1e-6,options={'maxiter': 1e+8, 'maxfev': 1e+8})
        sig=-f.fun-p-1
        alfa=sig/(sig+p)/(p+1)    
        design.anpcow(float(f.x),alfa)
        sig_last=sig
        print ('iteration')
    print(design.points)
    print(sum(design.weights))
    design.set_control(2,0.01)
    print(design.points)
    print(design.weights)
    print(sum(design.weights))
    '''написать функцию вычисления М матрицы для Федорова'''
fed_alg(0,[-0,0.5],'epanech',1,1)