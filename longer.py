"""Longer"""
import math
def longer(rad, aaa, bbb):
    'Longer'
    cir = 2 * math.pi * rad
    rob = 2 * (aaa + bbb)
    bol = cir > rob
    bol_2 = cir == rob
    print((bol * "Circle is longer") + ((not bol) * "Rectangle is longer" * (not bol_2)) + (bol_2 * "Equal"))
    print("%.5f"% abs(cir - rob))
longer(rad=float(input()), aaa=float(input()), bbb=float(input()))
