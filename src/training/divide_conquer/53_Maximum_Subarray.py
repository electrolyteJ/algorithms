'''
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0
示例 4：

输入：nums = [-1]
输出：-1
示例 5：

输入：nums = [-100000]
输出：-100000


提示：

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105


进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
'''
class Status:
    def __init__(self,lsum,rsum,msum,isum):
        self.lsum = lsum# l,r内以l为左端点的最大字段和
        self.rsum = rsum# l,r内以r为右端点的最大子段和
        self.msum = msum# l,r 内最大子段和
        self.isum = isum# l,r区间最和

class Solution:
    def maxSubArray(self, nums) -> int:  # dp
        if not nums: return 0
        n = len(nums)
        dp = [0]*n
        ret = dp[0] = nums[0]
        # dp[i] 下标为i的最大和
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            ret = max(dp[i], ret)
        return ret

    def maxSubArray1(self, nums) -> int:  # dp空间优化
        # if not nums: return 0
        # dp = [0] * 2
        # dp[0], ret = nums[0],nums[0]
        # for i in range(1, len(nums)):
        #     a, b = i % 2, (i - 1) % 2
        #     dp[a] = max(dp[b] + nums[i], nums[i])
        #     ret = max(ret,dp[a])
        # return ret
        if not nums: return 0
        o = p = ret = nums[0]
        for i in range(1, len(nums)):
            p = max(o + nums[i], nums[i])
            ret = max(ret, p)
            o = p
        return ret

    def maxSubArray2(self, nums) -> int:  # 分治法
        if not nums: return 0
        #时间复杂度O(n) 空间复杂度O(logn)  线段树
        def divide(left, right):
            if left >= right:
                return Status(nums[left], nums[left], nums[left], nums[left])
            mid = left + (right-left)//2
            lsub = divide(left, mid)
            rsub = divide(mid+1, right)
            
            isum = lsub.isum+rsub.isum
            lsum = max(lsub.lsum,lsub.isum+rsub.lsum)
            rsum = max(rsub.rsum, lsub.isum+rsub.rsum)
            msum = max(max(lsub.msum,rsub.msum),lsub.rsum+rsub.lsum)
            return Status(lsum, rsum, msum, isum)

        return divide(0, len(nums)-1).msum
         
if __name__ == '__main__':
    s=Solution()
    nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print('0', s.maxSubArray(nums))
    print('1', s.maxSubArray1(nums))
    print('2', s.maxSubArray2(nums))
    nums=[1]
    print('0', s.maxSubArray(nums))
    print('1', s.maxSubArray1(nums))
    print('2', s.maxSubArray2(nums))
    nums=[0]
    print('0', s.maxSubArray(nums))
    print('1', s.maxSubArray1(nums))
    print('2', s.maxSubArray2(nums))
    nums=[-1]
    print('0', s.maxSubArray(nums))
    print('1', s.maxSubArray1(nums))
    print('2', s.maxSubArray2(nums))
