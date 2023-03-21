#include <list.h>
#include <unordered_set>

/**
* 141. 环形链表
难度：简单
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？
*/
class Solution {
public:
    bool hasCycle0(ListNode *head) {
        std::unordered_set<ListNode*> seen;
        while (head){
            if (seen.count(head)){
                return true;
            }
            seen.insert(head);
            head = head->next;
        }

        return false;
    }

    bool hasCycle1(ListNode *head) {
        auto slow = head;
        auto fast = head;
        while (slow && fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;

        }
        return false;
    }
};

int main() {
    try {
        std::vector<int> datas = {1, 2, 3, 4, 5};
        ListNode *listnode = create_listnode(datas);
        print("raw data ", listnode);
        Solution s;
        print("hash: ", s.hasCycle0(listnode));
        listnode = create_listnode(datas);
        print("快慢指针: ", s.hasCycle1(listnode));
    } catch (...) {
    }
    return 0;
}