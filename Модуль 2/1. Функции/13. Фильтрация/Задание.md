# get_girl_friends()

Реализуйте в файле `src/solution.py` функцию `get_girl_friends()`, которая принимает единственный аргумент, список пользователей, и возвращает плоский список подруг всех пользователей (без сохранения ключей). Друзья каждого пользователя хранятся в виде списка в ключе `'friends'`. Пол записан в словаре каждого друга по ключу `'gender'` и может принимать значения `'male'` или `'female'`. У самих пользователей ключа `'gender'` нет, поэтому фильтруется список друзей.

## Пример использования:

```python
from solution import get_girl_friends

users = [
    {
        'name': 'Tirion',
        'friends': [
            {'name': 'Mira', 'gender': 'female'},
            {'name': 'Ramsey', 'gender': 'male'},
        ],
    },
    {'name': 'Bronn', 'friends': []},
    {
        'name': 'Sam',
        'friends': [
            {'name': 'Aria', 'gender': 'female'},
            {'name': 'Keit', 'gender': 'female'},
        ],
    },
    {
        'name': 'Rob',
        'friends': [
            {'name': 'Taywin', 'gender': 'male'},
        ],
    },
]

print(get_girl_friends(users))
# => [
# =>     {'name': 'Mira', 'gender': 'female'},
# =>     {'name': 'Aria', 'gender': 'female'},
# =>     {'name': 'Keit', 'gender': 'female'},
# => ]

print(get_girl_friends([]))
# => []
```

## Подсказки

- Так как нам нужны только друзья, то можно применить функцию `map()` и получить список друзей, который затем будет фильтроваться
- Одно из решений задачи предполагает использование функции `itertools.chain.from_iterable()` для "выравнивания" списка списков
- `map()`, `filter()` и `chain.from_iterable()` возвращают итераторы, а функция должна вернуть список. Список из итератора получается вызовом `list()`
