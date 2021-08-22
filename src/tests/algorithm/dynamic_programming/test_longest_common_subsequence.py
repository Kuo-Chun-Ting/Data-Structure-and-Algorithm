import pytest

from algorithm.dynamic_programming.longest_common_subsequence import longest_common_subsequence


@pytest.mark.parametrize("str_a,str_b,expected_value", [
    ("abc", "abc", 3), ("asbsc", "abc", 3), ("abc", "cba", 1), ("abc", "def", 0)
])
def test_longest_common_subsequence(str_a, str_b, expected_value):
    # Act
    result = longest_common_subsequence(str_a, str_b)

    # Assert
    assert result == expected_value
