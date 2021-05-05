'''
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
'''
class Solution:
    def isPalindrome1(self, s: str) -> bool:
        #时间复杂度O(n) 空间复杂度O(n)
        stack = []
        for c in s:
            if '0' <= c <= '9' or 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                stack.append(c)
        for c in s:
            if '0' <= c <= '9' or 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                if stack.pop().lower() != c.lower():
                    return False
        return len(stack) == 0
    def isPalindrome2(self, s: str) -> bool:
        left,right=0,len(s)-1
        #时间复杂度O(n)
        while left <right:
            
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1

            if left < right and s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right -=1
        return True

if __name__ == '__main__':
    ss = Solution()
    s = "A man, a plan, a canal: Panama"
    print('1', ss.isPalindrome1(s))
    print('2', ss.isPalindrome2(s))
    s = "race a car"
    print('1', ss.isPalindrome1(s))
    print('2', ss.isPalindrome2(s))
    'c'.isalnum()
    'c'.isalpha()
    'c'.isnumeric()
    'c'.islower()
    'c'.upper()
    'c'.lower()
