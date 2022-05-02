import pytest

from data_structure.binary_search_tree import (
    BinarySearchTreeNode,
    insert,
    search,
    delete,
    delete,
    get_min_key
)


def test_insert_when_node_none_then_create_new_node_by_key():
    # Arrange
    root = None

    # Act
    root = insert(root, 1)

    # Assert
    assert root.key == 1
    assert root.left is None
    assert root.right is None


def test_insert_when_1_level_tree():
    # Arrange
    root = None
    root = insert(root, 5)

    # Act
    root = insert(root, 1)

    # AssertÏ
    assert root.key == 5
    assert root.left.key == 1


def test_insert_when_2_level_tree():
    # Arrange
    root = None
    root = insert(root, 5)
    root = insert(root, 1)

    # Act
    root = insert(root, 2)

    # AssertÏ
    assert root.key == 5
    assert root.left.key == 1
    assert root.left.right.key == 2


def test_insert_when_3_level_tree():
    # Arrange
    root = None
    root = insert(root, 5)
    root = insert(root, 1)
    root = insert(root, 2)

    # Act
    root = insert(root, 4)

    # Assert
    assert root.key == 5
    assert root.left.key == 1
    assert root.left.right.key == 2
    assert root.left.right.right.key == 4


def test_get_min_key_when_1_node():
    # Arrange
    min_key = 5
    root = BinarySearchTreeNode(min_key)

    # Act
    result = get_min_key(root)

    # Assert
    assert result == min_key


def test_get_min_key_when_5_node():
    # Arrange
    min_key = 1
    root = BinarySearchTreeNode(min_key)
    root.right = BinarySearchTreeNode(2)
    root.right.right = BinarySearchTreeNode(3)
    root.right.right.right = BinarySearchTreeNode(4)
    root.right.right.right.right = BinarySearchTreeNode(5)

    # Act
    result = get_min_key(root)

    # Assert
    assert result == min_key


def test_search_when_key_not_existing_then_return_none():
    # Arrange
    node = BinarySearchTreeNode(5)
    not_existing_key = 7

    # Act
    searched_key = search(node, not_existing_key)

    # Assert
    assert searched_key == None


def test_search_when_key_at_middle_and_existing_then_return_it():
    # Arrange
    key_to_be_searched = 7
    node = BinarySearchTreeNode(5)
    insert(node, 1)
    insert(node, key_to_be_searched)
    insert(node, 2)

    # Act
    searched_key = search(node, key_to_be_searched)

    # Assert
    assert searched_key == key_to_be_searched


def test_search_when_key_at_leaf_and_existing_then_return_it():
    # Arrange
    key_to_be_searched = 2
    node = BinarySearchTreeNode(5)
    insert(node, 1)
    insert(node, 7)
    insert(node, 2)

    # Act
    searched_key = search(node, key_to_be_searched)

    # Assert
    assert searched_key == key_to_be_searched


def test_delete_when_root_is_None_then_return_None():
    # Arrange
    root = None
    key = 1

    # Act
    result = delete(root, key)

    # Assert
    assert result == None


def test_delete_when_deleted_node_is_leaf_then_do_nothing():
    # Arrange
    key_to_be_deleted = 2

    node = BinarySearchTreeNode(5)
    insert(node, key_to_be_deleted)

    # Act
    result = delete(node, key_to_be_deleted)

    # Assert
    assert result.key == 5
    assert result.left == None


def test_delete_when_deleted_node_has_only_one_child_then_get_child_as_successor():
    # Arrange
    key_to_be_deleted = 2
    deleted_nodes_child_key = 1

    node = BinarySearchTreeNode(5)
    insert(node, key_to_be_deleted)
    insert(node, deleted_nodes_child_key)

    # Act
    result = delete(node, key_to_be_deleted)

    # Assert
    assert result.key == 5
    assert result.left.key == deleted_nodes_child_key
    assert result.left.left == None


def test_delete_when_deleted_node_has_two_children_then_get_right_nodes_min_key_as_successor():
    # Arrange
    key_to_be_deleted = 5
    deleted_nodes_right_nodes_min_key = 7
    node = BinarySearchTreeNode(10)
    insert(node, key_to_be_deleted)
    insert(node, 1)
    insert(node, 8)
    insert(node, deleted_nodes_right_nodes_min_key)
    insert(node, 9)

    # Act
    result = delete(node, 5)

    # Assert
    assert result.key == 10
    assert result.left.key == deleted_nodes_right_nodes_min_key
    assert result.left.right.key == 8
    assert result.left.right.left == None
    assert result.left.right.right.key == 9
