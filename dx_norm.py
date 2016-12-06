import numpy as np
from M_norm import M
def d_x(purpose,design,dot,p,h,kernel):
    m=M(purpose,design.points,design.weights,kernel,p,h)
    D=np.linalg.inv(m)
    f_x=np.matrix([(dot-purpose)**(j) for j in range(p+1)]).T
    d_x=np.dot(f_x.T,D)
    d_x=np.dot(d_x,f_x)
    return d_x
class Temp_design:
    def __init__(self,x0):
        self.points=x0
        self.weights=[1/len(x0)for i in range(len(x0))]


def plot_wd(k):
    from kernel import kernel as K
    x=np.arange(-1,1,0.0005)
    y=[]
    j=-1
    for i in range(len(x)):
        j+=1
        des=Temp_design([1,0,x[j]])
        try:
            numb=float(d_x(purpose=0,design=des,dot=x[j]\
            ,p=2,h=1,kernel=k))

            y.append(numb)
        except np.linalg.LinAlgError:
            x=np.delete(x,j)
            j-=1

    from matplotlib import pyplot as pl
    pl.plot(x,y,'.')
    pl.show()
plot_wd('unif')
