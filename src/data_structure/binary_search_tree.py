class BinarySearchTreeNode():
    def __init__(self, key):
        self.key: int = key
        self.left: BinarySearchTreeNode = None
        self.right: BinarySearchTreeNode = None


def insert_key(node: BinarySearchTreeNode, key: int) -> BinarySearchTreeNode:
    if node is None:
        raise TypeError("The node should not be None.")

    if key <= node.key:
        if node.left is None:
            node.left = BinarySearchTreeNode(key)
        else:
            insert_key(node.left, key)

    else:
        if node.right is None:
            node.right = BinarySearchTreeNode(key)
        else:
            insert_key(node.right, key)


def search_key(node: BinarySearchTreeNode, key: int)  -> int:
    if key == node.key:
        return node.key

    if key < node.key:
        if node.left is None:
            return None
        else:
            return search_key(node.left, key)
    else:
        if node.right is None:
            return None
        else:
            return search_key(node.right, key)


def delete_key(node: BinarySearchTreeNode, key: int) -> BinarySearchTreeNode:
    if node is None:
        return None

    if key < node.key:
        node.left = delete_key(node.left, key)
    elif key > node.key:
        node.right = delete_key(node.right, key)
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
        node.right = delete_key(node.right, successor_key)
    return node


def get_min_key(node: BinarySearchTreeNode) -> int:
    if node.left is None:
        return node.key

    return get_min_key(node.left)


if __name__ == "__main__":
    node = BinarySearchTreeNode(5)
    insert_key(node, 3)
    insert_key(node, 15)
    insert_key(node, 26)
    insert_key(node, 7)
    insert_key(node, 1)
    insert_key(node, 2)
    insert_key(node, 9)

    print("search key for 5")
    print(search_key(node, 5))

    print("search key for 15")
    print(search_key(node, 15))

    print("search key for 100")
    print(search_key(node, 100))

    print("delete the key 3")
    print(delete_key(node, 3))

    print("search key for 3")
    print(search_key(node, 3))

    print("delete the key 2")
    print(delete_key(node, 2))

    print("search key for 2")
    print(search_key(node, 2))
