def in_range(start, end, step=1):
    current = start
    while current<end:
        yield current
        current += step

people = ['Human1', 'Human2', 'Human3']

for i in range(0, len(people), 2):
    print(people[i])

for i in in_range(0, len(people), 2):
    print(people[i])