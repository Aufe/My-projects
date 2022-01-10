len_size = int(input("Enter the line lenght, please:\n"))

while True:
    if len_size < 35:
        print("You entered the wrong line lenght.")
        len_size = int(input("Try again, please (min the line lenght 35):\n"))
    else:
        break

def lens(l):
    if "\n" in l:
        l.split("\n")
        l = l.split("\n")[0]
        return l
    else:
        if l[-1] == (" "):
            return l[:-1]
        else:
            return lens(l[:-1])

def len_correct(lens, len_size):
    s = lens.split(' ')
    a_s = ''.join(s)
    if len(s) > 1:
        while len(a_s) < len_size:    
            for el in range(len(s) - 1):
                if len(a_s) < len_size:
                    s[el] += " "
                else:
                    break
                a_s = ''.join(s)
    return a_s + "\n"

def words(text):
    t = text.replace("\n", " ")
    p = '''!#$%&'()*"+,−-./:;<=>…?@[\]^_`{|}~'''
    t = "".join(el for el in t if el not in p)
    w = {}
    for el in t.lower().split(" "):
        if el in w:
            w[el] += 1
        else:
            w[el] = 1
    return(w)  

b = 0
with open("text.txt", encoding="utf-8") as text:
    t = text.read()
    l = t[b:len_size + 1]
    with open("new_text.txt", "w", encoding="utf-8") as new_text:
        new_text.write(len_correct(lens(l), len_size))
        while True:
            b += len(lens(l)) + 1
            l = t[b:b + len_size + 1]
            if len(l) <= len_size:
                new_text.write(len_correct(l, len_size))
                break
            new_text.write(len_correct(lens(l), len_size))
    with open("text_words.txt", "w", encoding="utf-8") as t_words:
        d = words(t)
        for k, v in d.items():
            wr = f"{k} : {v}\n"
            t_words.write(wr)
