# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

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

    def merge2sortedll(self,head1,head2):
        a=head1
        b=head2
        dummy=Node(-1)
        temp=dummy
        while a is not None and b is not None:
            if a.data <= b.data:
                temp.next=a
                temp=a
                a=a.next
            else:
                temp.next=b
                temp=b
                b=b.next
        while a is not None:
            temp.next=a
            temp=a
            a=a.next
        while b is not None:
            temp.next=b
            temp=b
            b=b.next
        return dummy.next
    
n1 = Node(5)
sll = SLL()
sll.head = n1
n2 = Node(6)
n1.next = n2
n3 = Node(10)
n2.next = n3
n4 = Node(15)
n3.next = n4
n5 = Node(16)
n4.next = n5

t1 = Node(1)
sll.head = t1
t2 = Node(4)
t1.next = t2
t3 = Node(10)
t2.next = t3
t4 = Node(11)
t3.next = t4
t5 = Node(19)
t4.next = t5

sll.merge2sortedll(n1,t1)
sll.traversal()