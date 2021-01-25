from queue import PriorityQueue, LifoQueue
import heapq
if __name__ == '__main__':
    q = PriorityQueue(20)
    q.put(4)
    q.put(2)
    q.put(5)
    q.put(1)
    q.put(3)

    while not q.empty():
        next_item = q.get()
        print(next_item)
