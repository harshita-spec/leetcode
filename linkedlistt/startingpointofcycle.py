#  Find the starting point in LL

# Given the head of a singly linked list, the task is to find the starting point of a loop in the linked list if it exists. Return the starting node if a loop exists; otherwise, return null.

# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos denotes the index (0-based) of the node from where the loop starts.

# Note that pos is not passed as a parameter.
# Example 1
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
# Output(value of the returned node is displayed): 2
# Expla﻿nation: The tail of the linked list connects to the node at 1st index.
# Example 2
# Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
# Output(value of the returned node is displayed): null
# Explanation: No loop is present in the linked list.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    #brute force
    def loop_starting_point(self):
        mpp={}
        temp=self.head
        while temp is not None:
            if temp in mpp:
                return temp
            mpp[temp]=1
            temp=temp.next
        return None
    #optimal
    def loop_starting_point_optimal(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                slow=self.head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(25)
n3.next=n4
n4.next=n2
result=sll.loop_starting_point()
if result:
    print(result.data)
else:
    print("No loop detected")
if sll.loop_starting_point_optimal():
    print(sll.loop_starting_point_optimal().data)
else:
    print("No loop detected")