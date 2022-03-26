def thesaurus(*names):
    dict_list = dict()
    names = sorted(names)
    for name in names:
        dict_list.setdefault(name[0], [])
        dict_list[name[0]].append(name)
    return dict_list


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Азиз"))
