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


def num_translate(key_word):
    return num_list.get(key_word)


print(num_translate('one'))
print(num_translate('two'))
print(num_translate('zero'))
print(num_translate('eleven'))
