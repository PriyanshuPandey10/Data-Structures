class PriorityQueue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
p=PriorityQueue()
p.push("Rahul",5)
p.push("Rupesh",3)
p.push("Ramesh",1)
p.push("DEEPAK",7)
p.push("Krishna",2)
while not p.is_empty():
    print(p.pop())
