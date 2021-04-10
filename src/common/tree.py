"""
    [对各种树形结构的总结](https://warmgrid.github.io/2019/06/14/about-trees.html)
    树的种类：
        - 二叉树(binary tree)：一个节点最多只包含两个子节点
        - 满二叉树(full binary tree)
        - 完全二叉树(complete binary tree)：堆一般都使用完全二叉树实现
        - 平衡二叉树：当树有 N 个节点时, 高度不超过 O(log N), 例如 AVL 树, 红黑树
        - 二叉搜索树(BST)：当前节点的左子树只包含小于该节点的节点；当前节点的右子树只包含大于该节点的节点
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

    树的直径：任意两个节点的路径最大值
    树的叶子节点 高度为0
    树的根节点 深度为0，层级为0
"""

import numbers


def _get_tree_properties(root):
    """Inspect the binary tree and return its properties (e.g. height).

    :param root: Root node of the binary tree.
    :type root: binarytree.Node
    :return: Binary tree properties.
    :rtype: dict
    """
    is_descending = True
    is_ascending = True
    min_node_value = root.value
    max_node_value = root.value
    size = 0
    leaf_count = 0
    min_leaf_depth = 0
    max_leaf_depth = -1
    is_strict = True
    is_complete = True
    current_level = [root]
    non_full_node_seen = False

    while len(current_level) > 0:
        max_leaf_depth += 1
        next_level = []

        for node in current_level:
            size += 1
            val = node.value
            min_node_value = min(val, min_node_value)
            max_node_value = max(val, max_node_value)

            # Node is a leaf.
            if node.left is None and node.right is None:
                if min_leaf_depth == 0:
                    min_leaf_depth = max_leaf_depth
                leaf_count += 1

            if node.left is not None:
                if node.left.value > val:
                    is_descending = False
                elif node.left.val < val:
                    is_ascending = False
                next_level.append(node.left)
                is_complete = not non_full_node_seen
            else:
                non_full_node_seen = True

            if node.right is not None:
                if node.right.value > val:
                    is_descending = False
                elif node.right.val < val:
                    is_ascending = False
                next_level.append(node.right)
                is_complete = not non_full_node_seen
            else:
                non_full_node_seen = True

            # If we see a node with only one child, it is not strict
            is_strict &= (node.left is None) == (node.right is None)

        current_level = next_level

    return {
        'height': max_leaf_depth,
        'size': size,
        'is_max_heap': is_complete and is_descending,
        'is_min_heap': is_complete and is_ascending,
        'is_perfect': leaf_count == 2 ** max_leaf_depth,
        'is_strict': is_strict,
        'is_complete': is_complete,
        'leaf_count': leaf_count,
        'min_node_value': min_node_value,
        'max_node_value': max_node_value,
        'min_leaf_depth': min_leaf_depth,
        'max_leaf_depth': max_leaf_depth,
    }


def _build_tree_string(root, curr_index, index=False, delimiter='-'):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
    else:
        node_repr = str(root.value)

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        _build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        _build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


class Node:

    def __init__(self, value: numbers.Number, left=None, right=None):
        if left and not isinstance(left, Node):
            raise BaseException('left is Node class')
        if right and not isinstance(right, Node):
            raise BaseException('right is Node class')
        self.value = value
        self.left, self.right = left, right

    @property
    def inorder(self):
        ret = []
        stack = []
        node = self
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                ret.append(node)
                node = node.right
        return ret

    @property
    def preorder(self):
        ret = []
        stack = [self]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node)
                stack.append(node.right)
                stack.append(node.left)
        return ret

    @property
    def postorder(self):
        ret = []
        stack = [self]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node)
                stack.append(node.left)
                stack.append(node.right)
        return ret[::-1]  # reverse

    @property
    def levelorder(self):
        '''
         https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search

        '''
        current_level = [self]
        ret = []
        while len(current_level) > 0:
            next_level = []
            for node in current_level:
                ret.append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
        return ret

    @property
    def height(self):
        return _get_tree_properties(self)['height']
    @property
    def max_leaf_depth(self) -> int:
        return _get_tree_properties(self)['max_leaf_depth']
    @property
    def min_leaf_depth(self) -> int:
        return _get_tree_properties(self)['min_leaf_depth']
    def __hash__(self):
        return super().__hash__()

    def __str__(self):
        '''
        Return the pretty-print string for the binary tree.
        '''
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    def __repr__(self):
        '''
        Return the string representation of the current node.

        没有override的__repr__函数返回的是<__main__.Node object at 0x000002007B2751D0>
        '''
        return 'Node({})'.format(self.value)

    def __setattr__(self, attr, obj):
        # if attr == LEFT:
        #     if obj is not None and not isinstance(obj, Node):
        #         raise BaseException('left child must be a Node instance')
        # elif attr == RIGHT:
        #     if obj is not None and not isinstance(obj, Node):
        #         raise BaseException('right child must be a Node instance')
        # elif attr == VALUE:
        #     if not isinstance(obj, numbers.Number):
        #         raise BaseException('node value must be a number')
        #     object.__setattr__(self, VAL, obj)
        # elif attr == VAL:
        #     if not isinstance(obj, numbers.Number):
        #         raise BaseException('node value must be a number')
        #     object.__setattr__(self, VALUE, obj)

        object.__setattr__(self, attr, obj)

    # def __iter__(self):
    #     pass

    # def __len__(self):
    '''
    if node: 受这个函数影响
    '''
    #     pass

    def __getitem__(self, index):
        if not isinstance(index,int) or index <0:
            raise BaseException("index有问题")
        current_level = [self]
        current_index = 0
        has_more_nodes = True
        while has_more_nodes > 0:
            has_more_nodes = False
            next_level = []
            for node in current_level:
                if current_index == index:
                    if node is None:
                        break
                    else:
                        return node
                current_index += 1
                if node is None:
                    next_level.extend([None, None])
                    continue
                next_level.extend([node.left, node.right])
                if node.left or node.right:
                    has_more_nodes = True
            current_level = next_level
        # raise BaseException("没找到")
    def __setitem__(self, index, node):
        if index ==0:
            raise BaseException("index == 0 ")
        parent_index = (index-1)//2
        try:
            parent = self.__getitem__(parent_index)
        except BaseException:
            raise BaseException('haha')
        setattr(parent, 'left' if index % 2 else 'right', node)

    def __delitem__(self, index):
        pass

    # def toArray(self):
    #     pass


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


def recus_levelorder(root, level):
    if root is None:
        return []
    if level == 1:
        return [root.value]
    elif level > 1:
        recus_levelorder(root.left, level-1)
        recus_levelorder(root.right, level-1)


def levelorder(root):
    h = root.height
    ret = []
    for i in range(1, h+1):
        ret += recus_levelorder(root, i)
    return ret


def create_treenode(datas):
    '''
    [0,  #last idnex:0 num：2^0
    1, 2,  #last idnex:2 num：2^1
    3, 4, 5, 6,  #last idnex:6 num:2^2
    7, 8, 9, 10, 11, 12, 13, 14,  # last idnex:14 num:2^3
    # last idnex:30 num:2^4
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
    ]
    '''

    nodes = [None if v is None else Node(v) for v in datas]
    for i in range(1, len(nodes)):
        node = nodes[i]
        if node:
            parent_i = (i-1)//2
            parent = nodes[parent_i]
            if not parent:
                raise BaseException("node not found")
            setattr(parent, 'left' if i % 2 else 'right', node)
    return nodes[0] if nodes else None


if __name__ == '__main__':
    tree_node = create_treenode([5, 1, 4, None, None, 3, 6])
    print('tree:%s' % tree_node)
    print('inorder:%s' % tree_node.inorder)
    print('preorder:%s' % tree_node.preorder)
    print('postorder:%s' % tree_node.postorder)
    print('levelorder:%s' % tree_node.levelorder)
    print(tree_node[2])
    tree_node[2]=create_treenode([5, 1])
    print(tree_node)
