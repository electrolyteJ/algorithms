'''
438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
'''


class Solution:
    def findAnagrams(self, s: str, p: str):
        left,right =0,0
        import collections
        lookup = collections.defaultdict(int)
        for c in p:
            lookup[c] +=1
        ret,counter = [],0
        while right < len(s):
            lookup[s[right]] -=1
            if lookup[s[right]] <0:
                counter +=1
            right +=1
            while counter > 0:
                if lookup[s[left]]<0:
                    counter -=1
                lookup[s[left]] +=1
                left +=1
            if right-left == len(p):
                ret.append(left)
        return ret
    def findAnagrams2(self, s: str, p: str):
        import collections
        lookup = collections.defaultdict(int)
        for c in p:
            lookup[c] +=1
        l = r = 0
        ret = []
        count=0
        while r < len(s):
            if lookup[s[r]] >0:
                lookup[s[r]] -=1
                count +=1
                r +=1
            else:
                lookup[s[l]] +=1
                count -=1
                l +=1

            if count == len(p):
                ret.append(l)
        return ret


if __name__=='__main__':
    ss = Solution()
    s="cbaebabacd";p="abc"
    print('1',ss.findAnagrams(s,p))
    print('2', ss.findAnagrams2(s, p))
    s="abab";p="ab"
    print('1',ss.findAnagrams(s,p))
    print('2', ss.findAnagrams2(s, p))
