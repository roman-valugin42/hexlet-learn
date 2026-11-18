from itertools import chain


# BEGIN
def get_girl_friends(users):
    friends_of_users = map(lambda user: user['friends'], users)
    all_friends = chain.from_iterable(friends_of_users)
    return list(
        filter(lambda friend: friend['gender'] == 'female', all_friends)
        )
# END
