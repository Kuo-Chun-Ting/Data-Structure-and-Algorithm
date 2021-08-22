def knapsack_problem(weights, values, capacity):
    print(f'w {weights}')
    print(f'v {values}')

    stuff_count = len(weights)
    ref_table = init_ref_table(stuff_count, capacity)
    print_ref_table(ref_table)

    max_value = find_max_value(
        weights, values, capacity, stuff_count-1, ref_table)
    print(f'The max value is {max_value}')
    print_ref_table(ref_table)

    return max_value


def init_ref_table(stuff_count, capacity):
    reference = []

    for i in range(0, stuff_count):
        reference.append([-1] * capacity)
    return reference


def print_ref_table(ref_table):
    l = len(ref_table)
    for row in range(len(ref_table)-1, -1, -1):
        print(ref_table[row])


def find_max_value(weights, values, capacity, checking_index, ref_table):
    if ref_table[checking_index][capacity-1] != -1:
        return ref_table[checking_index][capacity-1]

    if checking_index == -1 or capacity == 0:
        return 0
    elif weights[checking_index-1] >= capacity:
        result = find_max_value(weights, values, capacity,
                                checking_index-1, ref_table)
    else:
        not_take_checking_value = find_max_value(
            weights, values, capacity, checking_index-1, ref_table)
        take_checking_value = values[checking_index] + find_max_value(
            weights, values, capacity-weights[checking_index], checking_index-1, ref_table)
        result = not_take_checking_value if not_take_checking_value > take_checking_value else take_checking_value

        if take_checking_value > not_take_checking_value:
            print(checking_index)

    ref_table[checking_index][capacity-1] = result
    return result


if __name__ == "__main__":
    weights = [1, 2, 4, 2, 5]
    values = [5, 3, 5, 3, 2]
    capacity = 10

    max_val = knapsack_problem(weights, values, capacity)
