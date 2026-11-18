# get_children()

Реализуйте в файле `src/solution.py` функцию `get_children()`, которая принимает на вход список пользователей и возвращает плоский список их детей. Дети каждого пользователя хранятся в виде списка в ключе `'children'`.

## Пример использования:

```python
from solution import get_children

users = [
    {
        'name': 'Tirion',
        'children': [
            {'name': 'Mira', 'birthday': '1983-03-23'},
        ],
    },
    {'name': 'Bronn', 'children': []},
    {
        'name': 'Sam',
        'children': [
            {'name': 'Aria', 'birthday': '2012-11-03'},
            {'name': 'Keit', 'birthday': '1933-05-14'},
        ],
    },
    {
        'name': 'Rob',
        'children': [
            {'name': 'Tisha', 'birthday': '2012-11-03'},
        ],
    },
]

print(get_children(users))
# => [
# =>     {'name': 'Mira', 'birthday': '1983-03-23'},
# =>     {'name': 'Aria', 'birthday': '2012-11-03'},
# =>     {'name': 'Keit', 'birthday': '1933-05-14'},
# =>     {'name': 'Tisha', 'birthday': '2012-11-03'},
# => ]

print(get_children([]))
# => []
```

## Подсказки

- `chain.from_iterable()`
- `map()` и `chain.from_iterable()` возвращают итераторы, а функция должна вернуть список. Список из итератора получается вызовом `list()`
