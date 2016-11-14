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
    def get_len(self):
        return len(self.points)