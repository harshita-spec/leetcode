#creating a node in linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#creating a class for SLL
class LL:
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
n1=Node(5)
sll=LL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
sll.traversal()
