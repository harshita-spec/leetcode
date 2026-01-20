#creating a node in linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#creating a class for SLL
class SLL:
    def __init__(self):
        self.head=None

#traversal of linked list
    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" -> ")
                temp=temp.next
            print("None")

#insert at the beginning of linked list
    def insert_at_beginning(self,data):
        print("insert at beginning:")
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node 

#insert at the end of linked list
    def insert_at_end(self,data):
        print("insert at end:")
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne

#insert at specific position       
    def insert_specific_position(self,position,data):
        print("insert at specific position:")
        npn=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        npn.next=a.next
        a.next=npn

#deleting a node at beginning
    def delete_at_beginning(self):
        print("deleting at beginning:")
        a=self.head
        self.head=a.next
        a.next=None
n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
sll.traversal()
sll.insert_at_beginning(1)
sll.traversal()
sll.insert_at_end(12)
sll.traversal()
sll.insert_specific_position(2,7)
sll.traversal()
sll.delete_at_beginning()
sll.traversal()