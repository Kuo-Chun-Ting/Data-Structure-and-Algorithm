class BinarySearchTreeNode():
    def __init__(self, key):
        self.key: int = key
        self.left: BinarySearchTreeNode = None
        self.right: BinarySearchTreeNode = None


def insert(node: BinarySearchTreeNode, key: int):
    if node is None:
        return BinarySearchTreeNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
        
    return node


def search(node: BinarySearchTreeNode, key: int) -> int:
    if key == node.key:
        return node.key

    if key < node.key:
        if node.left is None:
            return None
        else:
            return search(node.left, key)
    else:
        if node.right is None:
            return None
        else:
            return search(node.right, key)


def delete(node: BinarySearchTreeNode, key: int) -> BinarySearchTreeNode:
    if node is None:
        return None

    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        successor_key = get_min_key(node.right)
        node.key = successor_key
        node.right = delete(node.right, successor_key)
    return node


def get_min_key(node: BinarySearchTreeNode) -> int:
    if node.left is None:
        return node.key

    return get_min_key(node.left)


if __name__ == "__main__":
    node = BinarySearchTreeNode(5)
    insert(node, 3)
    insert(node, 15)
    insert(node, 26)
    insert(node, 7)
    insert(node, 1)
    insert(node, 2)
    insert(node, 9)

    print("search key for 5")
    print(search(node, 5))

    print("search key for 15")
    print(search(node, 15))

    print("search key for 100")
    print(search(node, 100))

    print("delete the key 3")
    print(delete(node, 3))

    print("search key for 3")
    print(search(node, 3))

    print("delete the key 2")
    print(delete(node, 2))

    print("search key for 2")
    print(search(node, 2))
