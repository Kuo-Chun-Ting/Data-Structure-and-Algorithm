def find_sets_of_num_add_up_to_n(arr, n):
    mem = {}
    return dp(arr, n, len(arr)-1, mem)


def dp(arr, total, i, mem):
    key = f"{total}:{i}"
    if mem.get(key) is not None:
        return mem[key]

    if total == 0:
        return 1

    if total < 0:
        return 0

    if i < 0:
        return 0

    if total < arr[i]:
        result = dp(arr, total, i-1, mem)
    else:
        result = dp(arr, total-arr[i], i-1, mem) + dp(arr, total, i-1, mem)

    mem[key] = result
    return result


if __name__ == "__main__":
    arr = [2, 4, 6, 10]
    test = arr[:3]
    n = 16
    count = find_sets_of_num_add_up_to_n(arr, n)
    print(count)
