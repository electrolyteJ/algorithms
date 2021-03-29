'''
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

提示：

0 <= num < 231

'''
class Solution:
    def translateNum(self, num: int) -> int:
        nums = [c for c in str(num)]
        n = len(nums)
        dp = [0]*(n+1)
        dp[0]=dp[1]=1
        #时间复杂度O(n) 空间复杂度O(n)
        for i in range(2, n+1):
            nums_i = i-1
            if nums[nums_i-1] + nums[nums_i] > '25' or nums[nums_i-1] == '0':
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    def translateNum2(self, num: int) -> int:#dp空间优化
        nums = [c for c in str(num)]
        n = len(nums)
        o, p, q = 0, 1, 1
        for i in range(2, n+1):
            nums_i = i-1
            o, p = p, q
            if nums[nums_i-1]+nums[nums_i] > '25' or nums[nums_i-1] == '0':
                q = p
            else:
                q = p+o
        return q

if __name__ == '__main__':
    s = Solution()
    num = 12258
    print('1', s.translateNum(num))
    print('2', s.translateNum2(num))
