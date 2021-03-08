'''
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
 
限制：

0 <= 节点个数 <= 1000

注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/
'''

from src.common.tree import create_treenode
class Solution:
    def mirrorTree(self, root):
        #时间复杂度O(n) 空间复杂度O(n)
        if not root:
          return
        root.left,root.right = self.mirrorTree(root.right),self.mirrorTree(root.left)
        return root
            
    def mirrorTree2(self, root):
        if not root :return None
        stack=[root]
        while stack:
            node = stack.pop()
            node.left,node.right = node.right,node.left
            if node.right:
              stack.append(node.right)
            if node.left:
              stack.append(node.left)

        return root
        

if __name__ == '__main__':
    s = Solution()
    root = create_treenode([4, 2, 7, 1, 3, 6, 9])
    print(root)
    print('1', s.mirrorTree(root))
    root = create_treenode([4, 2, 7, 1, 3, 6, 9])
    print('2', s.mirrorTree2(root))
    root = create_treenode([1, 2])
    print(root)
    print('1', s.mirrorTree(root))
    root = create_treenode([1, 2])
    print('2', s.mirrorTree2(root))
