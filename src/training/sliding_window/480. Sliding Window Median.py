'''
480. 滑动窗口中位数
中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
提示：

你可以假设 k 始终有效，即：k 始终小于等于输入的非空数组的元素个数。
与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
'''

import collections
import heapq


class MedianFinder:
    def __init__(self, k):
        self.k = k
        self.small = []
        self.large = []
        self.small_size = self.large_size = 0
        self.delayed = collections.Counter()

    def prune(self, heap):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                break

    def make_balance(self):
        if self.small_size >= self.large_size + 2:
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.large_size >= self.small_size+1:
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def add_num(self, num):
        if not self.small or num < -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.make_balance()

    def pop_num(self, num):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.make_balance()

    def find_median(self):
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0]+self.large[0])/2
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums:
            return []
        f = MedianFinder(k)
        for i in range(k):
            f.add_num(nums[i])
        ret = [f.find_median()]
        for i in range(k, len(nums)):
            f.add_num(nums[i])
            f.pop_num(nums[i-k])
            ret.append(f.find_median())
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print('1', s.medianSlidingWindow(nums, k))  # [1,-1,-1,3,5,6]
