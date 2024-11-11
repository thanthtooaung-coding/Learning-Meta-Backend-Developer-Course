with open('test.txt', mode = 'r') as file:
    data = file.readline()

    print(data)


try:
    with open('sample/newfile.txt', 'a') as file:
        file.writelines(["\nThis is a new file created!2", "\nThis is another line to be added."])
except FileNotFoundError as e:
    print("ERROR", e)