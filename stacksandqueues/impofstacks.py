class stacks:
    def __init__(self,size):
        self.st=[0]*size
        self.top=-1
        self.size=size

    def push(self,data):
        if self.top==self.size-1:
            print("stack overflow")
        else:
            self.top+=1
            self.st[self.top]=data
    
    def pop(self):
        if self.top==-1:
            print("stack underflow")
        else:
            data=self.st[self.top]
            self.top-=1
            return data
        
s=stacks(5)
s.push(10)
s.push(20)  
s.push(30)
s.push(40)
s.push(50)              
print(s.pop())
print(s.pop())
print(s.pop())  
