import numpy as np
from kernel import kernel as K
import matplotlib.pyplot as pl
from scipy.optimize import minimize

def single(design,point,p,bandwidth):
    '''best single design for point'''
    n=len(design)
    w=[K((design[i]-point)/bandwidth,mode='gauss')/bandwidth for i in range(n)]
    W=np.diag(w)
    
    X=np.empty((n,p+1))
    for i in range(n):
        for j in range(p+1):
            X[i,j]=(design[i]-point)**j
            
    XT=X.transpose()    
    Fish=np.dot(XT,W)
    res=np.dot(Fish,X)

    return np.linalg.det(res)
    
def find_best(p,purpose,bandwidth,one_side_size_of_design):
    
    def finite(design):
        res=0
        for point in purpose:
            res+=single(design,point,p,bandwidth)
        return -res

    def find_finite(func,x0):
        res=minimize(func,x0,method='Nelder-Mead',tol=1e-10,\
        options={'maxiter': 1e+4, 'maxfev': 1e+4})
        return res
       

    
    #plots(finite)
    plan=[np.mean(purpose)for i in range(one_side_size_of_design)]*2
    plan=[0,0.5,0.5,0,3,1,2,4]

    result=find_finite(finite,plan)
    if result.success==False:
        print("ERROR")
    res=result.x
    print(result)
    fun=result.fun
    res.sort()
    return res,'\nfunction={}'.format(-fun)

def dec_s(design):
    p=1
    point=0
    bandwidth=1
    return -single(design,point,p,bandwidth)
    
x0=[3]*4
if __name__=='__main__':

    #print(minimize(dec_s,x0,method='Nelder-Mead',tol=1e-10))    
    print(find_best(p=1,purpose=[0,0.5],bandwidth=0.75,one_side_size_of_design=1))