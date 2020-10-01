def ft_reverse_str(str):
    str1 = ''
    kol = 0
    for i in str:
        kol += 1
    for i in range(kol - 1, -1, -1):
        str1 = str1 + str[i]
    return str1


def ft_equal_reverse(str):
    if ft_reverse_str(str) == str:
        return True
    else:
        return False
