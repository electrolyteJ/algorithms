'''
69. x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
'''

import math


class Solution:
    def mySqrt11(self, x: int) -> int:  # 二分法
        if x == 0 or x == 1:
            return x
        left, right = 0, x
        while left <= right:
            mid = (left+right)/2
            if abs(x/mid-mid) < 1e-9:#10^-9
                return mid
            elif mid > x/mid:
                right = mid
            else:
                left = mid
                res = mid
        return res

    def mySqrt1(self, x: int) -> int:  # 二分法
        if x == 0 or x == 1:
            return x
        left, right = 0, x
        while left <= right:
            mid = (left+right)//2
            if mid == x//mid:
                return mid
            elif mid > x//mid:
                right = mid - 1
            else:
                left = mid + 1
                res = mid
        return res

    def mySqrt2(self, x: int) -> int:  # 牛顿迭代法
        r = x 
        while r *r >x:
            r =(r+x/r)/2
        return r


if __name__ == "__main__":
    s = Solution()
    print('1', s.mySqrt1(8))
    print('11', s.mySqrt11(8))
    print('2', s.mySqrt2(4))
