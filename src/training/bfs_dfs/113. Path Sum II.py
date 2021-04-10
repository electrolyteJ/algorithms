'''
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
from src.common.tree import create_treenode


class Solution:
    def pathSum_bfs(self, root, targetSum: int):
        if not root:return []
        ret = []
        import collections
        q = collections.deque([(root, root.value, [root.value])])
        while q:
            node, v, ls = q.popleft()
            if not node.left and not node.right and v == targetSum:
                ret.append(ls)
            if node.left:
                q.append((node.left, v+node.left.value, ls+[node.left.value]))
            if node.right:
                q.append((node.right, v+node.right.value, ls+[node.right.value]))
        return ret

    def pathSum_dfs(self, root, targetSum: int):
        if not root:return []
        # 时间复杂度O(n) 空间复杂度O(n)
        def dfs(root, targetSum):
            if not root:
                return
            path.append(root.value)
            targetSum -= root.value
            if not root.left and not root.right and targetSum == 0:
                ret.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()

        ret = []
        path = []
        dfs(root, targetSum)
        return ret


if __name__ == '__main__':
    s = Solution()
    root = create_treenode(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
    print(root)
    ts = 22
    print('1', s.pathSum_bfs(root, ts))
    print('1', s.pathSum_dfs(root, ts))
