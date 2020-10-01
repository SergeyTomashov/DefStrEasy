def ft_percent_lower_uppercase(str):
    str1 = 'ABCDEFGIJKLMNOPQRSTUVWXYZЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ'
    str2 = 'abcdefgijklmnopqrstuvwxyzйцукенгшщзхъфывапролджэёячсмитьбю'
    kolp = int()
    kols = int()
    for i in str:
        if i in str1:
            kolp += 1
        elif i in str2:
            kols += 1
    return kols / kolp * 100
