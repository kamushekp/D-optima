from modifiedM import M
from scipy.optimize import minimize
import numpy as np
def find_best_design(purpose,x0,p,h,kernel):
    """Availble kernels: 'gauss','epanech','unif'.
    Initial design x0 should be writen as [x1,x2..]
    where {x1,x2,...} have symmetrical pairs on the
    other side of purpose point.
    symm-flag that equal 1 when design has= odd number of points.
    remember, that symm=1 add one more point to design"""

    symm=[0,1][p%2==0]
    def count_finite_det(design):
        res=0
        for point in purpose:
            res+=np.linalg.det(M(point,design,kernel,p,h,symm))
        return -res
    
    if method=='NM':  
        
        res=minimize(count_finite_det,x0,method='Nelder-Mead',\
        tol=1e-3,options={'maxiter': 1e+8, 'maxfev': 1e+8})

    else:        
        from scipy.optimize import differential_evolution
        bounds = [(-1,1)for i in range(len(x0))]
        res = differential_evolution(count_finite_det, bounds)    

    #print('NelMead')
    #print (res)
    res.nfev+=1
    return res
            
import time
nit=10
method='NM'
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
    def __exit__(self, type, value, traceback):
        print ("Elapsed time: {:.3f} sec".format(time.time()/nit - self._startTime/nit))
with Profiler() as p:
    for i in range(nit):    
        a=find_best_design(purpose=[0],x0=[0.7,0.3],p=4 ,h=1,kernel='gauss')
