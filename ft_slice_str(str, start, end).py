def ft_len(str):
    kol = int()
    for i in str:
        kol += 1
    return kol


def ft_slice_str(str, start, end):
    res_ = ''
    if end >= ft_len(str):
        for i in range(start - 1, ft_len(str)):
            res_ = res_ + str[i]
    else:
        for i in range(start - 1, end):
            res_ = res_ + str[i]
    return res_
