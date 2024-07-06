#Define a class stack to implement stack data structure using SLL.Define __init__() method to initialize start variable and item_count variable to keep track of number of elements in the stack.
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0

    #Define a method is_empty() to check if the stack is empty or not
    def is_empty(self):
        return self.start==None
    
    #Define a method push() to add data in stack
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1

    #Define pop() method to remove top element from stack
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty")
        
    #Define peek() method to remove top element from stack 
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise self.is_empty()
        
    #Define size() method to return size of the stack
    def size(self):
        return self.item_count
    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Total elements in the stack=",s1.size())
print("Top element on the stack is",s1.peek())
print("Poped element is",s1.pop())
print("Total elements in the stack=",s1.size())
print("Top element on the stack is",s1.peek())
print()
