'''
61. 旋转链表
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''

from src.common.list import ListNode,create_listnode
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        old_tail=head
        n=1
        while old_tail.next:
            old_tail = old_tail.next
            n +=1
        old_tail.next = head
        new_tail=head
        for i in range(n-k%n-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next =None
        return new_head
if __name__ =='__main__':
    s = Solution()
    head = create_listnode([1,2,3,4,5])
    k=2
    print('1',s.rotateRight(head,k))
    head = create_listnode([0,1,2])
    k=4
    print('1',s.rotateRight(head,k))
