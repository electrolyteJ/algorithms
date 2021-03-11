'''
687. 最长同值路径
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
'''
from src.common.tree import create_treenode

class Solution:
    def longestUnivaluePath(self, root) -> int:
        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            if node.left and node.right and node.value == node.right.value and node.value == node.left.value:
                self.max_nodes = max(self.max_nodes, left_height+right_height+1)
                return max(left_height,right_height) +1
            elif node.left and node.value == node.left.value:
                self.max_nodes = max(self.max_nodes, left_height+1)
                return left_height+1
            elif node.right and node.value == node.right.value:
                self.max_nodes = max(self.max_nodes, right_height+1)
                return right_height+1
            else:
                return 1

        self.max_nodes=1
        dfs(root)
        return self.max_nodes-1
if __name__ == '__main__':
    s = Solution()
    root = create_treenode([5, 4, 5, 1, 1, None,5])
    print(root)
    print('1',s.longestUnivaluePath(root))
    root = create_treenode([1, 4, 5, 4, 4, None,5])
    print(root)
    print('1',s.longestUnivaluePath(root))
