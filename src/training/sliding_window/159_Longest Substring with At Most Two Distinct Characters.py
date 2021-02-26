'''
159.至多包含两个不同字符的最长子串
给定一个字符串 s ，找出至多包含两个不同字符的最长子串 t 。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
1
2
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct1(self,s):
        if not s : return 0
        left,right = 0,0
        max_len = 0
        import collections
        lookup = collections.defaultdict(int)#只能有两个key
        #时间复杂度O(n)
        while right < len(s):
            lookup[s[right]] +=1
            right +=1
            while len(lookup) > 2:
                lookup[s[left]] -=1
                if lookup[s[left]] == 0:
                    lookup.pop(s[left])
                left +=1
            max_len = max(max_len,right-left)
        return max_len

    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] == 0:
                counter += 1
            lookup[s[end]] += 1
            end +=1
            while counter > 2:
                if lookup[s[start]] == 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len
    def lengthOfLongestSubstringTwoDistinct3(self, s: str) -> int:
        left,ii,max_len=0,-1,0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:continue
            if ii > 0 and s[ii] != s[i]:
                max_len = max(max_len,i-left)
                left =ii+1
            ii =i-1
        return max(len(s)-left,max_len)

if __name__ =='__main__':
    s1 = Solution()
    s="eceba"
    print('1',s1.lengthOfLongestSubstringTwoDistinct1(s))
    print('3',s1.lengthOfLongestSubstringTwoDistinct3(s))
    s = "ccaabbb"
    print('1',s1.lengthOfLongestSubstringTwoDistinct1(s))
    print('3',s1.lengthOfLongestSubstringTwoDistinct3(s))
