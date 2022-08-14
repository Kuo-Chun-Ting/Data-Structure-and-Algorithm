from data_structure.graph import dfs, bfs


def test_dfs_when_one_vertex():
    # Arrange
    graph = {
        "0": set()
    }

    # Act
    result = dfs(graph, "0")

    # Assert
    expected_result = ["0"]
    assert set(result) == set(expected_result)


def test_dfs():
    # Arrange
    graph = {
        "0": ["1", "2", "3"],
        "1": ["0", "2", "4"],
        "2": ["0", "1", "4"],
        "3": ["0"],
        "4": ["2"]
    }

    # Act
    result = dfs(graph, "0")

    # Assert
    expected_result = ["0", "3", "2", "4", "1"]
    assert result == expected_result


def test_bfs_when_one_vertex():
    # Arrange
    graph = {
        "0": set()
    }

    # Act
    result = bfs(graph, "0")

    # Assert
    expected_result = ["0"]
    assert set(result) == set(expected_result)


def test_bfs():
    # Arrange
    graph = {
        "0": ["1", "2", "3"],
        "1": ["0", "2", "4"],
        "2": ["0", "1", "4"],
        "3": ["0"],
        "4": ["2"]
    }

    # Act
    result = bfs(graph, "0")

    # Assert
    expected_result = ["0", "1", "2", "3", "4"]
    assert set(result) == set(expected_result)
