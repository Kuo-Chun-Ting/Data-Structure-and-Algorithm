class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


class LinkedList:

    def __init__(self):
        self.head: Node = None

    def insert_at_beginning(self, data: int):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data: int):
        if prev_node is None:
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, data: int):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node

    def delete(self, data: int):
        if self.head.data == data:
            self.head = self.head.next
            return

        curr_node = self.head
        next_node = curr_node.next

        while(next_node.data != data):
            curr_node = next_node
            next_node = next_node.next

        curr_node.next = next_node.next
        next_node = None

    def search_data(self, data: int) -> bool:
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next

        return False

    def sort(self):
        if not self.head:
            return

        curr_node = self.head
        while curr_node.next:
            i = self.head

            while i.next:
                if i.data > i.next.data:
                    i.data, i.next.data = i.next.data, i.data
                i = i.next

            curr_node = curr_node.next

    def print_nodes(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(6)
    linked_list.print_nodes()
    print(linked_list.search_data(1))
    print(linked_list.search_data(2))
    print(linked_list.search_data(3))
    print(linked_list.search_data(7))
