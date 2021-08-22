import pytest

from algorithm.dynamic_programming.knapsack_problem import knapsack_problem


@pytest.mark.parametrize("weights,values,capacity,expected_value", [
    ([1, 2, 4, 2, 5], [5, 3, 5, 3, 2], 10, 11)
])
def test_knapsack_problem(weights, values, capacity, expected_value):
    # Act
    result = knapsack_problem(weights, values, capacity)

    # Assert
    assert result == expected_value
