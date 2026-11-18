from functools import reduce


# BEGIN
def group_by(objects, key):
    def reducer(acc, obj):
        # из каждого объекта берётся значение по ключу
        group_name = obj[key]
        # контейнером группы выступает список
        # метод get возвращает пустой список, если в аккумуляторе ничего нет
        group = acc.get(group_name, [])
        # возвращается новый словарь аккумулятора
        # старый аккумулятор обновляется
        # для текущей группы записывается новый список с данными
        return {**acc, group_name: group + [obj]}

    return reduce(reducer, objects, {})
# END
