"""
    [对各种树形结构的总结](https://warmgrid.github.io/2019/06/14/about-trees.html)
    树的种类：
        - 二叉树(binary tree)：一个节点最多只包含子节点
        - 满二叉树(full binary tree)
        - 完全二叉树(complete binary tree)：堆一般都使用完全二叉树实现
        - 平衡二叉树：当树有 N 个节点时, 高度不超过 O(log N), 例如 AVL 树, 红黑树
        - 二叉搜索树(BST)：当前节点的左子树只包含小于该节点的节点；当前节点的右子树只包含大于该节点的节点
        - Huffman tree:要么没有子节点要么有两个子节点
    存储形式:
        - 顺序存储结构
        - 链式存储结构
    traversals
        - 深度优先(dfs,Depth First Search)
            - 前序遍历preorder
            - 中序遍历inorder
            - 后序遍历postorder
        - 广度优先(bfs, Breadth First Search)
            - 层次遍历levelorder
"""


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def __str__(self):
        return '%s' % inorder(self)

    def add(self, v):
        if not self.value:
            return

        if v < self.value:
            if self.left is None:
                self.left = TreeNode(v)
            else:
                self.left.add(v)
        elif v > self.value:
            if self.right is None:
                self.right = TreeNode(v)
            else:
                self.right.add(v)
        else:
            self.value = v

    def toArray(self):
        pass


def create_treenode(data):
    if not data:
        return None
    tree_node = TreeNode(data[0])
    for i, e in enumerate(data[1:]):
        tree_node.add(e)
    return tree_node


def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


def levelorder(root):
    pass


if __name__ == '__main__':
    # datas = [1, 2, 5, 3,4]
    # treeNode = TreeNode.create(datas)
    # print('%s' % treeNode)
    print('%s' % create_treenode([5, 1, 4, None, None, 3, 6]))
    l = [0,  # idnex:0 num：2^0
         1, 2,  # idnex:2 num：2^1
         3, 4, 5, 6,  # idnex:6 num:2^2
         7, 8, 9, 10, 11, 12, 13, 14,  # idnex:14 num:2^3
         15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30  # idnex:30 num:2^4
         ]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # print(preorder(root))
    # print(inorder(root))
    # print(postorder(root))
