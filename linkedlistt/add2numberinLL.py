# Add two numbers in Linked List

# Given two non-empty linked lists linkedList1 and linkedList2 which represent two non-negative integers.

# The digits are stored in reverse order with each node storing one digit.
# Add two numbers and return the sum as a linked list.

# The sum Linked List will be in reverse order as well.

# The Two given Linked Lists represent numbers without any leading zeros, except when the number is zero itself.
# Example 1
# Input: linkedList1 = [5, 4], linkedList2 = [4]
# Output: [9, 4]
# Explanation: linkedList1 = 45, linkedList2 = 4.
# linkedList1 + linkedList2 = 45 + 4 = 49.
# Example 2
# Input: linkedList1 = [4, 5, 6], linkedList2 = [1, 2, 3]
# Output: [5, 7, 9]
# Explanation: linkedList1 = 654, linkedList2 = 321.
# linkedList1 + linkedList2 = 654 + 321 = 975.

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

    def addtwonumber(self,head1,head2):
        t1=head1
        t2=head2
        dummynode=Node(-1)
        curr=dummynode
        carry=0
        while t1!=None or t2!=None:
            sum=carry
            if t1:
                sum+=t1.data
            if t2:
                sum+=t2.data
            newnode=Node(sum%10)
            carry=sum//10
            curr.next=newnode
            curr=curr.next
            if t1:
                t1=t1.next
            if t2:
                t2=t2.next
        if carry:
            newnode=Node(carry)
            curr.next=newnode
        return dummynode.next

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a1.next = a2
a2.next = a3  
listA = SLL()
listA.head = a1
b1 = Node(7)
b2 = Node(8)
b1.next = b2 
listB = SLL()
listB.head = b1
listA.traversal()
listB.traversal()
result = listA.addtwonumber(listA.head, listB.head)
resList = SLL()
resList.head = result
resList.traversal()
