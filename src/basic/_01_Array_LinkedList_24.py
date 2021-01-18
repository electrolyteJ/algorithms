'''
24. 两两交换链表中的节点
难度：中等
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4->5, 你应该返回 2->1->4->3->5.
'''

from mock.ListNode import ListNode


class Solution:
    def swapPairs0(self, head: ListNode) -> ListNode:  # 迭代
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next

    def swapPairs1(self, head: ListNode) -> ListNode:  # 递归
        if head is None or head.next is None:
            return head
        tmp = head.next
        head.next = head

        # head.next.next = head

        return head
        # self.swapPairs1()


def main():
    datas = [1, 2, 3, 4, 5]
    listnode = ListNode.create(datas)
    print('raw datas--->{}'.format(listnode))
    s = Solution()
    print('迭代--->{}'.format(s.swapPairs0(listnode)))
    listnode2 = ListNode.create(datas)
    print('递归--->{}'.format(s.swapPairs1(listnode2)))


if __name__ == '__main__':
    main()
