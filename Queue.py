#Define a class Queue to implement queue data structure using list.Define __init__() method to create an empty list objects as instance objects of queue.
class Queue:
    def __init__(self):
        self.items=[]
    #Define a method is_empty() to check whether a queue is empty in Queue class
    def is_empty(self):
        return len(self.items)==0
    #Define a method enqueue() to add data at the rear end of the queue 
    def enqueue(self,data):
        self.items.append(data)
    #Define a method dequeue() to delete the data from the front end of the queue
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue Underflow")
    #Define get_front() method to return the front element of a queue
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
    #Define get_rear() method to return the front element of a queue
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")
    #Define a method size() to return size of a queue
    def size(self):
        return len(self.items)
    


q1=Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Front=",q1.get_front(),"Rear=",q1.get_rear())
try:
    q1.dequeue()
    print("Queue has now",q1.size(),"elements")

except IndexError as e:
    print(e.args[0])
