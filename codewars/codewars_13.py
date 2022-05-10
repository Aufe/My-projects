def sort_func(a):
    i = 0
    for j in a:
        i += int(j)
    return i


def sort_str(s):
    return " ".join(sorted(sorted(s.split()), key=lambda x: sum(int(i) for i in x)))
def sort_str_2(s):
    return " ".join(sorted(sorted(s.split()), key=sort_func))

print(sort_str_2("2001 12323 12354 44 51236 83354 8236 90451"))