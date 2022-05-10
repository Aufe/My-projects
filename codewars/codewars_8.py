def namelist(names):
    #your code here
    names_2 = [names[name]["name"] for name in range(0, len(names))]
    if len(names) == 0:
        return ""
    elif len(names) == 1:
        return names_2[0]
    else:
        answer = ""
        for el in range(0, len(names_2) - 2):
            answer += names_2[el] + ", "
        return answer + names_2[len(names) - 2] + " & " + names_2[len(names) - 1]

def namelist_2(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

def namelist_3(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

def namelist_4(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]

namelist = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]

print(namelist_4(namelist))

print(", ".join([name["name"] for name in namelist])[::-1].replace(",", "& ", 1)[::-1])
