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
        n = len(nums)
        i = n-2
        while i >=0 and nums[i] >= nums[i+1]:#从右往左找最小值,[i+1,n]为下降排序
            i-=1
        if i >=0:
            j = n-1
            while j >= 0 and nums[i] >= nums[j]:  # 找到较大数  3 5 4 2 1 --> 4 5 3 2 1
                j-=1
            nums[i],nums[j] =nums[j],nums[i]
        l,r=i+1,n-1
        while l <r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

if __name__ =='__main__':
    s = Solution()
    nums = [1, 2, 3]
    print('1', s.nextPermutation(nums), nums)
    nums = [3, 2, 1]
    print('1', s.nextPermutation(nums), nums)
    nums = [1, 1, 5]
    print('1', s.nextPermutation(nums), nums)
    nums = [1]
    print('1', s.nextPermutation(nums), nums)
