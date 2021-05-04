'''
剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
示例 1:
输入: [10,2]
输出: "102"
示例 2:
输入: [3,30,34,5,9]
输出: "3033459"
提示:
0 < nums.length <= 100
说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
'''
import functools
class Solution:
    def minNumber(self, nums) -> str:
        def sort_rule(x, y):
            a, b = x+y, y+x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return '0' if strs[0] == '0' else ''.join(strs)

    def minNumber2(self, nums) -> str:
        #时间复杂度O(n logn) 空间复杂度O(n) 
        def quick_sort(strs, l, r):
            if l >= r:
                return
            i, j = l, r
            pivot = strs[l]
            while i < j:
                #x+y>y+x 则x>y
                while i < j and strs[j]+pivot >= pivot+strs[j]:
                    j -= 1
                #x+y<y+x x<y
                while i < j and strs[i] + pivot <= pivot + strs[i]:
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(strs, l, i-1)
            quick_sort(strs, i+1, r)
        strs = [str(num) for num in nums]
        quick_sort(strs, 0, len(strs)-1)
        return '0' if strs[0] == '0' else ''.join(strs)


if __name__ == '__main__':
    s = Solution()
    nums = [10, 2]
    print('1', s.minNumber(nums))
    print('2', s.minNumber2(nums))
    nums = [3, 30, 34, 5, 9]
    print('1', s.minNumber(nums))
    print('2', s.minNumber2(nums))
    nums = [0, 0]
    print('1', s.minNumber(nums))
    print('2', s.minNumber2(nums))
