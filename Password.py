"""Password"""
import math
def entropy(password):
    'Password'
    intpool = 0
    upperpool = 0
    lowerpool = 0
    printable = 0
    lenth = len(password)
    for i in password:
        if i.isnumeric():
            intpool = 10
        elif i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if i == i.upper():
                upperpool = 26
            elif i == i.lower():
                lowerpool = 26
        else:
            printable = 32
    pool = intpool + upperpool + lowerpool + printable
    e_value = math.log2(pool**lenth)
    e_value = math.floor(e_value)
    print(e_value)
    if e_value >= 128:
        print("Very Strong")
    elif e_value > 60:
        print("Strong")
    elif e_value > 36:
        print("Reasonable")
    elif e_value >= 28:
        print("Weak")
    else:
        print("Very Weak")
entropy(password=input())
