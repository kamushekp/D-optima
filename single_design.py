import numpy as np
from kernel import kernel as K
from scipy.optimize import minimize
sf=0
def single_det(design,point):
    n=len(design)
    Ui=[[(design[i]-point)**(j) for j in range(p*2+1)]for i in range(n)]

    '''   [[первая точка плана],[вторая точка],[третья точка],...]    '''
    k_Ui=[K((design[i]-point)/h,mode='unif')/h for i in range (n)]

    def count_sum(k):
        sum=0
        for b in range(n):
            sum+=Ui[b][k]*k_Ui[b]
        return sum
    
    S=[count_sum(k)for k in range(p*2+1)]

    M=np.empty((p+1,p+1),dtype=np.float64)
    
    for i in range(p+1):
        for j in range(p+1):
            M[i,j]=S[i+j]
    global sf
    print(sf)
    sf+=1
    return(np.linalg.det(M))


def find_best_design(purpose):
    
    def finite_det(design):
        res=0
        for point in purpose:
            res+=np.log(single_det(design,point))
        return -res
        
    def find_design(func,x0):
        res=minimize(func,x0,method='Nelder-Mead',tol=1e-8,\
        options={'maxiter': 1e+6, 'maxfev': 1e+6})
        print(res)
        return res
    
    step=2*h/(p)
    x0=[-h+1e-14+step*i for i in range(p+1)]
    print(x0)
    result=find_design(finite_det,x0)
    return result

def count_finite_det(purpose,design):
        res=0
        for point in purpose:
            res+=single_det(design,point)
        return res
#(count_finite_det([0],plan))
#print(count_finite_det([0],find_best_design([0]).x))
p=10
h=1.4

res=find_best_design([0]).x
for i in range(len(res)):
    res[i]=round(res[i],2)
res.sort()
y=[0]*len(res)
import matplotlib.pyplot as plt

plt.plot(res,y,'.',ms=10)
plt.grid(True)
plt.axis([-3,3,-0.1,0.1])
font = {'family': 'Verdana',
        'weight': 'normal'}
plt.rc('font', **font)
plt.xlabel('p={0}, ядро {1},план: {2}'.format(p,u'равномерное',res))
plt.show()









