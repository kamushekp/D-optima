from scipy.optimize import minimize
import numpy as np
from M import M as FishM
def find_best_design(purpose,x0,p,h,kernel):
    """Availble kernels: 'gauss','epanech','unif'"""
    def count_finite_det(design):
        res=0
        old=0
        for point in purpose:
            if old==0:
                '''old version'''
                temp = np.linalg.det(FishM(point,design,kernel,p,h))
                if temp == 0:
                    pass
                else:
                    res+=temp
            else:
                '''new version'''
                try:
                    M=FishM(point,design,kernel,p,h)
                    M12=M[:1,1:]
                    M22inv=np.linalg.inv(M[1:,1:])
                    temp=np.dot(M12,M22inv)
                    temp=np.dot(temp,M12.T)
                    res+=float(M[:1,:1]-temp)
                except np.linalg.LinAlgError:
                    res=0
               
        return -res
    
    res=minimize(count_finite_det,x0,method='Nelder-Mead',\
    tol=1e-7,options={'maxiter': 1e+8, 'maxfev': 1e+8})
    
    print('NelMead')
    #print (res)
            
    from scipy.optimize import differential_evolution
    bounds = [(purpose[0]-h,purpose[len(purpose)-1]+h)for i in range(len(x0))]
    res1 = differential_evolution(count_finite_det, bounds)    
    print('evo')
    #print (res1)

    return res,res1
