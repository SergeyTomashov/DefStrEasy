def ft_len(str):
    kol = int()
    for i in str:
        kol += 1
    return kol


def ft_find_str(str1, str2):
    if str2 not in str1:
        return -1
    else:
        k = 0
        str3 = str1
        while str2 in str3:
            print(str3)
            k += 1
            str3 = ''
            for i in range(ft_len(str1) - k + 1):
                str3 = str3 + str1[i]
        return ft_len(str3) - ft_len(str2) + 1
