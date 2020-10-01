def ft_percent_lower_uppercase(str):
    kolp = int()
    kols = int()
    for i in str:
        if i.isupper():
            kolp += 1
        elif i.islower():
            kols += 1
    return kolp / kols * 100
