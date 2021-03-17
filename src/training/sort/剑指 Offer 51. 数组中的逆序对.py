'''
剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5

限制：

0 <= 数组长度 <= 50000
'''


class Solution:
    def reversePairs(self, nums) -> int:
        #时间复杂度O(nlogn)  空间复杂度O(n)
        def merge_sort(l, r):
            if l >= r:
                return 0
            mid = l+(r-l)//2
            ret = merge_sort(l, mid)+merge_sort(mid+1, r)
            i, j = l, mid+1
            tmp[l:r+1] = nums[l:r+1]
            for k in range(l, r + 1):
                if i == mid+1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r+1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    ret += mid+1-i
            return ret
        n = len(nums)
        tmp = [0]*n
        return merge_sort(0, n-1)


if __name__ == '__main__':
    s = Solution()
    nums = [7, 5, 6, 4]
    print('1', s.reversePairs(nums), nums)
