from itertools import chain


# BEGIN (write your solution here)
def get_children(children: list):
    users = map(lambda user: user["children"], children)
    return list(chain.from_iterable(users))
# END
