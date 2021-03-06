'''
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

from src.common.tree import create_treenode
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.value] + self.inorderTraversal(root.right)
    def inorderTraversal2(self, root):
        stack = []
        node = root
        ret =[]
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                ret.append(node.value)
                node = node.right
        return ret
                
                
         
if __name__ == '__main__':
    s = Solution()
    root = create_treenode([1, None, 2,None,None,3])
    print('1',s.inorderTraversal(root))
    root = create_treenode([])
    print('1',s.inorderTraversal(root))
    root = create_treenode([1, 2])
    print('1',s.inorderTraversal(root))
    root = create_treenode([1])
    print('1',s.inorderTraversal(root))
    root = create_treenode([1, None, 2])
    print('1',s.inorderTraversal(root))
