'''
459. 重复的子字符串
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。
示例 2:
输入: "aba"
输出: False
示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
'''
class Solution:
    def repeatedSubstringPattern1(self, s: str) -> bool:#枚举
        n = len(s)
        #时间复杂度O(n*n)
        for i in range(1,n//2+1):
            if n % i ==0:
                if all(s[j]==s[j-i] for j in range(i,n)):
                    return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:  # 字符串匹配
        # return (s+s).find(s, 1) != len(s) 
        n = len(s)
        return s in (s+s)[1:2*n-1]
    def repeatedSubstringPattern3(self, s: str) -> bool: #kmp算法
        pass
        
if __name__ =='__main__':
    ss = Solution()
    s = "abab"
    print('1', ss.repeatedSubstringPattern1(s))
    print('2', ss.repeatedSubstringPattern2(s))
    print('3', ss.repeatedSubstringPattern3(s))
    s = "aba"
    print('1', ss.repeatedSubstringPattern1(s))
    print('2', ss.repeatedSubstringPattern2(s))
    print('3', ss.repeatedSubstringPattern3(s))
    s = "abcabcabcabc"
    print('1', ss.repeatedSubstringPattern1(s))
    print('2', ss.repeatedSubstringPattern2(s))
    print('3', ss.repeatedSubstringPattern3(s))
    
