'''
31. 下一个排列
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。
示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：
输入：nums = [1]
输出：[1]
提示：
1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
if __name__ =='__main__':
    s = Solution()
    nums = [1, 2, 3]
    print('1',s.nextPermutation(nums))
    nums = [3, 2, 1]
    print('1',s.nextPermutation(nums))
    nums = [1, 1, 5]
    print('1',s.nextPermutation(nums))
    nums = [1]
    print('1',s.nextPermutation(nums))
