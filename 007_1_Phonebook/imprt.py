def EnterUserData():
    id = input('ID - ')
    name1 = input('1st Name - ')
    name2 = input('2nd Name - ')
    phone = input('Phone # - ')
    comm = input('Comments - ')
    with open('Phonebook.txt', 'a') as file:
        file.write(f'{id},{name1},{name2},{phone},{comm}\n')