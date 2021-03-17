'''
315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

提示：

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

'''
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        ret =[]
        #时间复杂度O(n*logn)快排
        def quick(left,right):
            pivot=nums[left]
            i,j=left,right
            while i < j:
                while i<j and nums[i] <pivot:
                    left+=1
                while i<j and nums[j] <pivot:
                    right-=1
        quick(0,n-1)
        return ret

if __name__ == '__main__':
    s = Solution()
    nums = [5, 2, 6, 1]
    print('1',s.countSmaller(nums))
