/**
 * 25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 */

#include <vector>
#include "list.h"

class Solution {
public:
    pair<ListNode*,ListNode*> reverse(ListNode* head,ListNode* tail){
        auto pre = tail->next;
        auto  p = head;
        while (pre != tail){
            auto next = p->next;
            p->next= pre;
            pre = p;
            p = next;
        }
        return {tail,head};

    }
    ListNode *reverseKGroup(ListNode *head, int k) {
        auto  hair = new ListNode(0);
        hair->next = head;
        auto pre = hair;
        while (head){
            auto tail = pre;
            for (int i=0;i<k;++i){
                tail = tail->next;
                if (!tail) return hair->next;
            }
            auto next = tail->next;
            pair<ListNode*,ListNode*> p = reverse(head,tail);
            head = p.first;
            tail = p.second;
            pre->next = head;
            tail->next = next;
            pre = tail;
            head = tail->next;

        }

        return hair->next;
    }
};

int main() {
    vector<int> datas = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    auto listnode = create_listnode(datas);
    print("raw datas: ", listnode);
    auto s = Solution();
    print("k =2 ", s.reverseKGroup(listnode, 2));
    listnode = create_listnode(datas);
    print("k = 3 ", s.reverseKGroup(listnode, 3));
}
