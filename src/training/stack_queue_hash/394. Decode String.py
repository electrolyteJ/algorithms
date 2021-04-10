'''
394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
'''


class Solution:
    def decodeString1(self, s: str) -> str:
        stack, k = [], 0
        ret = ''
        # 时间复杂度O(n) 空间复杂度O(n)
        for c in s:
            if c == '[':
                stack.append([k, ret])
                ret, k = '', 0
            elif c == ']':
                cur_k, last_ret = stack.pop()
                ret = last_ret + cur_k*ret
            elif '0' <= c <= '9':
                k = k*10 + int(c)
            else:
                ret += c
        return ret

    def decodeString2(self, s: str) -> str:
        def dfs(s, i):
            ret, k = '', 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    k = k * 10+int(s[i])
                elif s[i] == '[':
                    last_ret, i = dfs(s, i+1)
                    ret += k*last_ret
                    k = 0
                elif s[i] == ']':
                    return ret, i
                else:
                    ret += s[i]
                i += 1
            return ret
        return dfs(s, 0)


if __name__ == '__main__':
    ss = Solution()
    s = "3[a]2[bc]"
    print('1', ss.decodeString1(s))
    print('2', ss.decodeString2(s))
    s = "3[a2[c]]"
    print('1', ss.decodeString1(s))
    print('2', ss.decodeString2(s))
    s = "2[abc]3[cd]ef"
    print('1', ss.decodeString1(s))
    print('2', ss.decodeString2(s))
    s = "abc3[cd]xyz"
    print('1', ss.decodeString1(s))
    print('2', ss.decodeString2(s))
    s = ''
    print('1', ss.decodeString1(s))
    print('2', ss.decodeString2(s))
