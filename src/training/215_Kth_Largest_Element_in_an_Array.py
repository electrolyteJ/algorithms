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
    def findKthLargest2(self, nums, k: int) -> int:
        if not nums:return 0
        def partition(nums,l,r):
            pivot = nums[r]
            i = l-1
            for j in range(l,r):
                if nums[j] < pivot:
                    i +=1
                    nums[i],nums[j] = nums[j],nums[i]
            i +=1
            nums[i],nums[r] = nums[r],nums[i]
            return i
        def quick_select(nums,k_index,l,r):
            p_index = partition(nums,l,r)
            if p_index == k_index:
                return nums[k_index]
            else:
                return quick_select(nums,k_index,l,p_index-1) if p_index > k_index  else quick_select(nums,k_index,p_index+1,r)

        return quick_select(nums,len(nums)-k,0,len(nums)-1)
         
if __name__ == '__main__':
    s = Solution()
    n = [3, 2, 1, 5, 6, 4]
    k= 2
    print('1',s.findKthLargest(n,k))
    n = [3, 2, 1, 5, 6, 4]
    print('2',s.findKthLargest2(n,k))
    n = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print('1',s.findKthLargest(n,k))
    n = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print('2',s.findKthLargest2(n,k))