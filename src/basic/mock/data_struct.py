from queue import PriorityQueue, LifoQueue
import heapq
if __name__ == '__main__':
    q = PriorityQueue(4)
    q.put_nowait(4)
    q.put_nowait(2)
    # q.put_nowait(5)
    # q.put_nowait(1)
    # q.put_nowait(3)
    print('min heap', q.queue)
    # while not q.empty():
    #     next_item = q.get()
    #     print(next_item)
    # print('\n')
    # l = [4, 2, 5, 1, 3]
    # print('heapify before', l)
    # heapq.heapify(l)
    # print('heapify after', l)

    # while len(l):
    #     print(heapq.heappop(l))
    nums = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]

    def gen(nums):
        for i in range(len(nums)):
            yield nums[i]
    nums_iter = iter(nums)
    print('nums_iter')
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
    nums_gen = gen(nums)
    print('nums_gen')
    print(next(nums_gen))
    print(next(nums_gen))
    print(next(nums_gen))
    print(next(nums_gen))
