'''
83. 删除排序链表中的重复元素
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。
示例 1：
输入：head = [1,1,2]
输出：[1,2]
示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]
提示：
链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列
'''
from common.list import create_listnode,ListNode
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return
        cur=head
        while cur and cur.next:
            if cur.value == cur.next.value:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

if __name__ =='__main__':
    s = Solution()
    head = create_listnode([1,1,2])
    print('1',s.deleteDuplicates(head))
    head = create_listnode([1, 1, 2, 3, 3])
    print('1',s.deleteDuplicates(head))
