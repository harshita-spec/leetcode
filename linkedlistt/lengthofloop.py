# Length of loop in LL
# Given the head of a singly linked list, find the length of the loop in the linked list if it exists. Return the length of the loop if it exists; otherwise, return 0.

# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos is used to denote the index (0-based) of the node from where the loop starts.

# Note that pos is not passed as a parameter.
# Example 1
#ut: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
# Output: 4
# Explanation: 2 -> 3 -> 4 -> 5 - >2, length of loop = 4.
# Example 2
# Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
# Output: 0
# Explanation: No loop is present in the linked list.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    
    #brute force
    def length(self):
        mpp={}
        temp=self.head
        timer=0
        while temp is not None:
            if temp in mpp:
                return timer-mpp[temp]
            mpp[temp]=timer
            timer+=1
            temp=temp.next
        return 0
    #optimal
    def length_optimal(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                count=1
                fast=fast.next
                while slow!=fast:
                    count+=1
                    fast=fast.next
                return count
        return 0
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
print(sll.length())
print(sll.length_optimal())