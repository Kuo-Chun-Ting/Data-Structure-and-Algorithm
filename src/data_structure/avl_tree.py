import re


class AVLTreeNode():
    def __init__(self, key):
        self.key: int = key
        self.left: AVLTreeNode = None
        self.right: AVLTreeNode = None
        self.height = 1


def insert(node: AVLTreeNode, key: int):
    if not node:
        return AVLTreeNode(key)

    if key < node.key:
        node.left = insert(node.left, key)

    elif key > node.key:
        node.right = insert(node.right, key)

    left_child_height = get_height(node.left)
    right_child_height = get_height(node.right)
    max_height = max(left_child_height, right_child_height)
    node.height = 1 + max_height
    balance_factor = get_balance_factor(node)

    if balance_factor > 1:
        if key > node.left.key:
            node.left = left_rotate(node.left)
        return right_rotate(node)

    if balance_factor < -1:
        if key < node.right.key:
            node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


def get_height(node: AVLTreeNode) -> int:
    if not node:
        return 0
    return node.height


def get_balance_factor(node: AVLTreeNode) -> int:
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(node: AVLTreeNode) -> AVLTreeNode:
    if node.right:
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(get_height(node.left), get_height(node.right))
        right_child.height = 1 + \
            max(get_height(right_child.left),get_height(right_child.right))
        return right_child
    return node


def right_rotate(node: AVLTreeNode) -> AVLTreeNode:
    if node.left:
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = 1 + max(get_height(node.left), get_height(node.right))
        left_child.height = 1 + \
            max(get_height(left_child.left), get_height(left_child.right))
        return left_child
    return node


if __name__ == "__main__":
    node = AVLTreeNode(33)
    insert(node, 13)
    insert(node, 53)
    insert(node, 11)
    insert(node, 21)
    insert(node, 61)
    insert(node, 8)
    insert(node, 9)
    print(node.height)
