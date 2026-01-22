#creating a node in linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#creating a class for SLL
class SLL:
    def __init__(self):
        self.head=None

#traversal of linked list
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

#insert at the beginning of linked list
    def insert_at_beginning(self,data):
        print("insert at beginning:")
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node 

#insert at the end of linked list
    def insert_at_end(self,data):
        print("insert at end:")
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne

#insert at specific position       
    def insert_specific_position(self,position,data):
        print("insert at specific position:")
        npn=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        npn.next=a.next
        a.next=npn

#deleting a node at beginning
    def delete_at_beginning(self):
        print("deleting at beginning:")
        a=self.head
        self.head=a.next
        a.next=None

# deleting a node at end
    def delete_at_end(self):
        print("deleting at end:")
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None

# deletion at specific position can be implemented similarly
    def delete_at_specific_position(self,pos):
        print("deleting at specific position:")
        prev=self.head
        a=self.head.next
        for i in range(1,pos-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next=None

#delete a specific node
    def delete_a_node(self,key):
        print("deleting at specific node data:")
        prev=self.head
        a=self.head.next
        while a.data!=key and a.next is not None:
            a=a.next
            prev=prev.next
        if a.data==key:
            prev.next=a.next
            a.next=None

#length of linked list
    def length(self):
        count=0
        a=self.head
        while a is not None:
            count+=1
            a=a.next
        return count   

#Search in Linked List
    def search(self,key):
        a=self.head
        while a is not None:
            if a.data==key:
                return True
            a=a.next
        return False  
              
n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(25)
n3.next=n4
sll.traversal()
sll.insert_at_beginning(1)
sll.traversal()
sll.insert_at_end(12)
sll.traversal()
sll.insert_specific_position(2,7)
sll.traversal()
sll.delete_at_beginning()
sll.traversal()
sll.delete_at_end()
sll.traversal()
sll.delete_at_specific_position(2)
sll.traversal()
sll.delete_a_node(15)
sll.traversal()
print("Length of the linked list :", sll.length())
print("search of element 10 in LL:",sll.search(10))
print("search of element 12 in LL:",sll.search(12))