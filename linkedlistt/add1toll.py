# Add one to a number represented by Linked List

# Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. The task is to add one to the value represented by the linked list and return the head of a linked list containing the final value.

# The number will contain no leading zeroes except when the value represented is zero itself.
# Example 1
# Input: head -> 1 -> 2 -> 3
# Output: head -> 1 -> 2 -> 4
# Explanation: The number represented by the linked list = 123.
# 123 + 1 = 124.
# Example 2
# Input: head -> 9 -> 9
# Output: head -> 1 -> 0 -> 0
# Explanation: The number represented by the linked list = 99.

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
            while temp:
                print(temp.data,end=" -> ")
                temp=temp.next
            print("None")
    
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
    
    # def addOne(self,head):
    #     head=self.reverse(head)
    #     temp=head
    #     carry=1
    #     while temp is not None:
    #         temp.data+=carry
    #         if temp.data<10:
    #             carry=0
    #             break
    #         else:
    #             temp.data=0
    #             carry=1
    #         temp=temp.next
    #     if carry==1:
    #         newnode=Node(1)
    #         head=self.reverse(head)
    #         newnode.next=head
    #         return newnode
    #     head=self.reverse(head)
    #     return head
    
    def addone(self,head):
        carry=self.raddone(head)
        if carry==1:
            newnode=Node(1)
            newnode.next=head
            return newnode
        return head
    
    def raddone(self,temp):
        if temp==None:
            return 1
        carry=self.raddone(temp.next)
        temp.data+=carry
        if temp.data<10:
            return 0
        else:
            temp.data=0
            return 1
n1=Node(9)
sll=SLL()
sll.head=n1
n2=Node(8)
n3=Node(9)
n1.next=n2
n2.next=n3
sll.traversal()
# sll.head=sll.addOne(sll.head)
sll.head=sll.addone(sll.head)
sll.traversal()

