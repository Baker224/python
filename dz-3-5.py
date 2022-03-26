import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    jokes_list = []
    for i in range(num):
        ran_nouns = random.choice(nouns)
        ran_adverbs = random.choice(adverbs)
        ran_adjectives = random.choice(adjectives)
        jokes_list.append(f'{ran_nouns} {ran_adverbs} {ran_adjectives}')
    return jokes_list


print(get_jokes(1))
print(get_jokes(2))


