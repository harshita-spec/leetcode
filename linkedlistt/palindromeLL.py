# Check if LL is palindrome or not

# Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. Check whether the linked list values form a palindrome or not. Return true if it forms a palindrome, otherwise, return false.

# A palindrome is a sequence that reads the same forward and backwards.
# Example 1
# Input: head -> 3 -> 7 -> 5 -> 7 -> 3
# Output: true
# Explanation: 37573 is a palindrome.
# Example 2
# Input: head -> 1 -> 1 -> 2 -> 1
# Output: false
# Explanation: 1121 is not a palindrome.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def palindrome(self):
        st=[]
        temp=self.head
        while temp is not None:
            st.append(temp.data)
            temp=temp.next
        temp=self.head
        while temp is not None:
            if st.pop()!=temp.data:
                return False
            temp=temp.next
        return True
n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(10)
n2.next=n3
n4=Node(15)
n3.next=n4
if sll.palindrome():
    print("Palindrome")
else:
    print("Not a Palindrome")
