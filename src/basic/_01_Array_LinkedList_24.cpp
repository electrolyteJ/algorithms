#include <iostream>
#include "list.h"

/**
 *
 * 24. 两两交换链表中的节点
难度：中等
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4->5->nullptr, 你应该返回 2->1->4->3->5->nullptr.
 */
class Solution {
public:
    ListNode *swapPairs(ListNode *head) {
        auto *dummy_head = new ListNode();
        dummy_head->next = head;
        auto p = dummy_head;
        //nullptr->1->2
        while (p->next != nullptr && p->next->next != nullptr) {
            auto node1 = p->next;
            auto node2 = p->next->next;
            node1->next = node2->next;
            node2->next = node1;
            p->next = node2;
            p = node1;
        }
        return dummy_head->next;
    }

    ListNode *swapPairs1(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return head;
        auto node1 = head;
        auto node2 = head->next;
        auto node = swapPairs1(node2->next);
        node1->next = node;
        node2->next = node1;
        return node2;
    }
};


int main() {
    try {
        std::vector<int> datas = {1, 2, 3, 4, 5};
        ListNode *listnode = create_listnode(datas);
        print("raw data ", listnode);
        Solution s;
        print("迭代: ", s.swapPairs(listnode));
        listnode = create_listnode(datas);
        print("递归: ", s.swapPairs1(listnode));
    } catch (...) {
    }
    return 0;
}