#include <iostream>
#include <stack>
#include <unordered_map>

/**
* 20. 有效的括号
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
*/
class Solution {
public:
    bool isValid(std::string s) {
        std::unordered_map<char, char> map = {{'{', '}'},
                                              {'[', ']'},
                                              {'(', ')'},
                                              {'?', '?'}};
        std::stack<char> stk;
        stk.push('?');
        for (char c: s) {
            if (map.count(c)) {
                stk.push(c);
            } else {
                if (map.at(stk.top()) != c) {
                    return false;
                }
                stk.pop();
            }
        }
        return stk.size() == 1;
    }
};

int main() {
    Solution s;
    std::cout << s.isValid("([)]") << std::endl;
    std::cout << s.isValid("{[]}") << std::endl;
}