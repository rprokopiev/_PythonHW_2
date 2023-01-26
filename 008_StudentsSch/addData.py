def RandNameCreator():
    import random as r
    randName1_list = ['Phoeby', 'Joey', 'Rachel', 'Ross', 'Chandler', 'Monica']
    randName2_list = ['Green', 'Tribbiani',
                      'Buffay', 'Geller', 'Bing', 'Geller']
    NewName1 = r.choice(randName1_list)
    NewName2 = r.choice(randName2_list)
    return f'{NewName1},{NewName2}'


def FillStudentsListWithRandomNames(qty):
    f = open('StudentsList.csv', 'w')
    f.close()
    with open('StudentsList.csv', 'w') as file:
        for i in range(1, qty+1):
            if i == 1:
                file.writelines(f'{i},{RandNameCreator()}')
            else:
                file.writelines(f'\n{i},{RandNameCreator()}')


def EnterRandMarks(n):
    f = open('MarksList.csv', 'w')
    f.close()
    import random as r
    SubjIdList = [i.split(',')[0]
                  for i in open('SubjList.csv').read().split('\n')]
    for i in range(0, n):
        with open('StudentsList.csv', 'r') as file:
            for line in file:
                a = line.split(',')[0]
                with open('MarksList.csv', 'a') as file:
                    for i in range(0, len(SubjIdList)):
                        file.write(f'{a},')
                        file.write(f'{SubjIdList[i]},')
                        file.write(f'{r.randint(2,5)}\n')


def EnterStudentsData():
    id = input('ID - ')
    name1 = input('1st Name - ')
    name2 = input('2nd Name - ')
    with open('StudentsList.csv', 'a') as file:
        file.write(f'\n{id},{name1},{name2}')


def EnterSubject():
    id = input('ID - ')
    subjName = input('Subject - ')
    with open('SubjList.csv', 'a') as file:
        file.write(f'\n{id},{subjName}')


def EnterMarks():
    with open('StudentsList.csv', 'r') as file:
        studentsList = [line.split(',') for line in file]
    with open('SubjList.csv', 'r') as file:
        subjectList = [line.split(',') for line in file]
    print('Students list: ')
    for i in range(0, len(studentsList)):
        print(studentsList[i])
    stid = input('Enter Students ID - ')
    print('Subject list: ')
    for i in range(0, len(subjectList)):
        print(subjectList[i])
    subid = input('Enter Subject ID - ')
    mark = int(input('Enter Mark - '))
    with open('MarksList.csv', 'a') as file:
        file.write(f'\n{stid},{subid},{mark}')
