def divide_by(a, b):
    return a / b;

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "something went wrong")

# Starter code
items = [1,2,3,4,5]

try:
    item = items[6]
    print(item)
except IndexError as e:
    print(e, "Index 6 not exists.")

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
