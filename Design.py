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
        for i in range(self.len):
            if self.weights[i]<percent:
                self.delete_elem(i)
            
    def set_control(self,length,percent):
        '''if |x1-x2|<length*percent,x2 become x1 and x2 s weight doubled'''        
        nonused=set()        
        extra=[]
        crit=length*percent
        for i in range(self.len):
            extra_i=[]
            obj=self.points[i]
            for j in range(i+1,self.len):
                if abs(self.points[j]-obj)<crit:
                    if j not in nonused:
                        extra_i.append(j)
                        nonused.add(j)
            extra.append(extra_i)
        what_to_del=[]
        ba=0
        for i in range (len(extra)):
            if len(extra[i])!=0:
                el_p=[self.points[elem] for elem in extra[i]]
                el_w=[self.weights[elem] for elem in extra[i]]
                l=len(extra[i])+1
                self.points[i]/=l
                self.points[i]+=sum(el_p)/l
                self.weights[i]+=sum(el_w)
                print(extra[i])
                for j in range(len(extra[i])):
                    print("{0} {1}".format(self.points[extra[i][j]],self.weights[extra[i][j]]))
                print('ens')
                what_to_del.extend(extra[i])
                
        print(what_to_del)
        a=[]
        for elem in sorted(what_to_del,reverse=True):
            print(elem)
            print('del={0} {1} {2}\n'.format(elem,self.points[elem],self.weights[elem]))
            a.append(self.weights[elem])
            ba-=self.weights[elem]
            del(self.weights[elem])
            self.points.pop(elem)
            print(self.weights)
            self.len-=1

            


