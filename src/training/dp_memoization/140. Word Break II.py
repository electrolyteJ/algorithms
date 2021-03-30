'''
140. 单词拆分 II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 时间复杂度O(n*2^n)
        def backtrack(i):
            if i == n:
                return [[]]
            ret = []
            #pine apple pen apple
            #apple pen apple ; applepen apple
            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    tail_words = backtrack(j+1)
                    for w in tail_words:
                        ret.append([s[i:j+1]] + w)
            return ret
        n = len(s)
        r = backtrack(0)
        return [' '.join(ws) for ws in r]


if __name__ == '__main__':
    ss = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print('1', ss.wordBreak(s, wordDict))
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print('1', ss.wordBreak(s, wordDict))
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print('1', ss.wordBreak(s, wordDict))
