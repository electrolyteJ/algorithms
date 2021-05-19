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
    #可以使用归并排序和随机化快排
    def sortArray(self, nums):
        def merge_sort(l, r):
            if l >= r:
                return
            mid = (l+r) >> 1
            merge_sort(l, mid)
            merge_sort(mid+1, r)

            i, j = l, mid+1
            tmp[l:r+1] = nums[l:r+1]
            for k in range(l, r+1):
                if i == mid+1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r+1:
                    nums[k] = tmp[i]
                    i += 1
                elif tmp[i] >= tmp[j]:
                    nums[k] = tmp[j]
                    j += 1
                else:
                    nums[k] = tmp[i]
                    i += 1

        n = len(nums)
        tmp = [0]*n
        merge_sort(0, n-1)
        return nums
