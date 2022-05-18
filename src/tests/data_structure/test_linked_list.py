from data_structure.linked_list import LinkedList


def test_insert_at_beginning_when_insert_one_data():
    # Arrange
    linked_list = LinkedList()

    # Act
    linked_list.insert_at_beginning(1)

    # Assert
    assert linked_list.head.data == 1


def test_insert_at_beginning_when_insert_two_data():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_beginning(1)

    # Act
    linked_list.insert_at_beginning(2)

    # Assert
    assert linked_list.head.data == 2
    assert linked_list.head.next.data == 1


def test_insert_at_beginning_when_insert_three_data():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)

    # Act
    linked_list.insert_at_beginning(3)

    # Assert
    assert linked_list.head.data == 3
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 1


def test_insert_at_end_when_insert_one_data():
    # Arrange
    linked_list = LinkedList()

    # Act
    linked_list.insert_at_end(1)

    # Assert
    assert linked_list.head.data == 1


def test_insert_at_end_when_insert_two_data():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)

    # Act
    linked_list.insert_at_end(2)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2


def test_insert_at_end_when_insert_three_data():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)

    # Act
    linked_list.insert_at_end(3)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3


def test_insert_after_when_insert_after_middle_node():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)

    # Act
    node_with_two = linked_list.head.next
    linked_list.insert_after(node_with_two, 4)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 4
    assert linked_list.head.next.next.next.data == 3


def test_insert_after_when_insert_after_last_node():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)

    # Act
    node_with_two = linked_list.head.next
    linked_list.insert_after(node_with_two, 3)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3


def test_delete_when_delete_fist_node():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)

    # Act
    linked_list.delete(1)

    # Assert
    assert linked_list.head.data == 2
    assert linked_list.head.next.data == 3


def test_delete_when_delete_middle_node():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)

    # Act
    linked_list.delete(2)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 3


def test_delete_when_delete_last_node():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)

    # Act
    linked_list.delete(3)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2


def test_search_data_when_data_existing_then_return_true():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)

    # Act
    is_existing = linked_list.search_data(3)

    # Assert
    assert is_existing == True


def test_search_data_when_data_not_existing_then_return_false():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)

    # Act
    is_existing = linked_list.search_data(4)

    # Assert
    assert is_existing == False


def test_search_data_when_data_not_existing_then_return_false():
    # Arrange
    linked_list = LinkedList()
    linked_list.insert_at_end(-2)
    linked_list.insert_at_end(0)
    linked_list.insert_at_end(11)
    linked_list.insert_at_end(-9)
    linked_list.insert_at_end(45)

    # Act
    is_existing = linked_list.sort()

    # Assert
    assert linked_list.head.data == -9
    assert linked_list.head.next.data == -2
    assert linked_list.head.next.next.data == 0
    assert linked_list.head.next.next.next.data == 11
    assert linked_list.head.next.next.next.next.data == 45
