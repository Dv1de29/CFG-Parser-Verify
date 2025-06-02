def check_word(word):
    cnt_a = cnt_b = cnt_c = 0
    pass_a = pass_b = False

    for char in word:
        if char == 'a':
            if pass_a == True:
                return False
            cnt_a += 1
            continue
        if char == 'b':
            if pass_b == True:
                return False
            cnt_b += 1
            pass_a = True
            continue
        if char == 'c':
            cnt_c += 1
            pass_b = True
            continue
        return False
    
    if cnt_a != cnt_b or cnt_a != cnt_c or cnt_b != cnt_c:
        return False
    return True
