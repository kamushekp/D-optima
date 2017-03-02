
kern='epanech'
p=1
h = 2.1
purpose=[1,2,3]
x0=[0.8,1.2,2.2,1.8,2.8,3.2]
from find_design import find_best_design as fbd
resNM,resDIF=fbd(purpose,x0,p,h,kern)


from M import M
import numpy as np

print('kernel = {0}, p = {1}, h = {2}\n'.format(kern,p,h))

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

'''


def modif_M(point,design):
    fish=M(point,design,kern,p,h)
    M12=fish[:1,1:]
    M22inv=np.linalg.inv(fish[1:,1:])
    temp=np.dot(M12,M22inv)
    temp=np.dot(temp,M12.T)
    res=float(fish[:1,:1]-temp)
    return res
        
des=[-0.00937618,  0.00937618,  0.3987743 ,  0.6012257]
result=modif_M(0,des)+modif_M(0.5,des)


print('\n\nDiff. evolution')
a=M(1,resDIF.x,kern,p,h)
b=M(2,resDIF.x,kern,p,h)
print(np.linalg.det(a)+np.linalg.det(b))
print('first {}'.format(np.linalg.det(a)))
print('second {}'.format(np.linalg.det(b)))
print(list(resDIF.x))
'''