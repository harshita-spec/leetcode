# Sort LL

# Given the head of a singly linked list. Sort the values of the linked list in non-decreasing order and return the head of the modified linked list.
# Example 1
# Input: head -> 5 -> 6 -> 1 -> 2 -> 1
# Output: head -> 1 -> 1 -> 2 -> 5 -> 6
# Explanation: 1 <= 1 <= 2 <= 5 <= 6
# Example 2
# Input: head -> 6 -> 5 -> -1 -> -2 -> -3
# Output: head -> -3 -> -2 -> -1 -> 5 -> 6
# Explanation: -3 <= -2 <= -1 <= 5 <= 6
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
    
    #brute force
    def sortll(self):
        if self.head is None or self.head .next is None:
            return self.head
        arr=[]
        temp=self.head
        while temp is not None:
            arr.append(temp.data)
            temp=temp.next
        arr.sort()
        temp=self.head
        i =0
        while temp is not None:
            temp.data=arr[i]
            i+=1
            temp=temp.next
        return self.head
    
    #optimal
    def sortLL(self,head):
        if head is None or head.next is None:
            return head
        middle =self.findmiddle(head)
        leftmid=head
        rightmid=middle.next
        middle.next = None
        leftsorted=self.sortLL(leftmid)
        rightsorted=self.sortLL(rightmid)
        return self.merged(leftsorted,rightsorted)
    
    def findmiddle(self,head):
        slow=head
        fast=head.next
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
    
    def merged(self,left,right):
        dummy=Node(-1)
        temp=dummy
        while left is not None and right is not None:
            if left.data<right.data:
                temp.next=left
                temp=left
                left=left.next
            else:
                temp.next=right
                temp=right
                right=right.next

        if left:
            temp.next=left
        else:
            temp.next=right
        return dummy.next

n1 = Node(5)
sll = SLL()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(25)
n3.next = n4
n5 = Node(13)
n4.next = n5
n6 = Node(4)
n5.next = n6   
sll.traversal()
sll.sortll()
sll.traversal()
sll.head = sll.sortLL(sll.head)
sll.traversal()