'''
239. 滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例 1：

输入：nums = [1,3,-1,-3, 5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
示例 3：

输入：nums = [1,-1], k = 1
输出：[1,-1]
示例 4：

输入：nums = [9,11], k = 2
输出：[11]
示例 5：

输入：nums = [4,-2], k = 2
输出：[4]


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

import heapq

import time


class Solution:
    def maxSlidingWindow1(self, nums, k: int):  # 暴力
        n = len(nums)
        window_size = n-k+1
        ret = []
        # 时间复杂度为O((n-k+1)k)=O(nk),由于数据流巨大，所以nk值会导致超出时间会被停止
        for i in range(0, window_size):
            window = nums[i:i+k]
            # print(window)
            max = window[0]
            for j in range(0, k):
                if window[j] > max:
                    max = window[j]
            ret.append(max)
        return ret

    def maxSlidingWindow2(self, nums, k: int):  # 大顶推
        if not nums or k == 0:
            return None
        q = [(-nums[i], i) for i in range(0, k)]
        heapq.heapify(q)
        ret = []
        ret.append(-q[0][0])
        # O(nlog k)
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i-k:  # 通过i-k算出滑动窗口的左边界index，而处于maxheap的顶部值的index不能在边界之外
                heapq.heappop(q)
            ret.append(-q[0][0])
        return ret

    def maxSlidingWindow3(self, nums, k: int):  # 队列 dequeue
        if not nums:
            return []
        window, res = [], []
        # 时间复杂度O(n) 空间复杂度O(k)
        for i, x in enumerate(nums):
            # 强制要求滑动窗口左边界的index必须大于window的头index，保证window内部的index都是处于滑动窗口的可用范围
            if i >= k and window[0] <= i-k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k-1:  # 大于滑动窗口的size之后才append
                # print(window[0])
                res.append(nums[window[0]])
        return res


def main():

    s = Solution()
    l = [1, 3, -1, -3, 5, 3, 6, 7]  # [3,3,5,5,6,7]
    k = 3
    print('data stream:', l, k)
    print('max sli:', s.maxSlidingWindow3(l, k))
    print('\n')
    l = [1, -1]  # [1,-1]
    k = 1
    print('data stream:', l, k)
    print('max sli:', s.maxSlidingWindow2(l, k))
    print('\n')
    l = [7, 2, 4]  # [7,4]
    k = 2
    print('data stream:', l, k)
    print('max sli:', s.maxSlidingWindow3(l, k))
    print('\n')


if __name__ == '__main__':
    main()
