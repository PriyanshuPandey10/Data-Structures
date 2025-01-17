#Define a class Node to describe a node of a Doubly Linked List
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
    
#Define a class DLL to implement __init__() method to create and initialize start reference variable.
class DLL:
    def __init__(self,start=None):
        self.start=start

    #Define a method is_empty() to check if the linked list is empty 
    def is_empty(self):
        return self.start==None
    

    #Define a method insert_at_start() to insert an element at the startng of a list
    def insert_at_start(self,data):
        n=Node(data,None,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n

    #Define a method insert_at_last() to insert an element at last of a list
    def insert_at_last(self,data):
        temp=self.start
        if not self.is_empty():
            while temp.next!=None:
                temp=temp.next
        n=Node(data,temp,None)
        if temp ==None:
            self.start=n
        else:
            temp.next=n

    #Define a method search() to find the node with specified element value 
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    

    #Define a method insert_after() to insert a new node after a given node of a list
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n

    #Define a method print_list() to print all the elements of the list
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next

    #Define a method delete_first() to delete the first element from the list
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    #Define a method delete_last() to delete the last element from the list
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None

    #Define a method delete_item() to delete the specified element from the list
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not Node:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next


    



        


my_list=DLL()
my_list.insert_at_start(35)
my_list.insert_at_start(45)
my_list.insert_at_last(100)
my_list.insert_at_last(200)
my_list.insert_after(my_list.search(100),150)
my_list.delete_first()
my_list.delete_last()
my_list.delete_item(100)
my_list.print_list()
