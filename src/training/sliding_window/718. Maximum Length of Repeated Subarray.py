'''
718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
示例：
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
提示：
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''
from typing import List
class Solution:
    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:#dp
        #dp[i][j] a[:i]与b[:j]存在公共子数组的大小  if nums1[i-1] == nums2[j-1] dp[i][j] =max(dp[i-1][j-1]+1,dp[i][j])
        n1,n2=len(nums1),len(nums2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        # dp[0][0]=1
        ret =0
        #时间复杂度O(n1*n2) 空间复杂度O(n1*n2)
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    ret = max(ret,dp[i][j])
        return ret
    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:#sliding window
        n1, n2 = len(nums1), len(nums2)
        def maxLenght(addA,addB,length):
            ret = counter =0
            for i in range(length):
                if nums1[addA+i] == nums2[addB+i]:
                    counter += 1
                    ret = max(ret, counter)
                else:
                    counter = 0
            return ret
        ret = 0
        #时间复杂度O((n1+n2)* min(n1,n2))
        for i in range(n1):
            length = min(n1-i,n2)
            ret = max(ret,maxLenght(i, 0, length))
        for i in range(n2):
            length = min(n1,n2-i)
            ret = max(ret, maxLenght(0,i, length))
        return ret
    def findLength3(self, nums1: List[int], nums2: List[int]) -> int:#bisect
        pass
if __name__ =='__main__':
    s = Solution()
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    print('1',s.findLength1(nums1, nums2))
    print('2',s.findLength2(nums1, nums2))
    print('3',s.findLength3(nums1, nums2))
