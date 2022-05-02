from data_structure.avl_tree import (
    AVLTreeNode,
    get_height,
    get_balance_factor,
    insert
)


def test_get_height_when_node_none_then_return_0():
    # Arrange
    root = None

    # Act
    height = get_height(root)

    # Assert
    assert height == 0


def test_get_height_when_1_level_tree_then_return_1():
    # Arrange
    root = None
    root = insert(root, 33)

    # Act
    height = get_height(root)

    # Assert
    assert height == 1


def test_get_height_when_2_level_tree_then_return_2():
    # Arrange
    root = None
    root = insert(root, 33)
    root = insert(root, 13)

    # Act
    height = get_height(root)

    # Assert
    assert height == 2


def test_get_height_when_3_level_tree_then_return_3():
    # Arrange
    root = None
    root = insert(root, 33)
    root = insert(root, 13)
    root = insert(root, 53)
    root = insert(root, 9)

    # Act
    height = get_height(root)

    # Assert
    assert height == 3


def test_get_balance_factor_when_no_child_then_return_0():
    # Arrange
    root = None
    root = insert(root, 33)

    # Act
    balance_factor = get_balance_factor(root)

    # Assert
    assert balance_factor == 0


def test_get_balance_factor_when_1_left_0_right_then_return_1():
    # Arrange
    root = None
    root = insert(root, 33)
    root = insert(root, 13)

    # Act
    balance_factor = get_balance_factor(root)

    # Assert
    assert balance_factor == 1


def test_get_balance_factor_when_1_left_1_right_then_return_0():
    # Arrange
    root = None
    root = insert(root, 33)
    root = insert(root, 13)
    root = insert(root, 53)

    # Act
    balance_factor = get_balance_factor(root)

    # Assert
    assert balance_factor == 0


def test_get_balance_factor_when_0_left_1_right_then_return_negative_1():
    # Arrange
    root = None
    root = insert(root, 33)
    root = insert(root, 53)

    # Act
    balance_factor = get_balance_factor(root)

    # Assert
    assert balance_factor == -1


def test_insert_when_node_none_then_create_new_node_by_key():
    # Arrange
    root = None

    # Act
    root = insert(root, 33)

    # Assert
    assert root.key == 33
    assert root.left is None
    assert root.right is None


def test_insert_when_1_level_tree():
    # Arrange
    root = None
    root = insert(root, 33)

    # Act
    root = insert(root, 13)

    # Assert
    assert root.key == 33
    assert root.left.key == 13


def test_insert_when_2_level_tree():
    # Arrange
    root = None
    root = insert(root, 33)
    root = insert(root, 13)

    # Act
    root = insert(root, 53)

    # Assert
    assert root.key == 33
    assert root.left.key == 13
    assert root.right.key == 53


def test_insert_when_3_level_tree():
    # Arrange
    root = None
    root = insert(root, 33)
    root = insert(root, 13)
    root = insert(root, 53)

    # Act
    root = insert(root, 9)

    # Assert
    assert root.key == 33
    assert root.left.key == 13
    assert root.right.key == 53
    assert root.left.left.key == 9
