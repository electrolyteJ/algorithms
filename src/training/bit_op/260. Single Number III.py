'''
260. 只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
示例 1：

输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。
示例 2：

输入：nums = [-1,0]
输出：[-1,0]
示例 3：

输入：nums = [0,1]
输出：[1,0]
提示：

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
除两个只出现一次的整数外，nums 中的其他数字都出现两次
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        import functools
        ret = functools.reduce(lambda x,y:x^y,nums)
        div =1
        while (div & ret) ==0:
            div <<=1
        #div=0的为一组，不为0的为一组
        a,b=0,0
        for num in nums:
            if num & div:
                a ^=num
            else:
                b ^=num
        return [a,b]

                

if __name__ =='__main__':
    s = Solution()
    nums = [1, 2, 1, 3, 2, 5]
    print('1',s.singleNumber(nums))
    nums = [-1, 0]
    print('1',s.singleNumber(nums))
    nums = [0, 1]
    print('1',s.singleNumber(nums))
