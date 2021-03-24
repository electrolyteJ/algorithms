'''
670. 最大交换
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 10^8]
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [n for n in str(num)]
        last = [0]*10#值最大，下标越后
        for i in range(len(nums)):
            last[ord(nums[i])-ord('0')] = i
        #时间复杂度O(n)
        for i in range(len(nums)):
            # 倒着找最大值
            for digit in range(9, ord(nums[i])-ord('0'), -1):
                if last[digit] > i:
                    nums[i], nums[last[digit]] = nums[last[digit]], nums[i]
                    return ''.join(nums)
        return num


if __name__ == '__main__':
    s = Solution()
    num = 2736
    print('1', s.maximumSwap(num))
    num = 9973
    print('1', s.maximumSwap(num))
