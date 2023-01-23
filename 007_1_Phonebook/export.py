def ShowBookData():
    with open('Phonebook.txt', 'r') as file:
        for line in file:
            print(line)


def ShowBookNamesOnly():
    with open('Phonebook.txt', 'r') as file:
        for line in file:
            print((line.split(','))[1], (line.split(','))[2])


def ShowBookFiltByName():
    with open('Phonebook.txt', 'r') as file:
        n = [line.split(',')[1] for line in file]
        n = sorted(n)
    for i in n:
        with open('Phonebook.txt', 'r') as file:
            for line in file:
                if i == line.split(',')[1]:
                    print(line)
