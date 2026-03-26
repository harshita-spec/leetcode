class Node:
    def __init__(self, d):
        self.val = d
        self.next = None

# Structure to represent stack
class LinkedListStack:
    def __init__(self):
        self.head = None  
        self.size = 0  

    # Method to push an element onto the stack
    def push(self, x):
        element = Node(x)
        element.next = self.head 
        self.head = element
        self.size += 1

    # Method to pop an element from the stack
    def pop(self):
        if self.head is None:
            return -1 
        value = self.head.val 
        temp = self.head 
        self.head = self.head.next 
        del temp 
        self.size -= 1  
        return value 

    # Method to get the top element of the stack
    def top(self):
        if self.head is None:
            return -1  
        return self.head.val  

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.size == 0

st = LinkedListStack()
st.push(10)
st.push(20)     
st.push(30)
st.push(40)
st.push(50)
print("size:", st.size)
print("top:", st.top())
print(st.pop())
print("top:", st.top())
print(st.pop())
print("size:", st.size)
print("isEmpty:", st.isEmpty())