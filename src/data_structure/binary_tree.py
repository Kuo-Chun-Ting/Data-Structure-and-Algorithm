from typing import List


class BinaryTreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root: BinaryTreeNode, result: List[int] = None):
    if result is None:
        result = []

    if root:
        if root.left:
            inorder(root.left, result)

        result.append(root.val)

        if root.right:
            inorder(root.right, result)

    return result


def preorder(root: BinaryTreeNode, result: List[int] = None):
    if result is None:
        result = []

    if root:
        result.append(root.val)

    if root.left:
        preorder(root.left, result)

    if root.right:
        preorder(root.right, result)

    return result


def postorder(root: BinaryTreeNode, result: List[int] = None):
    if result is None:
        result = []

    if root:
        if root.left:
            postorder(root.left, result)

        if root.right:
            postorder(root.right, result)

        result.append(root.val)

    return result


def is_full(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_full(root.left) and is_full(root.right)

    return False


if __name__ == "__main__":
    node = BinaryTreeNode(1)
    node.left = BinaryTreeNode(2)
    node.right = BinaryTreeNode(3)
    node.left.left = BinaryTreeNode(4)
    node.left.right = BinaryTreeNode(5)

    print("inorder")
    print(inorder(node))
    print("preorder")
    print(preorder(node))
    print("postorder")
    print(postorder(node))
    print("Is it full?")
    print(is_full(node))
