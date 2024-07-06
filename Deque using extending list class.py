class Deque(list):
    def __init__(self):
        self=[]
    def is_empty(self):
        return len(self)==0
    def insert_front(self,data):
        self.insert(0,data)
    def insert_rear(self,data):
        self.append(data)
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.pop(0)
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.pop(-1)
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self[0]
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self[-1]
    def size(self):
        return len(self)
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(),d1.get_rear())
