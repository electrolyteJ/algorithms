'''
493. 翻转对
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。
'''

from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            if l >= r:return 0
            mid = l+(r-l)//2
            ret = merge_sort(l, mid)+merge_sort(mid+1, r)
            i, j = l, mid+1
            tmp[l:r+1] = nums[l:r+1]
            while i<mid+1 and j<r+1:
                if tmp[i] > 2*tmp[j]:
                    ret += mid+1-i
                    j+=1
                else:
                    i+=1
            
            i, j = l, mid+1
            for k in range(l, r+1):
                if i == mid+1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r+1:
                    nums[k] = tmp[i]
                    i += 1
                elif tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
            return ret
        tmp = [0]*len(nums)
        return merge_sort(0, len(nums)-1)

if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 2, 3, 1]
    print('1', s.reversePairs(nums), nums)
    nums = [2, 4, 3, 5, 1]
    print('1', s.reversePairs(nums), nums)
