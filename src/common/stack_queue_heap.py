
import heapq
class MaxHeap():
    def __init__(self, nums):
        self.rev_nums = [-e for e in nums]
        heapq.heapify(self.rev_nums)

    def offer(self, e):
        heapq.heappush(self.rev_nums, -e)

    def poll(self):
        return -heapq.heappop(self.rev_nums)

    def peek(self):
        return -self.rev_nums[0]


'''
  Queue
  - priority queue
  - lifo queue
  - deque 头部尾部的append/pop都是O(1)，list 头部pop会消耗O(n)
'''

import collections
import queue
if __name__=='__main__':
    dp = collections.deque([1,2,3,4,5],5)
    print(dp)
    dp.append(0)
    print('尾部插入0',dp)
    dp.appendleft(3)
    print('头部插入3',dp)
    dp.pop()
    print('尾部pop',dp)
    dp.popleft()
    print('头部pop', dp)
    q = queue.LifoQueue(5)
    for i in range(5):
        q.put(i)
    print(q)
    pq = queue.PriorityQueue(5)
    for i in range(5):
        pq.put(i)
    print(pq)
    # O(log n)
    h = MaxHeap([1, 3, 4, 5, 5, 2, 4])
    print(h.peek())
    h.offer(7)
    print(h.poll())
    h.offer(6)
    print(h.poll())
