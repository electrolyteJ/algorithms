'''
145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

from src.common.tree import create_treenode
class Solution:
    def postorderTraversal(self, root):
        if not root:return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) +[root.value]
    def postorderTraversal2(self, root):
        stack =[root]
        ret =[]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.value)
                stack.append(node.left)
                stack.append(node.right)
        return ret[::-1]

if __name__ == '__main__':
    s = Solution()
    root = create_treenode([1, None,2,None,None,3])
    print(root)
    print('1',s.postorderTraversal(root))
    print('2',s.postorderTraversal2(root))
