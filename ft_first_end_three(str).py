def ft_first_end_three(str):
    kol = 0
    for i in str:
        kol += 1
    if kol > 5:
        str1 = str[0] + str[1] + str[2] + str[-3] + str[-2] + str[-1]
        return str1
    elif kol <= 5:
        return str[0] * kol
