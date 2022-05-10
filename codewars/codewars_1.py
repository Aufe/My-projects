def to_camel_case(text):
    #your code here
    if len(text) == 0:
        return text
    text = text.replace("-", " ").replace("_", " ").split()
    return text[0] + ''.join(i.capitalize() for i in text[1:])

print(to_camel_case("the_stealth_warrior"))


