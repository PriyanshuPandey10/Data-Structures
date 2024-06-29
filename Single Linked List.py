#Class Node to describe a node of a Single Linked List
class Node:
    def __init__(self, item=None,next=None):
        self.item = item
        self.next = next


#Class SingleLinkedList to describe a Single Linked List
class SLL:
    def __init__(self,start=None):
        self.start=start

    #is_empty() => To check whether a linked list is empty in Single Linked List 
    def is_empty(self):
        return self.start ==None
    
    #insert_at_start => To insert an element at the starting of the List
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    
    #insert_at_end => To insert an element at the end of the list
    def insert_at_end(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next =n
        else:
            self.start=n
    
    #search() => To find the node with the specified element value
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None
    
    #insert_after => To insert a node after a given node in a list
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

    #print_list() => To print all the elements of a list
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
        print()









my_list=SLL()
print("List is empty:",my_list.is_empty())
my_list.insert_at_start(23)
my_list.insert_at_start(5)
my_list.insert_at_end(15)
my_list.insert_at_end(20)
my_list.insert_after(my_list.search(5), 100)
my_list.print_list()



