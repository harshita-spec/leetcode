# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end=" -> ")
                temp=temp.next
            print("None")

    def removeduplicates(self):
        if self.head is None or self.head.next is None:
            return self.head
        a=self.head
        temp=self.head.next
        while temp:
            if a.data == temp.data:
                a.next=temp.next
                temp.next=None
                temp=a.next
            else:
                a=a.next
                temp=temp.next
        return self.head
    
n1 = Node(5)
sll = SLL()
sll.head = n1
n2 = Node(5)
n1.next = n2
n3 = Node(10)
n2.next = n3
n4 = Node(15)
n3.next = n4
n5 = Node(15)
n4.next = n5
n6 = Node(15)
n5.next = n6
sll.removeduplicates()
sll.traversal()