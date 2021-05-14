'''
139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  #dp
        if not s:return True
        # dp[i] [0,i-1]组成的字符串能否被。。。
        # 时间复杂度O(n*n) 空间复杂度O(n)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:  # memo
        #时间复杂度O(n*n)
        def backtrack(i):
            if i == n:
                return True
            if men[i] is not None:
                return men[i]
            men[i] = False
            for j in range(i,n):
                if s[i:j+1] in wordDict:
                    men[i] = men[i] or backtrack(j+1)
            return men[i]
        n = len(s)
        men=[None]*n
        return backtrack(0)

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:  # memo
        import functools
        @functools.lru_cache(None)
        def backtrack(s, pos):
            if not s:
                return True
            ret = False
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    ret = ret or backtrack(s[i+1:], i+1)
            return ret
        return backtrack(s, 0)


if __name__ == '__main__':
    ss = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print('1', ss.wordBreak(s, wordDict))
    print('2', ss.wordBreak2(s, wordDict))
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print('1', ss.wordBreak(s, wordDict))
    print('2', ss.wordBreak2(s, wordDict))
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print('1', ss.wordBreak(s, wordDict))
    print('2', ss.wordBreak2(s, wordDict))
