'''
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"
说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 时间复杂度O(n1*n2) 空间复杂度O(n1+n2)
        n1, n2 = len(num1), len(num2)
        ret = [0]*(n1+n2)
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                ret[i+j+1] += int(num1[i]) * int(num2[j])
        for i in range(n1+n2-1, 0, -1):
            ret[i-1] += ret[i]//10
            ret[i] %= 10
        return ''.join(str(x) for x in ret).lstrip('0') or '0'

if __name__ == '__main__':
    s = Solution()
    num1 = "2"
    num2 = "3"
    print('1', s.multiply(num1, num2))
    num1 = "123"
    num2 = "456"
    print('1', s.multiply(num1, num2))
