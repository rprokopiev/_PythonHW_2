def AddGetSelection():
    stion = int(input(
        'Select: \n0 - to add Students name, \
        \n1 - to add Subject name, \
        \n2 - to add Mark, \
        \n3 - to see student marks, \
        \n4 - for random fill, \
        \n5 - exit. \n'))
    while stion not in [0, 1, 2, 3, 4, 5]:
        stion = int(input(
            'Select: \n0 - to add Students name, \
                \n1 - to add Subject name, \
                \n2 - to add Mark, \
                \n3 - to see student marks, \
                \n4 - for random fill, \
                \n5 - exit. \n'))
    return stion
