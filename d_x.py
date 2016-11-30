import numpy as np
from M import M
def d_x(purpose,design,dot,p,h,kernel):
    m=M(purpose,design,kernel,p,h)
    D=np.linalg.inv(m)
    f_x=np.matrix([(dot-purpose)**(j) for j in range(p+1)]).T
    d_x=np.dot(f_x.T,D)
    d_x=np.dot(d_x,f_x)
    return d_x