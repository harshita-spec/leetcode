# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
# Input: head = [1], n = 1
# Output: []
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def remove_nth_from_end(self,n):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next
        if count==n:
            newhead=self.head.next
            return newhead
        temp=self.head
        res=count-n
        while temp is not None:
            res-=1
            if res==0:
                break
            temp=temp.next
        delnode=temp.next
        temp.next=temp.next.next
        delnode.next=None
        return self.head
    
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
    
    def remove(self,n):
        fast=self.head
        slow=self.head
        for _ in range(n+1):
            fast = fast.next
        if fast is None:
            return self.head.next
        while fast is not None:
            slow=slow.next
            fast=fast.next 
        delnode=slow.next
        slow.next=slow.next.next
        delnode.next=None
        return self.head
    
n1 = Node(5)
sll = SLL()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(25)
n3.next = n4
n5 = Node(30)
n4.next = n5
n6 = Node(40)
n5.next = n6
n7 = Node(50)
n6.next = n7

sll.remove_nth_from_end(2)
sll.traversal()
sll.remove(3)
sll.traversal()