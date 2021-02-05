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
    def majorityElement1(self, nums) -> int:
        # 时间复杂度O(n) 空间复杂度O(n)
        # counts = collections.Counter(nums)
        counts = dict()
        for e in nums:
            counts[e] = counts.get(e, 0) + 1
        # return max(counts.keys(), key=counts.get)
        return max(counts.keys(), key=counts.get)

    def majorityElement2(self, nums) -> int:
        # 时间复杂度O(nlog n) 空间复杂度O(log n)
        new_nums = sorted(nums)
        return new_nums[len(nums)//2]

    def majorityElement3(self, nums) -> int:
        new_nums = sorted(nums)
        return new_nums[len(nums)//2]


if __name__ == "__main__":
    s = Solution()
    l = [3, 2, 3]
    print('1', s.majorityElement1(l))
    print('2', s.majorityElement2(l))
    print('3', s.majorityElement3(l))
    l = [2, 2, 1, 1, 1, 2, 2]
    print('1', s.majorityElement1(l))
    print('2', s.majorityElement2(l))
    print('3', s.majorityElement3(l))
