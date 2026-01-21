#creating a node in dll
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None  
#creating a class for DLL
class DLL:
    def __init__(self):
        self.head=None
    
# forward traversal of linked list
    def forward_traversal(self):
        print("none",end=" <-> ")
        a=self.head
        while a is not None:
            print(a.data,end=" <-> ")
            a=a.next
        print("none")
# backward traversal of linked list
    def backward_traversal(self):
        print("none",end=" <-> ")
        a=self.head
        while a.next is not None:
            a=a.next
        while a is not None:
            print(a.data,end=" <-> ")
            a=a.prev
        print("none")

n1=Node(10)
dll=DLL()
dll.head=n1
n2=Node(15)
n1.next=n2
n2.prev=n1
n3=Node(20)
n2.next=n3
n3.prev=n2
n4=Node(25)
n3.next=n4
n4.prev=n3
dll.forward_traversal()
print()
dll.backward_traversal()
print()