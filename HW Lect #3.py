print("Task #1")

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    couples = list(zip(boys, girls))
    print("Идеальные пары:")
    for person in couples:
        print(f'{person[0]} и {person[1]}')
else:
    print("Кто-то может остаться без пары!")
print()

print("Task #2")

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]

person = 5

for dishes in cook_book:
    print(dishes)
    print(f'{dishes[0].title()}:')
    for ing, amount, measure in dishes[1]:
        print(f'{ing}, {amount * person}{measure}')
    print()










