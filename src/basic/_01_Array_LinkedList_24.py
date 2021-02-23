"""
24. 两两交换链表中的节点
难度：中等
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4->5, 你应该返回 2->1->4->3->5.
"""

from src.common.list import ListNode, create_listnode


class Solution:
    def swapPairs0(self, head: ListNode) -> ListNode:  # 迭代
        dummyHead = ListNode(-1)
        dummyHead.next = head
        cur_node = dummyHead
        while cur_node.next and cur_node.next.next:
            node1 = cur_node.next
            node2 = cur_node.next.next

            # cur_node.next = node2
            # node1.next = node2.next
            # node2.next = node1
            cur_node.next,node1.next,node2.next = node2,node2.next,node1

            cur_node = node1
        return dummyHead.next

    def swapPairs1(self, head: ListNode) -> ListNode:  # 递归
        if head is None or head.next is None:
            return head
        node1 = head
        node2 = head.next
        node1.next, node2.next = self.swapPairs1(node2.next), node1
        return node2


def main():
    datas = [1, 2, 3, 4, 5]
    listnode = create_listnode(datas)
    print('raw datas:{}'.format(listnode))
    s = Solution()
    print('迭代:{}'.format(s.swapPairs0(listnode)))
    listnode2 = create_listnode(datas)
    print('递归:{}'.format(s.swapPairs1(listnode2)))


if __name__ == '__main__':
    main()
