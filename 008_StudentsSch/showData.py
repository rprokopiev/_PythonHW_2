def ShowSudentMarks():
    SubjIdList = {i.split(',')[0]: i.split(',')[1]
                  for i in open('SubjList.csv').read().split('\n')}
    print('Students list: ')
    with open('StudentsList.csv', 'r') as file:
        for line in file:
            print(line)
    stid = input('Enter Students ID - ')
    with open('MarksList.csv', 'r') as file:
        for line in file:
            if (line.split(','))[0] == stid:
                a = SubjIdList[line.split(',')[1]]
                b = line.split(',')[2]
                print(f'{a} - {b}')


def AverageSchoolSubjMark(subject_id):
    with open('MarksList.csv', 'r') as file:
        count = 0
        sum = 0
        for line in file:
            if int(line.split(',')[1]) == subject_id:
                count += 1
                sum += int(line.split(',')[2])
        print(round((sum/count), 2))


def AverageStudentMark(student_id):
    with open('MarksList.csv', 'r') as file:
        count = 0
        sum = 0
        for line in file:
            if int(line.split(',')[0]) == student_id:
                count += 1
                sum += int(line.split(',')[2])
        print(round((sum/count), 2))
