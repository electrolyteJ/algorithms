'''
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2


进阶：

尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
'''
import collections


class Solution:

    def majorityElement1(self, nums) -> int:  # 暴力
        max_value=0
        majority_e=0
        #O(n^2)
        for i in range(len(nums)):
            e1= nums[i]
            counter=1
            for j in range(i+1,len(nums)):
                e2=nums[j]
                if e1 ==e2:
                    counter +=1
            if counter > max_value:
                max_value = counter
                majority_e=e1
        return majority_e
    def majorityElement2(self, nums) -> int:
        # 时间复杂度O(n) 空间复杂度O(n)
        # counts = collections.Counter(nums)
        counts = dict()
        for e in nums:
            counts[e] = counts.get(e, 0) + 1
        # return max(counts.keys(), key=counts.get)
        return max(counts.keys(), key=counts.get)

    def majorityElement3(self, nums) -> int:
        # 时间复杂度O(nlog n) 空间复杂度O(log n)
        new_nums = sorted(nums)
        return new_nums[len(nums)//2]

    def majorityElement4(self, nums) -> int:#分治
        def majority_e_rec(lo,hi):
            if lo==hi :
                return nums[lo]
            mid = (hi-lo)//2+lo
            left = majority_e_rec(lo,mid)
            right = majority_e_rec(mid+1,hi)
            if left == right:
                return left
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo,hi+1) if nums[i] == right)
            return left if left_count > right_count else right

        #O(nlogn)
        return majority_e_rec(0,len(nums)-1)

if __name__ == "__main__":
    s = Solution()
    l = [3, 2, 3]
    print('1', s.majorityElement1(l))
    print('2', s.majorityElement2(l))
    print('3', s.majorityElement3(l))
    print('4', s.majorityElement4(l))
    l = [2, 2, 1, 1, 1, 2, 2]
    print('1', s.majorityElement1(l))
    print('2', s.majorityElement2(l))
    print('3', s.majorityElement3(l))
    print('4', s.majorityElement4(l))
