import view as v
import imprt as imp
import export as exp

def Button():
    a = v.ImpExpSelection()
    if a == 1:
        b = v.IfFilter()
        if b == 0:
            exp.ShowBookData()
        elif b == 1:
            exp.ShowBookNamesOnly()
        else:
            exp.ShowBookFiltByName()
    else:
        imp.EnterUserData()

