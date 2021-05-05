'''
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        n = len(nums)
        ret=float('inf')
        nums.sort()
        #时间复杂度为O(n*n)
        for i in range(n-2):
            if i >=1 and nums[i] ==nums[i-1]:continue
            left,right=i+1,n-1
            while left<right:
                sum_ret = nums[i]+nums[left]+nums[right]
                if abs(sum_ret - target) < abs(ret - target):
                    ret =sum_ret
                if sum_ret < target:
                    left+=1
                elif sum_ret > target:
                    right-=1
                else:
                    return target        
        return ret


if __name__ =='__main__':
    s = Solution()
    nums = [-1, 2, 1, -4]; target = 1
    print('1', s.threeSumClosest(nums,target))
