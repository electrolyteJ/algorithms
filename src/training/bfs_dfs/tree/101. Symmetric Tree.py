'''
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
'''

from src.common.tree import create_treenode
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root: return False
        import collections
        q = collections.deque([root,root])
        #时间复杂度O(n)
        while q:
            a = q.popleft()
            b = q.popleft()
            if not a and not b:
                continue
            if not a or not b or (a.value !=b.value):
                return False
            q.append(a.left)
            q.append(b.right)

            q.append(a.right)
            q.append(b.left)
        return True
    def isSymmetric2(self, root) -> bool:
        if not root:return False
        def dfs(lnode,rnode):
            if not lnode and rnode:return False
            if not rnode and lnode:return False
            if not lnode and not rnode:return True
            return (lnode.value == rnode.value) and dfs(lnode.left, rnode.right) and dfs(lnode.right, rnode.left)
        return dfs(root.left,root.right)
if __name__ =='__main__':
    s =Solution()
    root = create_treenode([1, 2, 2, 3, 4, 4, 3])
    print(root)
    print('1',s.isSymmetric(root))
    print('2',s.isSymmetric2(root))
    root = create_treenode([1, 2, 2, None, 3, None, 3])
    print(root)
    print('1',s.isSymmetric(root))
    root = create_treenode([1, 2])
    print(root)
    print('1',s.isSymmetric(root))
    root = create_treenode(
        [2, 3, 3, 4, 5, 5, 4, None, None, 8, 9, None, None, 9, 8])
    print(root)
    print('1',s.isSymmetric(root))
