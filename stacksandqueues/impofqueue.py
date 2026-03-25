class queues:
    def __init__(self,size):
        self.q=[0]*size
        self.front=-1
        self.end=-1
        self.cursize=0
        self.size=size

    def push(self,data):
        if self.cursize==self.size:
            print("queue overflow")
        elif self.cursize==0:
            self.front=0
            self.end=0
        else:
            self.end=(self.end+1)%self.size
        self.q[self.end]=data
        self.cursize+=1
    
    def pop(self):
        if self.cursize==0:
            print("queue underflow")
        elif self.cursize==1:
            self.front=self.end=-1
        else:
            self.front=(self.front+1)%self.size
        el=self.q[self.front]
        self.cursize-=1
        return el
        
    def top(self):
        if self.cursize==0:
            print("queue underflow")
        else:
            return self.q[self.front]
        
    def sizeofst(self):
        return self.cursize
        
    def printst(self):
        for i in range(self.cursize):
            print(self.q[i],end=" ")
        print()

s=queues(5)
s.push(10)
s.push(20)  
s.push(30)
s.push(40)
s.push(50)   
print("size:",s.sizeofst()) 
s.printst()          
print(s.pop())
print("top:",s.top())
print(s.pop())
print("top:",s.top())
print(s.pop())  
print("size:",s.sizeofst())
