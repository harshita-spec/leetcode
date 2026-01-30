# Find the intersection point of Y LL

# Given the heads of two linked lists A and B, containing positive integers. Find the node at which the two linked lists intersect. If they do intersect, return the node at which the intersection begins, otherwise return null.

# The Linked List will not contain any cycles. The linked lists must retain their original structure, given as per the input, after the function returns.

# Note: for custom input, the following parameters are required(your program is not provided with these parameters):
# intersectVal - The value of the node where the intersection occurs. This is -1 if there is no intersected node.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node(-1 if no intersection).
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node(-1 if no intersection).
# listA - The first linked list.
# listB - The second linked list.
# Example 1
# Input: listA: intersectVal = 4, skipA = 3, skipB = 2, head -> 1 -> 2 -> 3 -> 4 -> 5, listB: head -> 7 -> 8 -> 4 -> 5
# Output(value at returned node is displayed): 4
# Explanation: The two lists have nodes with values 4 and 5 as their tails.
# Example 2
# Input: listA: intersectVal = -1, skipA = -1, skipB = -1, head -> 1 -> 2 -> 3, listB: head -> 8 -> 9
# Output(value at returned node is displayed): null
# Explanation: The two lists do not intersect.

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
    
    def getIntersectionNode(self,headA,headB):
        if headA is None or headB is None:
            return None
        mpp={}
        temp=headA
        while temp is not None:
            mpp[temp]=1
            temp=temp.next
        temp=headB
        while temp is not None:
            if temp in mpp:
                return temp
            temp=temp.next
        return None


n4 = Node(4)
n5 = Node(5)
n4.next = n5
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a1.next = a2
a2.next = a3
a3.next = n4   
listA = SLL()
listA.head = a1
b1 = Node(7)
b2 = Node(8)
b1.next = b2
b2.next = n4   
listB = SLL()
listB.head = b1
listA.traversal()
listB.traversal()
intersection = listA.getIntersectionNode(listA.head,listB.head)
if intersection:
    print(intersection.data)
else:
    print("null")