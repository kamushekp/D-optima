import numpy as np
from kernel import kernel as K

def M(purpose,design,kernel,p,h,flag):
    '''flag shows if design odd(1) or it isnt(0)'''
    
    n=len(design)
    u=[[(point-purpose)**(2*j) for j in range(p*2)]for point in design]

    w1=[K((point-purpose)/h,mode=kernel)/h for point in design]
    
    def c_s(k):
        sum=0
        for b in range(n):
            sum+=u[b][k]*w1[b]
        sum*=2
        return sum        
    
    S=[c_s(k)for k in range(p*2)]
    M=np.empty((p+1,p+1),dtype=np.float64)
    
    from math import trunc
    for i in range(p+1):
        for j in range(p+1):
            if trunc((i+j)%2)==0:
                M[i,j]=S[int((i+j)/2)]
            else:
                M[i,j]=0
    
    '''contrib. of nonsymmetric point'''
    if flag==1:
        M[0,0]+=K(0.,mode=kernel)/h
       
    return M

def M_fed_style(purpose,design,kernel,p,h,flag,fed_w):
    '''
    flag shows if design odd(1) or it isnt(0)
    fed_w is array with weights of norming design (sum eq 1)    
    '''
    
    n=len(design)
    u=[[(point-purpose)**(2*j) for j in range(p*2)]for point in design]

    w1=[K((point-purpose)/h,mode=kernel)/h for point in design]
    for i in range(len(w1)):
        w1[i]*=fed_w[i]
    def c_s(k):
        sum=0
        for b in range(n):
            sum+=u[b][k]*w1[b]
        sum*=2
        return sum        
    
    S=[c_s(k)for k in range(p*2)]
    M=np.empty((p+1,p+1),dtype=np.float64)
    
    from math import trunc
    for i in range(p+1):
        for j in range(p+1):
            if trunc((i+j)%2)==0:
                M[i,j]=S[int((i+j)/2)]
            else:
                M[i,j]=0
    
    '''contrib. of nonsymmetric point'''
    if flag==1:
        M[0,0]+=K(0.,mode=kernel)/h
       
    return M