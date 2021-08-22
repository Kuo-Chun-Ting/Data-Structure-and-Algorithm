def longest_common_subsequence(str_p, str_q):
    len_p = len(str_p)
    len_q = len(str_q)

    ref_table = init_ref_table(len_p, len_q)
    ref_table = fill_out_ref_table(str_p, str_q, ref_table)

    print_ref_table(ref_table)
    return ref_table[len_p][len_q]


def init_ref_table(row, column):
    ref_table = []
    for i in range(row+1):
        ref_table.append([None]*(column+1))

    for i in range(row+1):
        ref_table[i][0] = 0
    for i in range(column+1):
        ref_table[0][i] = 0

    return ref_table


def fill_out_ref_table(str_p, str_q, ref_table):
    for i in range(len(str_p)):
        for j in range(len(str_q)):
            if str_p[i] == str_q[j]:
                ref_table[i+1][j+1] = 1 + ref_table[i][j]
            else:
                ref_table[i+1][j+1] = max(ref_table[i+1][j], ref_table[i][j+1])
    return ref_table


def max(val1, val2):
    return val1 if val1 > val2 else val2


def print_ref_table(ref_table):
    l = len(ref_table)
    for row in range(0, len(ref_table)):
        print(ref_table[row])


if __name__ == "__main__":
    str_p = "aeb"
    str_q = "ab"

    lcs = longest_common_subsequence(str_p, str_q)
    print(lcs)
