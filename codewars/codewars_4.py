def duplicate_count(text):
    dict = {}
    num = 0
    text = text.lower()
    list = [sym for sym in text]
    if len(list) == len(set(list)):
        return 0
    else:
        for el in list:
            dict[el] = dict.get(el, 0) + 1
    for elem in dict:
        if dict[elem] != 1:
            num += 1
    return num

duplicate_count("texTexsad1123")

h = "textexttt"

print(len(set([el for el in h.lower() if h.lower().count(el) > 1])))