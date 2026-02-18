# 876: Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one

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
 
    def middle(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow

n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(25)
n3.next=n4
n5=Node(45)
n4.next=n5
sll.traversal()
sll.middle()
print(sll.middle().data)