def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result

a = ["zone", "abigail", "theta", "form", "libe", "zas"]

k = 1
c = 0
d = ""
e = []
while c + k < len(a) + 1:
    for i in range(c, c + k):
        d += a[i]
    else:
        c += 1
        e.append(d)
        d = ""
print(e)
print(max(e, key=len))