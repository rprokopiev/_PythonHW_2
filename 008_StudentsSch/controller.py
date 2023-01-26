import view as v
import addData as add
import showData as show


def Start():
    a = v.AddGetSelection()
    if a in [0, 2]:
        b = int(
            input('Do you want to clear Students List and Marks List (1-Yes, 2-No) - '))
        if b == 1:
            m_list = open('MarksList.csv', 'w')
            m_list.close()
            st_list = open('StudentsList.csv', 'w')
            st_list.close()
    if a == 0:
        add.EnterStudentsData()
    elif a == 1:
        add.EnterSubject()
    elif a == 2:
        add.EnterMarks()
    elif a == 3:
        show.ShowSudentMarks()
    elif a == 4:
        add.FillStudentsListWithRandomNames(
            int(input('Enter students quantity - ')))
        add.EnterRandMarks(int(input(
            'How many "Marks" runs? \n(each run adds to each student 1 rand mark for each subject)\n')))
        n = int(
            input('Do you want to know average school subject mark? (1 - yes, 2 - no) '))
        if n == 1:
            with open('SubjList.csv', 'r') as file:
                for line in file:
                    print(line)
            show.AverageSchoolSubjMark(int(input('Enter subject ID - ')))
        n = int(
            input('Do you want to know average student mark? (1 - yes, 2 - no) '))
        if n == 1:
            with open('StudentsList.csv', 'r') as file:
                for line in file:
                    print(line)
            show.AverageStudentMark(int(input('Enter Studients ID - ')))
        print('Bye-Bye!')
    else:
        print('Good bye!')
