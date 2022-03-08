class Node():
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def inorder(self):
        if self.item:
            if self.left:
                self.left.inorder()

            print(f"{self.item} -> ", end='')

            if self.right:
                self.right.inorder()
        return

    def preorder(self):
        if self.item:
            print(f"{self.item} -> ", end='')

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()
        return

    def postorder(self):
        if self.item:
            if self.left:
                self.left.inorder()

            if self.right:
                self.right.inorder()

            print(f"{self.item} -> ", end='')
        return


if __name__ == "__main__":
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    
    print("inorder")
    node.inorder()
    print("\npreorder")
    node.preorder()
    print("\npostorder")
    node.postorder()
