'''
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。
'''
from src.common.tree import create_treenode
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        '''
        树的路径为经过的节点数-1
        '''
        def dfs(root):
            if not root:return 0
            l_height = dfs(root.left)
            r_height = dfs(root.right)
            self.max_ret = max(self.max_ret,r_height+l_height+1)
            return max(l_height,r_height)+1

        self.max_ret = 1#最大节点数
        dfs(root)
        return self.max_ret-1
    def diameterOfBinaryTree2(self, root) -> int:
        diameter = 0
        def height(node):
            if not node:
                return 0
            nonlocal diameter
            lheight = height(node.left)
            rheight = height(node.right)
            diameter = max(lheight+rheight, diameter)
            return max(lheight, rheight)+1
        height(root)
        return diameter

if __name__ == '__main__':
    s =Solution()
    root = create_treenode([1,2,3,4,5])
    print(root)
    print('1',s.diameterOfBinaryTree(root))
    print('2',s.diameterOfBinaryTree2(root))
