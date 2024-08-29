# '' *args will enable you pass any number of arguments.. Only key ''
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(9,10,11))


# '' *args will enable you pass any number of arguments.. Key Value ''
def sum_of(**kwargs):
    sum = 0
    for k, x in kwargs.items():
        sum += x
    return sum

print(sum_of(cake = 9, coffee = 10, tea = 5.09))