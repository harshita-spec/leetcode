# Detect a loop in Linked List

# Given the head of a singly linked list. Return true if a loop exists in the linked list or return false.

# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer.

# Internally, pos is used to denote the index(0-based) of the node from where the loop starts. Note that pos is not passed as a parameter.
# Example 1
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
# Output: true
# Explanation: The tail of the linked list connects to the node at 1st index.
# Example 2
# Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
# Output: false
# Explanation: No loop is present in the linked list.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    # def detectloop(self):
    #     mpp={}
    #     temp=self.head
    #     while temp is not None:
    #         if temp in mpp:
    #             return True
    #         mpp[temp]=1
    #         temp=temp.next
    #     return False
    def detect_loop(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False
    
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
if sll.detect_loop():
    print("Loop detected")
else:
    print("No loop detected")