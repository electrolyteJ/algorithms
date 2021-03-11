'''
7. 整数反转
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
 

提示：

-231 <= x <= 231 - 1
'''


class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31-1
        min_int = -pow(2, 31)
        recv = 0
        absx =abs(x)
        #时间复杂度O(logx)
        while absx:
            pop = absx % 10
            absx //= 10
            if recv > max_int//10 or (recv == max_int//10 and pop > max_int % 10):
                return 0
            if recv < min_int//10 or (recv == min_int//10 and pop < min_int % 10):
                return 0
            recv = recv*10 + pop
        return recv if x >0 else -recv
        


if __name__ == '__main__':
    s =Solution()
    x = 123
    print('1',s.reverse(x))
    x = -123
    print('1',s.reverse(x))
    x = 120
    print('1',s.reverse(x))
    x=0
    print('1',s.reverse(x))
    x = 1534236469
    print('1',s.reverse(x))
