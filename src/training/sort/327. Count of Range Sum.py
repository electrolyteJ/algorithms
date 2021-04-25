'''
327. 区间和的个数
给定一个整数数组 nums 。区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

请你以下标 i （0 <= i <= nums.length ）为起点，元素个数逐次递增，计算子数组内的元素和。

当元素和落在范围 [lower, upper] （包含 lower 和 upper）之内时，记录子数组当前最末元素下标 j ，记作 有效 区间和 S(i, j) 。

求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 有效 区间和的个数。

注意：
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例：

输入：nums = [-2,5,-1], lower = -2, upper = 2,
输出：3 
解释：
下标 i = 0 时，子数组 [-2]、[-2,5]、[-2,5,-1]，对应元素和分别为 -2、3、2 ；其中 -2 和 2 落在范围 [lower = -2, upper = 2] 之间，因此记录有效区间和 S(0,0)，S(0,2) 。
下标 i = 1 时，子数组 [5]、[5,-1] ，元素和 5、4 ；没有满足题意的有效区间和。
下标 i = 2 时，子数组 [-1] ，元素和 -1 ；记录有效区间和 S(2,2) 。
故，共有 3 个有效区间和。
 

提示：

0 <= nums.length <= 10^4
'''
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            mid = l+(r-l)//2
            ret = merge_sort(l, mid)+merge_sort(mid+1, r)
            i, j = l, mid+1
            tmp[l:r+1] = prefix_sum[l:r+1]
            a, b, c = l, mid+1, mid+1
            while a <= mid:
                while b <= r and tmp[b]-tmp[a] < lower:
                    b += 1
                while c <= r and tmp[c]-tmp[a] <= upper:
                    c += 1
                ret += c-b
                a += 1
            for k in range(l, r+1):
                if i == mid+1:
                    prefix_sum[k] = tmp[j]
                    j += 1
                elif j == r+1:
                    prefix_sum[k] = tmp[i]
                    i += 1
                elif tmp[i] <= tmp[j]:
                    prefix_sum[k] = tmp[i]
                    i += 1
                else:
                    prefix_sum[k] = tmp[j]
                    j += 1
            return ret
        n = len(nums)
        prefix_sum=[0]*(n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i]+nums[i]
        tmp = [0]*len(prefix_sum)
        return merge_sort(0, len(prefix_sum)-1)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 5, -1]
    print('1', s.countRangeSum(nums, -2, 2), nums)
