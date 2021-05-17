'''
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''
class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        # 时间复杂度O(nlogn)
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = [0]*26
        # O(n)
        for e in s:
            table[ord(e)-ord('a')] += 1
        for e in t:
            table[ord(e)-ord('a')] -= 1
            if table[ord(e)-ord('a')] < 0:
                return False

        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = dict()
        # 时间复杂度O(n) 空间复杂度O(S)
        for e in s:
            table[e] = table.get(e, 0)+1
        for e in t:
            table[e] = table.get(e, 0)-1
            if table[e] < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram1('anagram', 'nagaram'))
    print(s.isAnagram2('anagram', 'nagaram'))
    print(s.isAnagram2('anagram', 'nagaram'))
    print(s.isAnagram3('anagramU+263B', 'nagaramU+263B'))
