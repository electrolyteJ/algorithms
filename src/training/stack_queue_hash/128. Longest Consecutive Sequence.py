'''
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

提示：

0 <= nums.length <= 104
-109 <= nums[i] <= 109
'''
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for num in nums:
            if num-1 in s:continue
            cur_len = 1
            cur_num = num+1
            while cur_num in s:
                cur_num += 1
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len

if __name__ == '__main__':
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print('1', s.longestConsecutive(nums))
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print('1', s.longestConsecutive(nums))
    nums = [1, 2, 0, 1]
    print('1', s.longestConsecutive(nums))
