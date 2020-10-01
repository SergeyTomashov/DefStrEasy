def ft_len(str):
    kol = int()
    for i in str:
        kol += 1
    return kol


def ft_cmp_str(str1, str2, num):
    res_ = ''
    for i in range(num - 1):
        res_ = res_ + str1[i]
    res_ += str2
    for i in range(num - 1, ft_len(str1)):
        res_ += str1[i]
    return res_
