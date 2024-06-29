#Class Node to describe a node of a Single Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#Class SingleLinkedList to describe a Single Linked List
class SingleLinkedList:
    def __init__(self,start=None):
        self.start=start

    #is_empty() => To check whether a linked list is empty in Single Linked List 
    def is_empty(self):
        return self.start == None
    
    #insert_at_start => To insert an element at the starting of the List
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    
    #insert_at_end => To insert an element at the end of the list
    def insert_at_end(self,data)
        n=Node(data)
        if not self.is_empty:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next =n
        else:
            self.start=n


