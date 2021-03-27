'''
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

提示：

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
'''


class Solution:
    def minSubArrayLen1(self, target: int, nums) -> int:
        if not nums: return 0
        s, min_len = 0, float('inf')
        left, right = 0, 0
        #O(n)
        while right < len((nums)):
            s += nums[right]
            right += 1
            while s >= target:
                min_len = min(min_len, right - left)
                s -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0

    def minSubArrayLen2(self, target: int, nums) -> int:
        #O(n log(n))二分查找  空间复杂度O(n)
        if not nums: return 0
        import bisect
        min_len=float('inf')
        n = len(nums)
        sums = [0]*(n+1)
        for i in range(n):
            sums[i+1] = sums[i]+nums[i]
        for i in range(1,n+1):
            t = target+sums[i-1]
            bound = bisect.bisect_left(sums,t)
            if bound !=n+1:
                min_len = min(min_len,bound -(i-1))

        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    s = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print('1', s.minSubArrayLen1(target, nums))
    print('2', s.minSubArrayLen2(target, nums))
    target = 4
    nums = [1, 4, 4]
    print('1', s.minSubArrayLen1(target, nums))
    print('2', s.minSubArrayLen2(target, nums))
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print('1', s.minSubArrayLen1(target, nums))
    print('2', s.minSubArrayLen2(target, nums))
    nums = [1, 2, 3, 4, 5]
    target = 15
    print('1', s.minSubArrayLen1(target, nums))
    print('2', s.minSubArrayLen2(target, nums))
