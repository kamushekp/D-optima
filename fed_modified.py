import numpy as np
from modifiedM import M_fed_style 
from scipy.optimize import minimize
from kernel import kernel as K

presition=1e-6
def del_repeated(des,weits):
    points=[]    
    weights=[]
    thing_was_count=set()
    
    des=list(enumerate(des))
    for elem in des:
        if elem[0] not in thing_was_count:
            rep=filter(lambda x:abs(x[1]-elem[1])<presition,des)    
            rep=list(rep)
            things=set([x[0]for x in rep])
            if not things&thing_was_count:
                value=sum([x[1]for x in rep])/len(rep)
                weight=sum([weits[i]for i,k in rep])
                points.append(value)
                weights.append(weight)
                thing_was_count.update(things)
    return points,weights
        
def alg(purpose,x0,kernel,p,h):
    def dx(dot):
        dot=float(dot)
        f_x=np.matrix([(dot-purpose)**(j) for j in range(p+1)]).T
        d_x=np.dot(f_x.T,D)
        d_x=np.dot(d_x,f_x)
        return d_x
        
    def minimax(dot):
        dot=float(dot)
        d=dx(dot)
        w=K((dot-purpose)/h,mode=kernel)/h
        return float(-w*d)
    
    
    
    flag=[0,1][p%2==0]

    weits=[0.5/len(x0)]*len(x0)#weights of points in x0
    for i in range(10):
        m=M_fed_style(purpose,x0,kernel,p,h,flag,weits)
        D=np.linalg.inv(m)
        minimax(-0.9999)
        strt=2*h*np.random.random_sample()+purpose-h
        f=minimize(minimax,strt,method='Nelder-Mead',\
        tol=presition,options={'maxiter': 1e+8, 'maxfev': 1e+8})
        alfa=-f.fun-p-1
        alfa=alfa/((alfa+p)*(p+1))
        
        weits=list(map(lambda w:w*(1-alfa),weits))
        weits.append(alfa/2)
        x0.append(float(f.x))
    x0,weits=del_repeated(x0,weits)      
        
    print(x0)
    print(sum(weits))


alg(0,[0.5,0.1],'unif',1,1)