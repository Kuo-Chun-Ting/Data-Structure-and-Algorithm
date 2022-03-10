import pytest

from data_structure.tree import Node, inorder, is_full, preorder, postorder


def test_inorder():
    # Arrange
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)

    # Act
    result = inorder(node)

    # Assert
    assert result == [4, 2, 5, 1, 3]


def test_preorder():
    # Arrange
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)

    # Act
    result = preorder(node)

    # Assert
    assert result == [1, 2, 4, 5, 3]


def test_postorder():
    # Arrange
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)

    # Act
    result = postorder(node)

    # Assert
    assert result == [4, 5, 2, 3, 1]


def test_if_full_when_root_none_return_true():
    # Arrange
    node = None

    # Act
    result = is_full(node)

    # Assert
    assert result == True


def test_if_full_when_only_root_return_true():
    # Arrange
    node = Node(1)

    # Act
    result = is_full(node)

    # Assert
    assert result == True


def test_if_full_when_full_return_true():
    # Arrange
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)

    # Act
    result = is_full(node)

    # Assert
    assert result == True


def test_if_full_when_not_full_return_false():
    # Arrange
    node = Node(1)
    node.left = Node(2)

    # Act
    result = is_full(node)

    # Assert
    assert result == False
