def likes(names):
    # your code here
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "".join(names[0] + " likes this")
    elif len(names) == 2:
        return "".join(names[0] + " and " + names[1] + " like this")
    elif len(names) == 3:
        return "".join(names[0] + ", " + names[1] + " and " + names[2] + " like this")
    else:
        return "".join(names[0] + ", " + names[1] + " and {} others like this").format(len(names) - 2)

def likes_2(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

def likes_3(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)