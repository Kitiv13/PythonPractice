print("Task #1")
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
# ver #1
for d in geo_logs:
    for keys, value in d.items():
        if 'Россия' in value:
            print(list(d.items()))
# ver #1
# geo_list = []
# for d in geo_logs:
#     for value in d.values():
#         if 'Россия' in value:
#             geo_list.append(d)
# print(geo_list)
# print()

print("Task #2")

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

ids_value = list(ids.values())
ids_set = set([x for row in ids_value for x in row])
print(list(ids_set))

print('Task #3')
queries = [
       'смотреть сериалы онлайн',
       'новости спорта',
       'афиша кино',
       'курс доллара',
       'сериалы этим летом',
       'курс по питону',
       'сериалы про спорт'
]

dict_queries = {}
list_words = []
for el in queries:
    res = (len(el.split()))
    list_words.append(res)
for q in list_words:
    if q in dict_queries:
        dict_queries[q] += 1
    else:
        dict_queries[q] = 1

count = sum(dict_queries.values())
for k, v in dict_queries.items():
    print(f'Поисковыих запросов из {k} слов - {100/count*v:.1f} %')

print("Task #4")
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
sort_stats = sorted(stats.items(), key=lambda x: -x[1])
print(f'Канал с максимальным объемом продаж - {sort_stats[0][0]}')

print("Task #5")
my_list = ['2018-01-01', 'yandex', 'cpc', 100]
my_dict = {my_list[-2]: my_list[-1]}
for el in my_list[::-1][2:]:
    my_dict = {el: my_dict}
print(my_dict)

