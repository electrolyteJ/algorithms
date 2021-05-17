'''
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
提示：

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
'''
class Solution:
    def myPow1(self, x: float, n: int) -> float:
        # O(log n)
        if not n:
            return 1
        if n < 0:
            return 1/self.myPow1(x, -n)
        if n % 2:  # n为奇数
            return self.myPow1(x, n-1)*x
        return self.myPow1(x*x, n//2)

    def myPow2(self, x: float, n: int) -> float:
        # O(logn)
        if n < 0:
            x = 1/x
            n = -n
        pow = 1
        while n:
            if n & 1:  # n为奇数
                pow *= x
            x *= x
            n >>= 1
        return pow


if __name__ == "__main__":
    s = Solution()
    print('1', s.myPow1(2.00000, 20))
    print('2', s.myPow2(2.00000, 20))
    print('1', s.myPow1(2.10000, 3))
    print('2', s.myPow2(2.10000, 3))
    print('1', s.myPow1(2.10000, -2))
    print('2', s.myPow2(2.10000, -2))
