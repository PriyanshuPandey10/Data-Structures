class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, e):
        index = len(self.heap)
        self.heap.append(e)  # Start by adding the new element at the end
        parent_index = (index - 1) // 2
        
        # Fix the heap property by "bubbling up" the new element
        while index > 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def create_heap(self, data_list):
        for e in data_list:
            self.insert(e)

    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        return self.heap[0]

    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        temp = self.heap.pop()
        if len(self.heap) == 0:
            return max_value

        self.heap[0] = temp
        index = 0
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        
        # Fix the heap property by "bubbling down" the new root element
        while left_child_index < len(self.heap):
            larger_child_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[left_child_index]:
                larger_child_index = right_child_index
            
            if self.heap[larger_child_index] > self.heap[index]:
                self.heap[larger_child_index], self.heap[index] = self.heap[index], self.heap[larger_child_index]
                index = larger_child_index
                left_child_index = 2 * index + 1
                right_child_index = 2 * index + 2
            else:
                break

        return max_value

    def heapsort(self, data_list):
        self.create_heap(data_list)
        sorted_list = []
        while len(self.heap) > 0:
            sorted_list.insert(0, self.delete())
        return sorted_list

class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg = msg
    def __str__(self):
        return self.msg

data_list = [30, 20, 50, 10, 70, 30, 20, 45, 20]
h = Heap()
sorted_list = h.heapsort(data_list)
print(sorted_list)
