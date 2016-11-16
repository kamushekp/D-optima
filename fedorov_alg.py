from kernel import kernel as K
from scipy.optimize import minimize
import numpy as np
from Design import Design
from d_x import d_x as dx
from M import M

def round_design(design,prec):
    design=list(map(lambda x:float(round(x,prec)),design))
    return design
    

def fed_alg(purpose,x0_design,kernel,p,h):
    design=Design(x0_design)
    
    def minimax(dot):
        d=dx(purpose,design,dot,p,h,kernel)
        d*=np.linalg.det(M(purpose,design,kernel,p,h))
        w=K((dot-purpose)/h,mode=kernel)/h
        return -w
    f=minimize(minimax,purpose,method='Nelder-Mead',\
    tol=1e-6,options={'maxiter': 1e+8, 'maxfev': 1e+8})
    print(f)
    '''написать функцию вычисления М матрицы для Федорова'''
fed_alg(0,[-1,1],'unif',1,1)