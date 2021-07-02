def thesaurus(*args):
    d = dict()
    for name in args:
        s = name[0]
        if s not in d:
            d[s] = []
        d[s].append(name)
    return d


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
