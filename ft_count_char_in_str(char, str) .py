def ft_count_char_in_str(char, str):
    kol = 0
    for i in str:
        if char == i:
            kol += 1
    return kol
