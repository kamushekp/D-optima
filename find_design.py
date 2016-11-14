from scipy.optimize import minimize
import numpy as np
from M import M
def find_best_design(purpose,x0,p,h,kernel):
    """Availble kernels: 'gauss','epanech','unif'"""
    def count_finite_det(design):
        res=0
        for point in purpose:
            res+=np.linalg.det(M(point,design,kernel,p,h))
        return -res
    
    res=minimize(count_finite_det,x0,method='Nelder-Mead',\
    tol=1e-6,options={'maxiter': 1e+8, 'maxfev': 1e+8})
    
    from scipy.optimize import differential_evolution
    bounds = [(-10,10)for i in range(len(x0))]
    res1 = differential_evolution(count_finite_det, bounds)    
    if res1.fun<res.fun:
        print('evo')
        return res1
    else:
        print('NelMead')
        return res
            