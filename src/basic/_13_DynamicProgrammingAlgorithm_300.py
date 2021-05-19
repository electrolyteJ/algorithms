'''
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
提示：
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
进阶：你可以设计时间复杂度为 O(n^2) 的解决方案吗？你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''
class Solution:
    def lengthOfLIS1(self, nums) -> int:
        if not nums: return 0
        ret =1
        dp=[1]*len(nums)
        #dp[i] 以第i个数字结尾的最长上升子序列的长度
        #时间复杂度O(n*n)
        for i in range(1,len(nums)):        
            for j in range(0,i):
                if nums[j] <nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
            ret = max(ret,dp[i])
        return ret

    def lengthOfLIS2(self, nums) -> int:  # 贪心+二分
        def bisect_left(a, target):
            l,r = 0,len(a)-1
            while l <= r:
                mid = (r+l) >> 1
                if a[mid] >= target:
                    r = mid-1
                else:
                    l = mid+1
            return l
        ret = []#创建一个数组保证单调性，虽然保存的结果不一定是对的
        for n in nums:
            if not ret or n > ret[-1]:
                ret.append(n)
            else:  # 通过二分查找到目标值在递增数组中的位置
                pos = bisect_left(ret, n)
                ret[pos] = n
        return len(ret)


if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 1]
    print('1', s.lengthOfLIS1(nums))  # 4  [2,3,7,101] or [2, 3, 7, 18]
    print('2', s.lengthOfLIS2(nums))  # 4
    nums = [0, 1, 0, 3, 2, 3]
    print('1', s.lengthOfLIS1(nums))  # 4  [0, 1, 2, 3]
    print('2', s.lengthOfLIS2(nums))  # 4
    nums = [7, 7, 7, 7, 7, 7, 7]
    print('1', s.lengthOfLIS1(nums))  # 1  [7]
    print('2', s.lengthOfLIS2(nums))  # 1 
