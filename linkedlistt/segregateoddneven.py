# Segregate odd and even nodes in Linked List

# Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list.

# Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.
# Example 1
# Input: linkedList = [1, 2, 3, 4, 5]
# Output: [1, 3, 5, 2, 4]
# Explanation:
# The nodes with odd indices are 1, 3, 5 and the ones with even indices are 2, 4.
# Example 2
# Input: linkedList = [4, 3, 2, 1]
# Output: [4, 2, 3, 1]
# Explanation:
# The nodes with odd indices are 4, 2 and the ones with even indices are 3, 1.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    
    #brute force approach
    def segregate_odd_even(self):
        if self.head is None or self.head.next is None:
            return self.head
        arr=[]
        temp=self.head
        while temp is not None and temp.next is not None:
            arr.append(temp.data)
            temp=temp.next.next
        if temp:
            arr.append(temp.data)
        temp=self.head.next
        while temp is not None and temp.next is not None:
            arr.append(temp.data)
            temp=temp.next.next
        if temp:
            arr.append(temp.data)
        temp=self.head
        i=0
        while temp is not None:
            temp.data=arr[i]
            i+=1
            temp=temp.next
        return self.head
    
    #optimal approach
    def segregate_odd_even(self):
        if self.head is None or self.head.next is None:
            return self.head
        odd=self.head
        even=self.head.next
        evenhead=even
        while even is not None and even.next is not None:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenhead
        return self.head
    
n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(25)
n3.next=n4
n5=Node(30)
n4.next=n5
sll.segregate_odd_even()
temp=sll.head
while temp is not None:
    print(temp.data,end=" -> ")
    temp=temp.next
print("none")