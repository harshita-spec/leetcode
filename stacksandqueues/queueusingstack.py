# 232. Implement Queue using Stacks

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class StackQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []
 
    def traversal(self):
        for i in self.st1:
            print(i,end=" ")
        print()

    def push(self, x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            print("Stack is empty")
            return -1 
        top_element = self.st1.pop()  
        return top_element  

    def peek(self):
        if not self.st1:
            print("Stack is empty")
            return -1  
        return self.st1[-1]

    def is_empty(self):
        return not self.st1
    
q = StackQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.traversal()
print(q.peek())
print(q.pop())
print(q.is_empty())


class Stackqueue:
    def __init__(self):
        self.input = []  
        self.output = [] 

    def push(self, x):
        self.input.append(x)

    def pop(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            print("Queue is empty, cannot pop.")
            return -1
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            print("Queue is empty, cannot peek.")
            return -1
        return self.output[-1]

    def isEmpty(self) :
        return not self.input and not self.output
    
print()
q = Stackqueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print(q.peek())
print(q.pop())
print(q.isEmpty())