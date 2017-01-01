from modifiedM import M
from scipy.optimize import minimize
import numpy as np
def find_best_design(purpose,x0,p,h,kernel,symm):
    """Availble kernels: 'gauss','epanech','unif'.
    Initial design x0 should be writen as [x1,x2..]
    where {x1,x2,...} have symmetrical pairs on the
    other side of purpose point.
    symm-flag that equal 1 when design has= odd number of points.
    remember, that symm=1 add one more point to design"""
    '''if len(x0)*2<p+1:
        raise NameError('Not enought dots')
    '''
    def count_finite_det(design):
        res=0
        for point in purpose:
            res+=np.linalg.det(M(point,design,kernel,p,h,symm))
        return -res
    
    res=minimize(count_finite_det,x0,method='Nelder-Mead',\
    tol=1e-7,options={'maxiter': 1e+8, 'maxfev': 1e+8})
    
    from scipy.optimize import differential_evolution
    bounds = [(-2,2)for i in range(len(x0))]
    res1 = differential_evolution(count_finite_det, bounds)    
    res.fun/=len(res.x)
    res1.fun/=len(res1.x)
    print('evo')
    print (res1)

    print('NelMead')
    print (res)
            
find_best_design(purpose=[0],x0=[0.29, 0.5, 0.3,0.5,0.99],p=10,h=1,kernel='unif',symm=1)
a=np.linalg.det(M(0,[0.29, 0.5, 0.94,0.78,0.99],'unif',10,1,1))
print(a)

