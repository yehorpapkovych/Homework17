class MyIterable:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        result = self.iterable[self.index]
        self.index += 1
        return result

    def __getitem__(self, index):
        return self.iterable[index]

people = ['Human1', 'Human2', 'Human3']
iterable = MyIterable(people)

for i in iterable:
    print(i)

print(iterable[1])