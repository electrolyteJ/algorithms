'''
415. 字符串相加
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

提示：

num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1)-1, len(num2)-1
        ret =''
        add=0 
        #时间复杂度O(max(m,n))
        while i>=0 or j>=0 or add !=0:
            x = ord(num1[i]) -ord('0') if i>=0 else 0
            y = ord(num2[j]) -ord('0') if j>=0 else 0
            sum_result = x+y+add
            ret += str(sum_result % 10)
            add =sum_result//10
            i -=1
            j -=1
        return ''.join(reversed(ret))
if __name__=='__main__':
    s = Solution()
    num1 = '12'
    num2 ='342'
    print('1',s.addStrings(num1,num2))
