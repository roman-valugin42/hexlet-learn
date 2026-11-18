from functools import reduce


# BEGIN (write your solution here)
def group_by(data, key):
    def reducer(acc, item):
        k = item[key]
        if k not in acc:
            acc[k] = []
        acc[k].append(item)
        return acc

    return reduce(reducer, data, {})
# END
