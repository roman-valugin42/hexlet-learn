from itertools import chain


# BEGIN (write your solution here)
def get_girl_friends(users: list):
    friends = map(lambda user: user['friends'], users)
    all_friends = chain.from_iterable(friends)
    girls = filter(lambda all_friends: all_friends['gender'] == 'female', all_friends)
    return list(girls)
# END
