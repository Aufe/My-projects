def is_interesting(number, awesome_phrases):
    x = [number]
    for el in x:
        if el > 97:
            check_1 = str(el) == str(el)[::-1] and len(str(el)) >= 3
            check_2 = el in awesome_phrases and len(str(el)) >= 3
            check_3 = str(el) in "01234567890" and len(str(el)) >= 3
            check_4 = str(el) in "09876543210" and len(str(el)) >= 3
            check_5 = set(str(el)[1:]) == set("0") and len(str(el)) >= 3
            if check_1 or check_2 or check_3 or check_4 or check_5:
                return 2
                
            else:
                x = [el - 2, el - 1, el + 1, el + 2]
                for el in x:
                    check_1 = str(el) == str(el)[::-1] and len(str(el)) >= 3
                    check_2 = el in awesome_phrases and len(str(el)) >= 3
                    check_3 = str(el) in "01234567890" and len(str(el)) >= 3
                    check_4 = str(el) in "09876543210" and len(str(el)) >= 3
                    check_5 = set(str(el)[1:]) == set("0") and len(str(el)) >= 3
                    if check_1 or check_2 or check_3 or check_4 or check_5:
                        return 1
                        
                else:
                    return 0
        else:
            return 0