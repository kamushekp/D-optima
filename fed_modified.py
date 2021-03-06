import numpy as np
from modifiedM import M_fed_style 
from scipy.optimize import minimize_scalar
from kernel import kernel as K

presition=1e-6
def del_repeated(des,weits):
    points=[]    
    weights=[]
    thing_was_count=set()
    
    des=list(enumerate(des))
    for elem in des:
        if elem[0] not in thing_was_count:
            rep=filter(lambda x:abs(x[1]-elem[1])<1e-2,des)    
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
    weits=[(0.5)/len(x0)]*len(x0)#weights of points in x0
    right=[0.58]
    i=0
    err=1
    alfa=100
    x=[0]*int((p+1)/2)
    nfev=0
    while i<10:

        i+=1
        m=M_fed_style(purpose,x0,kernel,p,h,flag,weits)
        D=np.linalg.inv(m)
        #strt=h*np.random.random_sample()+purpose

        f=minimize_scalar(minimax, tol=1e-3)
        '''alfa=-f.fun-p-1
        alfa=alfa/((alfa+p)*(p+1))'''
        alfa=1/(1+i)
        weits=list(map(lambda w:w*(1-alfa),weits))
        weits.append(alfa/2)
        x0.append(float(f.x))
        x0,weits=del_repeated(x0,weits)
        print(x0)
        '''
        print(alfa)
        answer=zip(x0,weits)
        answer=sorted(answer,key=lambda x:x[1])[::-1]
        x,y=zip(*answer[:int((p+1)/2):])
        x=sorted(list(map(lambda x:round(x,2),x)))
        print("{0},     {1}".format(i,x))      
        err=sum(list([(b-y)**2 for b,y in zip(right,x)]))
    print(nfev)'''

import time
nit=1
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
    def __exit__(self, type, value, traceback):
        print ("Elapsed time: {:.3f} sec".format(time.time()/nit - self._startTime/nit))
with Profiler():
    for i in range(nit):    
        alg(0,[0.1,0.5,0.7],'unif',5,1)