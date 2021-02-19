'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
'''
class Solution:
    def swap(self,nums,a,b):
        nums[a],nums[b]=nums[b],nums[a]
    def quick_select(self,nums,k,start,end):
        if start>=end:
            return
        pivot = nums[start]
        l = start+1
        r = end
        while(l <= r):
            if nums[l] >pivot:
                l +=1
                continue
            if nums[r] <=pivot:
                r -=1
                continue
            self.swap(nums,l,r)
        self.swap(nums,start,r)
        if r-start+1 ==k :
            return
        if r-start+1>k:
            self.quick_select(nums,k,start,r-1)
        else:
            self.quick_select(nums,k-(l-start),r+1,end)

    def findKthLargest(self, nums, k: int) -> int:
        self.quick_select(nums,k,0,len(nums)-1)
        return nums[k-1]
