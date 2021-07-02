from random import choice


def get_jokes(n, no_doubles=True):

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    res = []
    if no_doubles:
        res2 = []
    for _ in range(n):
        tmp = []
        if n > 5:
            no_doubles = False
        if no_doubles:
            new = choice(nouns)
            while new in res2:
                new = choice(nouns)
            tmp.append(new)

            new = choice(adverbs)
            while new in res2:
                new = choice(adverbs)
            tmp.append(new)

            new = choice(adjectives)
            while new in res2:
                new = choice(adjectives)
            tmp.append(new)
        else:
            tmp.append(choice(nouns))
            tmp.append(choice(adverbs))
            tmp.append(choice(adjectives))
        res.append(" ".join(tmp))
        if no_doubles:
            res2.extend(tmp)
    return res


print(get_jokes(n=5))
