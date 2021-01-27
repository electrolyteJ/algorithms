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


class Solution:
    def maxSlidingWindow1(self, nums, k: int):  # 暴力
        num_size = len(nums)
        window_size = num_size-k+1
        ret = []
        # 时间复杂度为O((num_size-k+1)k)=O(num_sizek),超出时间会被停止
        for i in range(0, window_size):
            window = nums[i:i+k]
            # print(window)
            max = window[0]
            for j in range(0, k):
                if window[j] > max:
                    max = window[j]
            ret.append(max)
        return ret

    def maxSlidingWindow2(self, nums, k: int):  # 优化
        num_size = len(nums)
        window_size = num_size-k+1
        ret = []
        for i in range(0, window_size):
            window = nums[i:i+k]
            # print(window)
            max = 0
            for j in range(0, k):
                if window[j] > max:
                    max = window[j]
            ret.append(max)
        return ret


def main():

    l = [1, 3, -1, -3, 5, 3, 6, 7]  # [3,3,5,5,6,7]
    k = 3
    s = Solution()
    # print(s.maxSlidingWindow1(l, k))


if __name__ == '__main__':
    main()
