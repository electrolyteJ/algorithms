'''
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
'''

class Solution:
    def swap(self,nums,a,b):
        nums[a],nums[b] = nums[b],nums[a]
    def quick_sort(self,nums,start,end):
        if start >=end:
            return
        pivot = nums[start]
        l = start+1
        r = end
        while l <=r:
            if nums[l] < pivot:
                l+=1
                continue
            if nums[r] >=pivot:
                r -=1
                continue
            self.swap(nums,l,r)
        self.swap(nums,start,r)
        self.quick_sort(nums,start,r-1)
        self.quick_sort(nums,r+1,end)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums,0,len(nums)-1)
        return nums
