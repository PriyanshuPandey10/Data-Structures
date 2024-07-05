#Define a class Stack to implement stack data structure using list.Define __init__() method to create an empty list of objects as instance object member of stack
class Stack:
    def __init__(self):
        self.items=[]

    #Define a method is_empty() to check if the stack is empty in Stack class
    def is_empty(self):
        return len(self.items)==0
            
        
    #Define a method push() to add data in stack
    def push(self,data):
        self.items.append(data)

    #Define a method pop() to remove the top element from stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
        
    #Define a method peek() to return top element from a stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack Is Empty")
        
    #Define a method size() to return size of the stack
    def size(self):
        return len(self.items)
    

s1=Stack()
s1.push(50)
s1.push(40)
s1.push(30)
s1.push(20)
s1.push(10)
print(s1.items)


# Check the size of the stack
print("Size of stack:", s1.size())

# Peek the top element
print("Top element:", s1.peek())

# Pop an element
print("Popped element:", s1.pop())

# Check if stack is empty
print("Is stack empty?", s1.is_empty())

# Display the stack after popping
print(s1.items)