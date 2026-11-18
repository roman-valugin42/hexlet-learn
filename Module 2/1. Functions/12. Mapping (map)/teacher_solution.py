from itertools import chain


# BEGIN
def get_children(users):
    def extract_children(user):
        return user.get('children', [])

    children_of_users = map(extract_children, users)
    return list(chain.from_iterable(children_of_users))
# END
