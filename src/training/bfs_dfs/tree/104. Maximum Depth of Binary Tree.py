'''
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''
from common.tree import create_treenode
class Solution:
    def maxDepth_bfs(self, root) -> int:
        if not root:return 0
        import collections
        q = collections.deque([root])
        max_depth=0
        #时间复杂度O(n)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            max_depth +=1
        return max_depth
    def maxDepth_dfs(self, root) -> int:
        if not root: return 0
        return max(self.maxDepth_dfs(root.left), self.maxDepth_dfs(root.right))+1


if __name__ == '__main__':
    s  = Solution()
    root = create_treenode([3, 9, 20, None, None, 15, 7])
    print('bfs',s.maxDepth_bfs(root))
    print('dfs',s.maxDepth_dfs(root))
    root = create_treenode([3])
    print('bfs',s.maxDepth_bfs(root))
    print('dfs',s.maxDepth_dfs(root))
