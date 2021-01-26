from queue import PriorityQueue, LifoQueue
import heapq
if __name__ == '__main__':
    q = PriorityQueue(20)
    q.put(4)
    q.put(2)
    q.put(5)
    q.put(1)
    q.put(3)
    print('min heap', q.queue)
    while not q.empty():
        next_item = q.get()
        print(next_item)
    print('\n')
    l = [4, 2, 5, 1, 3]
    print('heapify before', l)
    heapq.heapify(l)
    print('heapify after', l)

    while len(l):
        print(heapq.heappop(l))
