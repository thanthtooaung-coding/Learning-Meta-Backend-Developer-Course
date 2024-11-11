set_a = {1, 2, 3, 4, 5, "koko"}

set_a.add(6)

set_a.remove("koko")

set_a.discard(5)

print(set_a)

set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b))

print(set_a | set_b)

set_c = set_a.union(set_b)

print(set_c)

set_d = set_a | set_b

print(set_d)

print(set_c.intersection(set_a))

print(set_c & set_a)

print(set_c.difference(set_a))

print(set_c - set_a)

print(set_a.symmetric_difference(set_b))

print(set_a ^ set_b)

print(set_a[0])