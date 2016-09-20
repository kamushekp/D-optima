from numpy import diag,empty,dot,transpose,linalg
from kernel import kernel as K
def main():
    p=1
    purpose=1
    bandwidth=1
    def determinant(ksi):
        n=len(ksi)
        nonlocal purpose
        nonlocal p
        nonlocal bandwidth
        w=[K((ksi[i]-purpose)/bandwidth)for i in range(n)]
        W=diag(w)
          
        X=empty((n,p+1))
        for i in range(n):
            for j in range(p+1):
                X[i,j]=(ksi[i]-purpose)**j
                
        Fish=dot(W,X)
        XT=X.transpose()
        Fish=dot(XT,Fish)
        return linalg.det(Fish)
    
    from scipy.optimize import minimize
    def find_single_D(func,x0):
        return minimize(func,x0,method='Nelder-Mead',tol=1e-10)
    
    d=find_single_D(determinant,(0,1))
    print(d)
main()