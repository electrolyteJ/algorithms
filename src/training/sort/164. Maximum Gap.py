'''
164. 最大间距
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。
示例 1:
输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
'''
class Solution:
    def maximumGap(self, nums) -> int:#基数排序
        def quick_select(left, right):
            if left >= right:
                return
            pivot = nums[left]
            i, j = left, right
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[left] = nums[left], nums[i]
            quick_select(left, i-1)
            quick_select(i+1, right)
        # 平均时间复杂度为O(nlogn) 空间复杂度O(nlogn) 采用基数排序和桶排序可以达到线性时间 or 空间复杂度
        quick_select(0, len(nums)-1)
        max_ret = 0
        for i in range(1, len(nums)):
            max_ret = max(max_ret, nums[i]-nums[i-1])
        return max_ret

    def maximumGap2(self, nums) -> int:#桶排序
        if not nums or len(nums) < 2:
            return 0
        n = len(nums)
        max_num, min_num = max(nums), min(nums)
        bucket_size = max(1, (max_num-min_num)//(n-1))
        buckets = [[] for _ in range((max_num-min_num)//bucket_size+1)]
        for num in nums:
            buckets[(num-min_num)//bucket_size].append(num)
        pre_max, max_gap = max(buckets[0]), 0
        for i in range(1, len(buckets)):
            if buckets[i]:
                max_gap = max(max_gap, min(buckets[i])-pre_max)
                pre_max = max(buckets[i])
        return max_gap


if __name__ == '__main__':
    s = Solution()
    nums = [3, 6, 9, 1]
    print('1', s.maximumGap(nums), nums)
    print('2', s.maximumGap2(nums))
    nums = [10]
    print('1', s.maximumGap(nums))
    print('2', s.maximumGap2(nums))
