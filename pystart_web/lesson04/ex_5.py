from functools import reduce

print(reduce(lambda *args: sum(args), [x for x in range(100, 1001, 2)]))
