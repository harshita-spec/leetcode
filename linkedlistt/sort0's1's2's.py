# Sort a Linked List of 0's 1's and 2's

# Given the head of a singly linked list consisting of only 0, 1 or 2.

# Sort the given linked list and return the head of the modified list.

# Do it in-place by changing the links between the nodes without creating new nodes.
# Example 1
# Input: linkedList = [1, 0, 2, 0 , 1]
# Output: [0, 0, 1, 1, 2]
# Explanation: The values after sorting are [0, 0, 1, 1, 2].
# Example 2
# Input: linkedList = [1, 1, 1, 0]
# Output: [0, 1, 1, 1]
# Explanation: The values after sorting are [0, 1, 1, 1].

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

    # def sortll(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     count0 = count1 = count2 = 0
    #     temp = head
    #     while temp:
    #         if temp.data == 0:
    #             count0 += 1
    #         elif temp.data == 1:
    #             count1 += 1
    #         elif temp.data == 2:
    #             count2 += 1
    #         temp = temp.next
    #     temp = head
    #     while temp:
    #         if count0 > 0:
    #             temp.data = 0
    #             count0 -= 1
    #         elif count1 > 0:
    #             temp.data = 1
    #             count1 -= 1
    #         else:
    #             temp.data = 2
    #             count2 -= 1
    #         temp = temp.next
    #     return head
    
    def sortLL(self,head):
        if head is None or head.next is None:
            return head
        zerohead=Node(-1)
        onehead=Node(-1)
        twohead=Node(-1)
        zero=zerohead
        one=onehead
        two=twohead
        temp=head
        while temp is not None:
            if temp.data==0:
                zero.next=temp
                zero=zero.next
            elif temp.data==1:
                one.next=temp
                one=one.next
            else:
                two.next=temp
                two=two.next
            temp=temp.next
        if onehead.next is not None:
            zero.next=onehead.next
        else:
            zero.next=twohead.next
        one.next=twohead.next
        two.next=None
        return zerohead.next

  
n1 = Node(0)
sll = SLL()
sll.head = n1
n2 = Node(1)
n1.next = n2
n3 = Node(2)
n2.next = n3
n4 = Node(0)
n3.next = n4
n5 = Node(0)
n4.next = n5
n6 = Node(1)
n5.next = n6   
# sll.traversal()
# sll.head = sll.sortll(sll.head)
sll.traversal()
sll.head = sll.sortLL(sll.head)
sll.traversal()
