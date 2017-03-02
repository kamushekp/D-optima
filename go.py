

p=1
h = 3.0
purpose=[1,2,3]
x0=[0.8,1.2,2.2,1.8,2.8,3.2]
from find_design import find_best_design as fbd



from M import M
import numpy as np
def main():
    print('kernel = {0}, p = {1}, h = {2}\n'.format(kern,p,h))
    resNM,resDIF=fbd(purpose,x0,p,h,kern)
    print('\n\nNelder-Mead')
    
    res=0
    for i in range(len(purpose)):
        a=M(purpose[i],resNM.x,kern,p,h)
        print(np.linalg.det(a))
        res+=np.linalg.det(a)
    
    print(res)
    print(list(sorted(resNM.x)))
    
    print('\n\nDiff. evolution')
    res=0
    for i in range(len(purpose)):
        a=M(purpose[i],resDIF.x,kern,p,h)
        print(np.linalg.det(a))
        res+=np.linalg.det(a)
    
    print(res)
    print(list(sorted(resDIF.x)))


def get_graphics_of_parts():
    X_ = []
    Y_epan = []
    Y_gauss =  []  
    
    for step in np.linspace(0.4, 5, 25):
        kern='gauss'
        print(step)
        resNM, resDIF=fbd(purpose,x0,p,step,kern)
        dets = [np.linalg.det(M(purpose[i],resNM.x,kern,p,step)) for i in range(3)]
        Y_epan.append(max(dets) / sum(dets))
        
    for step in np.linspace(0.4, 5, 25):
        kern='epanech'
        print(step)
        resNM, resDIF=fbd(purpose,x0,p,step,kern)
        dets = [np.linalg.det(M(purpose[i],resDIF.x,kern,p,step)) for i in range(3)]
        Y_gauss.append(max(dets) / sum(dets))
        X_.append(step)
    print('\n\nGauss - {0}\n\nEpanech - {1}'.format(Y_gauss, Y_epan))


    import matplotlib.pyplot as plt
    
    plt.plot(X_, Y_epan, X_, Y_gauss)
    plt.show()
get_graphics_of_parts()



