#include <list.h>

/**
* 206. 反转链表
难度：简单
反转一个单链表。

示例:

输入: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
输出: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
*/

class Solution {
public:
    ListNode *reverseList0(ListNode *head) {
        ListNode* pre = nullptr;
        ListNode* cur = head;
        while(cur){
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }

    ListNode *reverseList1(ListNode *head) {
        if (!head || !head->next) return head;
        ListNode* l = reverseList1(head->next);
        head->next->next = head;
        head->next = nullptr;
        return l;
    }
};

int main() {
    try {
        std::vector<int> datas = {1, 2, 3, 4, 5};
        ListNode *listnode = create_listnode(datas);
        print("raw data ", listnode);
        Solution s;
        print("迭代: ", s.reverseList0(listnode));
        listnode = create_listnode(datas);
        print("递归: ", s.reverseList1(listnode));
    } catch (...) {
    }
    return 0;
}