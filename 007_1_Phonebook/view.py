def ImpExpSelection():
    stion = int(input('Select 0 to add data and 1 - for export: '))
    while stion not in [0, 1]:
        stion = int(input('Select 0 to add data and 1 - for export: '))
    return stion


def IfFilter():
    stion = int(input(
        'Select: \n0 - to see book as it is \n1 - Names only,\n2 - book filtered by 1st Names\n'))
    while stion not in [0, 1, 2]:
        stion = int(input(
            'Select: \n0 - to see book as it is \n1 - Names only,\n2 - book filtered by 1st Names\n'))
    return stion