import sys


def findMax(n):
    """Finds minimum possible base that a number n could be and returns
    a list containing formatted version of that base for printing, and the base"""
    maxe = max([int(x) for x in str(n)]) + 1
    return [str("(" + str(maxe) + "-10)"), maxe]


def convert(n, b):
    """Converts an integer n from decimal to base b"""
    if b == 1:
        return '1' * n
    if n == 0:
        return ''
    for i in range(b):
        if n % b == i:
            return convert(n//b, b) + str(i)


def deconvert(n, b):
    """Converts an integer from base b to decimal"""
    num = 0
    n = str(n)[::-1]
    if len(n) == 0:
        return 0
    for i in range(len(n)):
        num += (int(n[i])) * (b ** i)
    return num


def selection(f):
    """loop for selecting options"""
    while True:
        if f:
            print("Convert Same Number (1) Convert Different Number (2) End Program (3)")
            p = input()
            if p == '1':
                return 1
            elif p == '3':
                sys.exit()
            elif p == '2':
                return 2
            else:
                print("ERROR,", p, "is not a valid option")
                continue
        else:
            print("Convert Number (1) End Program (2)")
            p = input()
            if p == '1':
                return 2
            elif p == '2':
                sys.exit()
            else:
                print("ERROR,", p, "is not a valid option")
                continue


def getVal(m, numby):
    """Gets base and number values inputted and checks that they are valid for the program"""
    if m == 1:  # Defining Base
        while True:
            print("Base" + findMax(numby[0])[0] + ":")
            imp = input()
            try:
                imp = int(imp)
                if imp in range(findMax(numby[0])[1], 11):
                    return imp
                else:
                    print("Error,", imp, "is not a valid option")
            except:
                print("Error,", imp, "is not a valid option")
                continue
    if m == 2:  # Conversion Base
        while True:
            print("Select a Base(1-10) to Convert", form(numby, 2), "to")
            imp = input()
            try:
                imp = int(imp)
                if imp in range(1, 11):
                    return imp
                else:
                    print("Error,", imp, "is not a valid option")
            except:
                print("Error,", imp, "is not a valid option")
                continue
    if m == 3:  # Get Number
        while True:
            print("Number(int):")
            imp = input()
            try:
                imp = int(imp)
                return imp
            except:
                print("Error,", imp, "is not a valid option")
                continue


def form(numby, variable):
    """Formats number and base"""
    if variable == 1:
        return str(str(numby[0]) + " |" + str(numby[1]) + "|")
    else:
        return str(str(numby[0]) + " |" + str(numby[2]) + "|")


print("Welcome to Number Converter \nPress Enter to Continue")
input()
numby = [0, 10, 10]
# numby(Number, Number Base, Previous Number Base)
f = False
while True:
    m = selection(f)
    if m == 1:  # Convert Same Number
        numby[2] = numby[1]
        numby[1] = getVal(2, numby)
        print(form(numby, 2), "Converted to base", numby[1], "equals:")
        numby[0] = int(convert(deconvert(numby[0], numby[2]), numby[1]))
        print(form(numby, 1))
    if m == 2:  # Convert Different Number
        f = True
        numby[0] = getVal(3, numby)
        numby[2] = getVal(1, numby)
        numby[1] = getVal(2, numby)
        print(form(numby, 2), "Converted to base", numby[1], "equals:")
        numby[0] = int(convert(deconvert(numby[0], numby[2]), numby[1]))
        print(form(numby, 1))
