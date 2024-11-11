list1 = [1, 2, 3, 4, 5]

print(list1[2])
print(*list1)
print(list1)
print(list1, sep = " ")

list1.insert(len(list1), 6)

print(list1, sep = " ")

list1.append(6)

print(list1, sep = " ")

list1.extend([7, 8, 9])

print(list1, sep = " ")

list1.pop(4)

print(list1, sep = " ")

del list1[5]

print(list1, sep = " ")

list2 = ['A', 'B', 'C']

print(list2[2])

list3 = ['Hello', 1, True, 40.22]

print(list3[2])

list4 = [1, [2, 3, 4], 5, 6]

print(list4[1])