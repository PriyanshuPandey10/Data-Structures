from typing import SupportsIndex


class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack Is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack Is Empty")
    def size(self):
        return len(self)
    

    #Implement the way to restrict use of insert() method of list class from stack object
    def insert(self,index,data):
        raise AttributeError("No Attribute 'insert'in stack")

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1)


# Check the size of the stack
print("Size of stack:", s1.size())

# Peek the top element
print("Top element:", s1.peek())

# Pop an element
print("Popped element:", s1.pop())

# Check if stack is empty
print("Is stack empty?", s1.is_empty())

# Display the stack after popping
print(s1)

