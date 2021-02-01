
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


if __name__ == '__main__':
    # O(log n)
    h = MaxHeap([1, 3, 4, 5, 5, 2, 4])
    print(h.peek())
    h.offer(7)
    print(h.poll())
    h.offer(6)
    print(h.poll())
