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
'''
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
'''
import math
class Solution:
    #但是在异号的整数运算中，C和Java都尽可能让商大(例如-12 mod 5中，d=-2,r=-2)。而Python则是让商尽可能小(比如-12 mod 5中，d=-3，r=3)。
    def reverse(self, x: int) -> int: 
        max_int = 2**31-1
        min_int = -pow(2, 31)
        recv = 0
        #时间复杂度O(logx)
        while x:
            pop = x % 10 if x>=0 else x%(-10)
            x = x // 10 if x >= 0 else int(x / 10)  # python负数向上取整，正数向下取整
            if recv > max_int//10 or (recv == max_int//10 and pop > max_int % 10):
                return 0
            if recv < int(min_int/10) or (recv == int(min_int/10) and pop < min_int % (-10)):
                return 0
            recv = recv*10 + pop
        return recv
        


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
