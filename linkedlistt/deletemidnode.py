# Delete the middle node in LL

# Given the head of a non-empty singly linked list containing integers, delete the middle node of the linked list. Return the head of the modified linked list.

# The middle node of a linked list of size n is the (⌊n / 2⌋ + 1)th node from the start using 1-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# Example 1
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5
# Output: head -> 1 -> 2 -> 4 -> 5
# Explanation: n = 5.
# ⌊n / 2⌋ + 1 = 3, therefore middle node has index 3 and so the node with value 3 was deleted.
# Example 2
# Input: head -> 7 -> 6 -> 5 -> 4
# Output: head -> 7 -> 6 -> 4
# Explanation: n = 4.
# ⌊n / 2⌋ + 1 = 3, therefore middle node has index 3 and so the node with value 5 was deleted.

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

    #brute 
    def deletemidnode(self):
        if self.head is None or self.head.next is None:
            return None
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next
        mid=count//2
        if mid==0:
            newhead=self.head.next
            return newhead
        temp=self.head
        for _ in range(mid-1):
            temp=temp.next
        delnode=temp.next
        temp.next=temp.next.next
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
sll.deletemidnode()
sll.traversal()