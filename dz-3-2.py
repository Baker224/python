num_list = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}


def num_translate_adv(key_word):
    if key_word == key_word.title():
        return num_list.get(key_word.lower()).title()
    else:
        return num_list.get(key_word)


print(num_translate_adv('One'))
print(num_translate_adv('two'))
print(num_translate_adv('Two'))
print(num_translate_adv('Zero'))
print(num_translate_adv('eleven'))
