'''
剑指 Offer 22. 链表中倒数第k个节点
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
'''

from common.list import ListNode,create_listnode
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #时间复杂度O(n)
        cur = head
        counter=0
        while cur:
            cur = cur.next
            counter+=1
        cur = head
        while cur and counter !=k:
            cur = cur.next
            counter -=1
        return cur

    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        #时间复杂度O(n) 双指针
        former,latter = head,head
        for _ in range(k):
            former = former.next
        while former:
            former,latter=former.next,latter.next
        return latter
            


if __name__ =='__main__':
    s = Solution()
    head = create_listnode([1,2,3,4,5])
    k=2
    print('1',s.getKthFromEnd(head,k))
    print('2',s.getKthFromEnd2(head,k))
