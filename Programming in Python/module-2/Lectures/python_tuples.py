my_tuples = 1, 'strings', 4.5, True, 'strings'

print(type(my_tuples))

print(my_tuples[1])

print(my_tuples.count('strings'))

print(my_tuples.index(4.5))

my_tuples[0] = 5

for x in my_tuples:
    print(x)