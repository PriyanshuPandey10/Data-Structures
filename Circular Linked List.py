#Define a class Node to describe a node of a Circular Linked List
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

#Define a class CLL to implement Circular Linked List with __init__() method to create and initialize last reference variable
class CLL:
    def __init__(self,last=None):
        self.last=last

    #Define a method is_empty() to check if the Linked List is empty in CLL class
    def is_empty(self):
        return self.last==None
    
    #Define a method insert_at_start() to insert an element at the starting of a list 
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n

    #Define a method insert_at_last() to insert an element at the last of a list 
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    #Define a method search() to find the node with the specified element value
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    
    #Define a method insert after() to insert a node after a given node of a list
    def insert_after(self,data,temp):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp == self.last:
                self.last=n

    #Define a method print_all() to print all the elements of a list
    def print_all(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item)

    #Define a method delete_first() to delete the first element from a list
    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next

    #Define a method  delete_last() to delete the last element from the list
    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next == self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp

    #Define a method delete_item() to delete specified elements from the list
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:
                    temp=self.last.next

                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                            break
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
                        
    
                    


my_list=CLL()
my_list.insert_at_start(500)
my_list.insert_at_start(400)
my_list.insert_at_start(300)
my_list.insert_at_start(200)
my_list.insert_at_start(100)
my_list.insert_at_last(600)
my_list.insert_at_last(800)
my_list.insert_at_last(900)
my_list.insert_at_last(1000)
my_list.insert_after(700,my_list.search(600))
my_list.print_all()
my_list.delete_first()
my_list.print_all()
my_list.delete_last()
my_list.print_all()
my_list.delete_item(300)
my_list.print_all()

 
 



