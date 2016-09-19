from numpy import diag,empty,dot,transpose,linalg
from kernel import kernel as K
def determinant(purpose,p,bandwidth,*ksi):
    n=len(ksi)
    
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