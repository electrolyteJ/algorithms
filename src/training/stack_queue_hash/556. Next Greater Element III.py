'''
556. 下一个更大元素 III
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
示例 1：
输入：n = 12
输出：21
示例 2：

输入：n = 21
输出：-1

提示：
1 <= n <= 2^31 - 1
'''


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums)-1
        while i-1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            return -1
        j = i
        while j+1 < len(nums) and nums[j+1] > nums[i-1]:
            j += 1
        nums[j], nums[i-1] = nums[i-1], nums[j]
        nums[i:] = nums[i:][::-1]
        ret = int(''.join(nums))
        return ret if ret < (1 << 31) else -1


if __name__ == '__main__':
    s = Solution()
    n = 12
    print('1', s.nextGreaterElement(n))
    n = 21
    print('1', s.nextGreaterElement(n))
    n = 101
    print('1', s.nextGreaterElement(n))
    n = 1234
    print('1', s.nextGreaterElement(n))
    n = 12431  # 13421
    print('1', s.nextGreaterElement(n))
    n = 12413  # 12431
    print('1', s.nextGreaterElement(n))
