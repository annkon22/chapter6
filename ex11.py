#11. Using the BinaryHeap class, implement a new class called PriorityQueue. Your PriorityQueue 
# class should implement the constructor, plus the enqueue and dequeue methods.


class PriorityQueue:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i][0] < self.heap_list[i // 2][0]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def enqueue(self, k, val_prior):
        self.heap_list.append((k, val_prior))
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while(i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i][0] > self.heap_list[mc][0]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc
    
    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2][0] < self.heap_list[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1
                
    def dequeue(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val[1]

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.perc_down(i)
            i -= 1


my_test = PriorityQueue()
my_test.enqueue(10, 23)
my_test.enqueue(1, 2)
my_test.enqueue(18, 36)
my_test.enqueue(6, 9)
my_test.enqueue(30, 7)
print(my_test.heap_list)
print(my_test.dequeue())
