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

import heapq
class MedianFinder:

    def __init__(self,k):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        import collections
        self.delayed = collections.Counter()
        self.k=k

    #时间复杂度O(logn)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)
        heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        if len(self.minheap) < len(self.maxheap):
            n = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, n)

    def findMedian(self) -> float:
        return (self.minheap[0]-self.maxheap[0])/2 if len(self.minheap) == len(self.maxheap) else self.minheap[0]
    def popNum(self,num):
        # heapq.heappop()
        pass

class Solution:
    def medianSlidingWindow(self, nums, k: int):
        if not nums:return
        m = MedianFinder(k)
        ret=[]
        for i in range(k-1):
            m.addNum(nums[i])
        #时间复杂度O(n*logn)
        for i in range(k-1,len(nums)):
            m.addNum(nums[i])
            ret.append(m.findMedian())
            # m.popleft()
        return ret
        
if __name__ =='__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]; k = 3
    print('1', s.medianSlidingWindow(nums, k))  # [1,-1,-1,3,5,6]
