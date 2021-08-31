import pytest

from algorithm.dynamic_programming.find_sets_of_numbers_that_add_up_to_n import find_sets_of_num_add_up_to_n


@pytest.mark.parametrize("arr,total,expected_value", [
    ([2, 4, 6, 10], 16, 2),
    ([1, 2, 3, 4, 5], 10, 3),
    ([], 3, 0),
    ([1, 2, 3], 0, 1)
])
def test_knapsack_problem(arr, total, expected_value):
    # Act
    result = find_sets_of_num_add_up_to_n(arr, total)

    # Assert
    assert result == expected_value
