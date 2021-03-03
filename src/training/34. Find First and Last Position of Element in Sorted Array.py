'''
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
'''
class Solution:
    def searchRange(self, nums, target: int):
        def search(nums,target,high):
            left,right =0,len(nums)-1
            while left <= right:
                # mid = (right +left)//2
                mid = left +(right-left)//2
                if nums[mid] < target or (high and nums[mid] <= target):
                    left = mid+1
                else:
                    right = mid-1
            return left
        left_i = search(nums,target,False)
        right_i = search(nums,target,True)-1
        if left_i <= right_i and right_i < len(nums) and nums[left_i] ==target and nums[right_i] ==target:
            return [left_i,right_i]
        return [-1,-1]
                    
                
if __name__ =='__main__':
    s = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print('1',s.searchRange(nums,target))
    nums = [5,7,7,8,8,10]
    target = 6
    print('1',s.searchRange(nums,target))
    nums = [] 
    target = 0
    print('1',s.searchRange(nums,target))
    nums = [1]
    target =1
    print('1',s.searchRange(nums,target))
    nums =[1,2,2]
    target = 2
    print('1',s.searchRange(nums,target))