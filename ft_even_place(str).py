def ft_len(str):
    kol = 0
    for i in str:
        kol += 1
    return kol


def ft_even_place(str):
    str_ = ''
    res = ft_len(str)
    for i in range(res):
        if i % 2 != 0:
            str_ += str[i]
    return str_
