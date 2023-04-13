'''
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true
 

提示：

树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104
'''
from common.tree import create_treenode

class Solution:
    def isBalanced(self, root) -> bool:
        def height(root):
            if not root:return 0
            nonlocal ret
            left_subtree_height = height(root.left)
            right_subtree_height = height(root.right)
            if abs(left_subtree_height-right_subtree_height) > 1:
                ret = False
            return max(left_subtree_height, right_subtree_height)+1
        ret = True
        height(root)
        return ret
        
if __name__ == '__main__':
    s  = Solution()
    root = [3, 9, 20, None, None, 15, 7]
    print('1', s.isBalanced(create_treenode(root)))
    root = [1, 2, 2, 3, 3, None, None, 4, 4]
    # print(create_treenode(root))
    print('1', s.isBalanced(create_treenode(root)))
    root = []
    print('1', s.isBalanced(create_treenode(root)))
