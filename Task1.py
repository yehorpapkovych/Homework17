def with_index(iterable, start=0):
    for i, item in enumerate(iterable, start=start):
        yield i, item

people = ['Human1', 'Human2', 'Human3']

for i, person in enumerate(people, start=1):
    print(i, person)

for i, person in with_index(people, start=1):
    print(i, person)