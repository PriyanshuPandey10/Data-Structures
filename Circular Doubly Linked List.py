#Define a class Node to describe a node of a circular doubly linked list
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

#Define a class CDLL to implement Circular Doubly Linked List with __init__() method to create and initialize last reference variable
class CDLL:
    def __init__(self,start=None):
        self.start=start

    #Define a method is_empty() to check if the Linked List is empty in CDLL class
    def is_empty(self):
        return self.start==None 
    
    #Define a method insert_at_start() to insert an element at the starting of the list
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
        
    #Define a method insert_at_last() to insert an element at the end of the list
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            
            n.next=self.start
            n.prev=self.start.prev
            n.prev.next=n
            self.start.prev=n

    #Define a method search() to search an element in list
    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
        while temp!=self.start:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    #Define a method insert_after() to insert a node after the given node of a list
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data)
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n
        
    #Define a method print_list() to print all the elements present in the list
    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
            while temp is not self.start:
                print(temp.item,end=' ')
                temp=temp.next

    #Define a method delete first() to delete first element from the list
    def delete_first(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next

    #Define a method delete_last() to delete the last element from the list
    def delete_last(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev

    #Define a method delete_item() to delete a specified item from the list
    def delete_item(self,data):
        if self.start is not None:
            temp=self.start
            if temp.item==data:
                self.delete_first()
            else:
                temp=temp.next
                while temp is not self.start:
                    if temp.item==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
                    temp=temp.next






my_list=CDLL()
my_list.insert_at_start(100)
my_list.insert_at_start(200)
my_list.insert_at_start(300)
my_list.insert_at_start(400)
my_list.insert_at_start(500)
my_list.insert_at_last(10)
my_list.insert_at_last(20)
my_list.insert_at_last(30)
my_list.insert_at_last(40)
my_list.insert_after(my_list.search(20),25)
my_list.print_list()
print()
my_list.delete_first()
my_list.print_list()
print()
my_list.delete_last()
my_list.print_list()
print()
my_list.delete_item(25)
my_list.print_list()




        