'''
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        d = {'[': ']', '(': ')', '{': '}', '?': '?'}
        stack = ['?']
        for e in s:
            if e in d:
                stack.append(e)
            elif d[stack.pop()] != e:
                return False
        return len(stack) == 1


def main():
    text = "{[]}"
    # print('raw datas: {}'.format(text))
    s = Solution()
    print('{} {}'.format(text, s.isValid(text)))
    text = "()[]{}"
    print('{} {}'.format(text, s.isValid(text)))
    text = "(]"
    print('{} {}'.format(text, s.isValid(text)))


if __name__ == '__main__':
    main()
