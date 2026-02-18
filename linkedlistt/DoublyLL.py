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

# inserting nodes at beginning
    def insert_at_beginning(self,data):
        nb=Node(data)
        a=self.head
        nb.next=self.head
        a.prev=nb
        self.head=nb

#inserting at end
    def insert_at_end(self,data):
        ns=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ns
        ns.prev=a

#insert at specific position
    def insert_specific_position(self,data,position):
        npn=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        npn.next=a.next
        npn.prev=a
        if a.next is not None:
            a.next.prev=npn
        a.next=npn     

#deletion at beginning
    def delete_at_beginning(self):
        a=self.head
        self.head=a.next
        a.next.prev=None
        a.next=None
#deletion at end
    def deletion_at_end(self):
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        a.prev=None
        prev.next=None
#deletion at specific position
    def deletion_at_position(self,position):
        prev=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next.prev=prev
        a.next=None
        a.prev=None

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
dll.backward_traversal()
dll.insert_at_beginning(30)
dll.forward_traversal()
dll.backward_traversal()
dll.insert_at_end(40)
dll.forward_traversal()
dll.backward_traversal()
dll.insert_specific_position(50,4)
dll.forward_traversal()
dll.backward_traversal()
dll.delete_at_beginning()
dll.forward_traversal()
dll.backward_traversal()
dll.deletion_at_end()
dll.forward_traversal()
dll.backward_traversal()
dll.deletion_at_position(2)
dll.forward_traversal()
dll.backward_traversal()