# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
# Input: head = []
# Output: []

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
          
class SLL:
    def __init__(self):
        self.head = None

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

    def reverse(self):
        prev=None
        temp=self.head
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        self.head=prev

        
n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(25)
n3.next=n4
sll.traversal()
sll.reverse()
sll.traversal()