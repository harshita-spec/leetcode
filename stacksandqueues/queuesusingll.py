# Node structure
class Node:
    def __init__(self, d):
        self.val = d
        self.next = None

# Structure to represent queue
class LinkedListQueue:
    def __init__(self):
        self.start = self.end = None  
        self.size = 0  

    # Method to push an element in the queue
    def push(self, x):
        element = Node(x)
        if self.start is None:
            self.start = self.end = element
        else:
            self.end.next = element  
            self.end = element 
        self.size += 1

    # Method to pop an element from the queue
    def pop(self):
        if self.start is None:
            return -1  
        value = self.start.val 
        temp = self.start  
        self.start = self.start.next  
        del temp  
        self.size -= 1 
        return value 
    
    def peek(self):
        if self.start is None:
            return -1 
        return self.start.val 

    def isEmpty(self):
        return self.size == 0

# Creating a queue
q = LinkedListQueue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
print("size:", q.size)
print("front:", q.peek())
print(q.pop())
print("front:", q.peek())   
print(q.pop())
print("size:", q.size)
print("isEmpty:", q.isEmpty())
