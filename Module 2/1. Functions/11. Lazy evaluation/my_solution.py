# BEGIN (write your solution here)
def get_fibonacci():
    num_1 = 0
    num_2 = 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2
# END
