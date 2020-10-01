def ft_first_end_three(str):
    kol = int()
    for i in str:
        kol += 1
    if kol > 5:
        print(str[0], str[1], str[2], str[-3], str[-2], str[-1], sep='')
    elif kol <= 5:
        print(str[0] * kol)
