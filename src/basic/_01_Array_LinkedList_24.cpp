#include <iostream>
#include "list.h"

/**
 *
 * 24. 两两交换链表中的节点
难度：中等
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4->5, 你应该返回 2->1->4->3->5.
 */
class Solution {
public:
    ListNode *swapPairs(ListNode *head) {
        if (head == nullptr || head) return head;
        return nullptr;
    }
};


int main() {
    std::vector<int> datas = {1, 2, 3, 4, 5};
    ListNode *listnode = create_listnode(datas);
//    std::cout << "raw data ";
//    println(datas);
//    Solution s;
    std::cout << "迭代: ";
    println(listnode);
//    s.swapPairs(listnode);

    return 0;
}