#reverse a DLL
#brute
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None     
class DLL:
    def __init__(self):
        self.head = None

    def traversal(self):
        print("none",end=" <-> ")
        a=self.head
        while a is not None:
            print(a.data,end=" <-> ")
            a=a.next
        print("none")

    def reverse(self):
        prev=None
        temp=self.head
        if temp==None or temp.next==None:
            return temp
        while temp!=None:
            prev=temp.prev
            temp.prev=temp.next
            temp.next=prev
            temp=temp.prev
        self.head=prev.prev

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
dll.traversal()
dll.reverse()
dll.traversal()