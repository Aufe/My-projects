def top_3_words(text):
    for el in text:
        if not (el.isalpha() or el == "'"):
            text = text.replace(el, " ").lower()
    for j in text:
        if not j.isalpha():
            continue
        a = {i: text.split().count(i) for i in text.split()}
        b = sorted(a, key=lambda x: a.get(x))[::-1]
        return b[:3]
    else:
        return []
