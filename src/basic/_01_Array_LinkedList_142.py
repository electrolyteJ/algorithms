"""
142. Linked List Cycle II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
"""

from src.common.list import ListNode, create_listnode


class Solution:
    def detectCycle1(self, head: ListNode) -> ListNode:  # hash
        s = set()
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next
        return None

    def detectCycle2(self, head: ListNode) -> ListNode:  # 快慢指针
        #时间复杂度N(n)
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow


def main():
    datas = [1, 2, 3, 4, 5]
    listnode = create_listnode(datas)
    print('{}'.format(listnode))
    s = Solution()
    print('{}'.format(s.detectCycle1(listnode)))
    listnode2 = create_listnode(datas)
    print('{}'.format(s.detectCycle2(listnode2)))


if __name__ == '__main__':
    main()
