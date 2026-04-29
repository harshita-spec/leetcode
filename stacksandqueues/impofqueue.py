class queues:
    def __init__(self,size):
        self.q=[0]*size
        self.front=-1
        self.end=-1
        self.cursize=0
        self.size=size
    
    #append a element at the end of the queue and increase the size of queue by 1
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
    
    #remove the front element of the queue and decrease the size of queue by 1
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
        
    #return the front element of the queue without removing it
    def top(self):
        if self.cursize==0:
            print("queue underflow")
        else:
            return self.q[self.front]
        
    #return the current size of the queue
    def sizeofst(self):
        return self.cursize

    #print the elements of the queue from front to end 
    def printst(self):
        for i in range(self.cursize):
            print(self.q[i],end=" ")
        print()

Q=queues(5)
Q.push(10)
Q.push(20)  
Q.push(30)
Q.push(40)
Q.push(60)   
print("size:",Q.sizeofst()) 
Q.printst()          
print(Q.pop())
print("top:",Q.top())
print(Q.pop())
print("top:",Q.top())
print(Q.pop())  
print("size:",Q.sizeofst())
