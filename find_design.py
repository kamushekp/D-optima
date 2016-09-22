import numpy as np
from kernel import kernel as K
import matplotlib.pyplot as pl
def main():
    p=1
    purpose=[0,12,3]
    bandwidth=2
    def finite(design):

        def single(design,point):
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
            return -np.linalg.det(res)
            
        res=0
        for point in purpose:
            res+=single(design,point)
        return res
        
        
        
    
    from scipy.optimize import minimize_scalar
    from scipy.optimize import minimize


       

        

    def find_single(func,x0):
        res=minimize(func,x0,method='Nelder-Mead',tol=1e-6)
        return res
       
    def plots():
        x=[i*0.0001 for i in range(100000)]
        y=[single([x[i]]) for i in range ( len(x))]
        pl.plot(x,y,'ro',linewidth=1)
        print(x)
        print(y)
        pl.show()
    

    print(find_single(finite,[0.5,-0.5]))

    
main()