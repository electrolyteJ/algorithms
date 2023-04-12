'''
226. 翻转二叉树
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
'''


class Solution:
    def invertTree(self, root):
        if not root:return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

if __name__ =='__main__':
    s = Solution()
    from common.tree import create_treenode
    root = create_treenode([4, 2, 7, 1, 3, 6, 9])
    print(root)
    print('1',s.invertTree(root))
