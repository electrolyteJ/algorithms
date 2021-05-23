'''
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？
示例 1：
输入：nums = [1,2,0]
输出：3
示例 2：
输入：nums = [3,4,-1,1]
输出：2
示例 3：
输入：nums = [7,8,9,11,12]
输出：1
提示：
0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
'''
class Solution:
    def firstMissingPositive(self, nums) -> int:  # 标记法
        # 哈希表 时间复杂度O(n)  空降复杂度O(1)
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num-1] = -abs(nums[num-1])
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1

    def firstMissingPositive2(self, nums) -> int:
        if not nums:return []
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        s = set(nums)
        for i in range(1, n+1):
            if i not in s:
                return i
        return n+1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 0]
    print('1', s.firstMissingPositive(nums))
    nums = [1, 2, 0]
    print('2', s.firstMissingPositive2(nums))
    nums = [3, 4, -1, 1]
    print('1', s.firstMissingPositive(nums))
    nums = [3, 4, -1, 1]
    print('2', s.firstMissingPositive2(nums))
    nums = [7, 8, 9, 11, 12]
    print('1', s.firstMissingPositive(nums))
    nums = [7, 8, 9, 11, 12]
    print('2', s.firstMissingPositive2(nums))
    nums = [3, 4, -1, 1, 9, -5]
    print('1', s.firstMissingPositive(nums))
