class stacks:
    def __init__(self,size):
        self.st=[0]*size
        self.top=-1
        self.size=size
    
    #append a element at the top of the stack and increase the size of stack by 1
    def push(self,data):
        if self.top==self.size-1:
            print("stack overflow")
        else:
            self.top+=1
            self.st[self.top]=data
    
    #remove the top element of the stack and decrease the size of stack by 1
    def pop(self):
        if self.top==-1:
            print("stack underflow")
        else:
            data=self.st[self.top]
            self.top-=1
            return data

    #return the top element of the stack without removing it 
    def peek(self):
        if self.top==-1:
            print("stack underflow")
        else:
            return self.st[self.top]
        
    #return the current size of the stack
    def sizeofst(self):
        return self.top+1

    #print the elements of the stack from top to bottom    
    def printst(self):
        for i in range(self.top+1):
            print(self.st[i],end=" ")
        print()

s=stacks(5)
s.push(10)
s.push(20)  
s.push(30)
s.push(40)
s.push(50)   
print("size:",s.sizeofst()) 
s.printst()          
print(s.pop())
print("top:",s.peek())
print(s.pop())
print("top:",s.peek())
print(s.pop())  
print("size:",s.sizeofst())
