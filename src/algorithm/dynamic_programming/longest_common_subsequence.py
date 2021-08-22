def longest_common_subsequence(p, q):
    ref_table = init_ref_table(len(p), len(q))
    lcs = ls(p, q, ref_table)
    print_ref_table(ref_table)
    return lcs


def init_ref_table(n, m):
    ref_table = []
    for i in range(n):
        ref_table.append([None]*m)
    return ref_table


def print_ref_table(ref_table):
    l = len(ref_table)
    for row in range(0, len(ref_table)):
        print(ref_table[row])


def ls(str_p, str_q, ref_table):
    p_len = len(str_p)
    q_len = len(str_q)

    if p_len == 0 or q_len == 0:
        return 0
    elif ref_table[p_len-1][q_len-1] != None:
        return ref_table[p_len-1][q_len-1]
    elif str_p[-1] == str_q[-1]:
        result = 1 + ls(str_p[:p_len-1], str_q[:q_len-1], ref_table)
    elif str_p[-1] != str_q[-1]:
        res1 = ls(str_p, str_q[:q_len-1], ref_table)
        res2 = ls(str_p[:p_len-1], str_q, ref_table)
        result = res1 if res1 > res2 else res2

    ref_table[p_len-1][q_len-1] = result
    return result


if __name__ == "__main__":
    str_p = "aeb"
    str_q = "ab"

    lcs = longest_common_subsequence(str_p, str_q)
    print(lcs)
