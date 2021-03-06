'''
103. 二叉树的锯齿形层序遍历
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''

from src.common.tree import create_treenode
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:return []
        #时间复杂度O(n) 空间复杂度O(n
        import collections
        q  = collections.deque([root])
        ret=[]
        level = 0
        while q:
            current_level=collections.deque()
            for i in range(len(q)):
                node = q.popleft()
                if level % 2==0:#偶数
                    current_level.append(node.value)
                else:
                    current_level.appendleft(node.value)

                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(list(current_level))
            level +=1
        return ret

if __name__ =='__main__':
    s = Solution()
    root = create_treenode([3, 9, 20, None, None, 15, 7])
    print('1',s.zigzagLevelOrder(root))
    root=create_treenode([1, 2, 3, 4, None, None, 5])
    print(root)
    print('1', s.zigzagLevelOrder(root))  # [[1],[3,2],[4,5]]

