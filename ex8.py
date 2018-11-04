
import random


def min_child(i, size):
    if i * 2 + 1 > size:
        return i * 2
    else:
        if heap_list[i * 2] < heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

def perc_d(index, size):
    while(index * 2) <= size:
        mc = min_child(index, size)
        if heap_list[index] > heap_list[mc]:
            heap_list[index], heap_list[mc] = heap_list[mc], heap_list[index]
        index = mc

def sort_f(a_list):
    i = len(a_list) // 2
    global heap_list 
    heap_list = [0] + a_list[:]
    while (i > 0):
        perc_d(i, len(a_list))
        i -= 1
    return heap_list

my_test = []
for i in range(11):
    my_test.append(random.randrange(0, 100))
print(my_test)
print(sort_f(my_test))