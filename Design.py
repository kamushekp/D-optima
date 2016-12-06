class Design:
    def __init__(self,x0):
        self.len=len(x0)        
        self.points=x0
        self.weights=[1/len(x0)for i in range(len(x0))]
    def anpcow(self,x,alpha):
        '''add_new_point_change_other_weights'''
        self.weights=list(map(lambda w:w*(1-alpha),self.weights))
        self.points.append(x)
        self.weights.append(alpha)
        self.len+=1
    def get_len(self):
        return len(self.points)
    def delete_elem(self,index):
        wi=self.weights[index]        
        self.weights.pop(index)
        self.points.pop(index)
        self.len=self.len-1
        for i in range(self.len):
            self.weights[i]+=wi/self.len
      
    def find_nonc(self,percent):
        '''finding and delete points with small weights; doing redistrib.'''
        cpyw=[]        
        cpyp=[]  
        for i in range(self.len):
            if self.weights[i]>percent:
                cpyw.append(self.weights[i])                
                cpyp.append(self.points[i])
        for i in range(self.len):
            if self.weights[i]<percent:
                cpyw=list(map(lambda x:x+self.weights[i]/len(cpyw),cpyw))
        self.weights=cpyw
        self.points=cpyp
        self.len=len(cpyp)
            
    def set_control(self,length,percent):
        '''if |x1-x2|<length*percent,x2 become x1 and x2 s weight doubled'''
        #self.points=list(map(lambda x:round(x,5),self.points))        
        nonused=set()        
        extra=[]
        crit=length*percent
        
        for i in range(self.len):
            extra_i=[]
            obj=self.points[i]
            
            a=[]
            for elem in extra:
                a.extend(elem)
                
            #print(a)
            if i not in a:
                for j in range(i+1,self.len):
                    if abs(self.points[j]-obj)<crit:
                        if j not in nonused:
                            extra_i.append(j)
                            nonused.add(j)
            extra.append(extra_i)
            
            
        what_to_del=[]
        b=[]
        #print(extra)

        
        for i in range (len(extra)):
            if len(extra[i])!=0:
                el_p=[self.points[elem] for elem in extra[i]]
                el_w=[self.weights[elem] for elem in extra[i]]
                b.append(sum(el_w))
                l=len(extra[i])+1
                self.points[i]/=l
                self.points[i]+=sum(el_p)/l
                self.weights[i]+=sum(el_w)
                what_to_del.extend(extra[i])
                

        for elem in sorted(what_to_del,reverse=True):
            self.weights.pop(elem)
            self.points.pop(elem)
            self.len-=1

            