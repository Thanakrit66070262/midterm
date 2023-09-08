"""Niwarn World"""
import math
def main(nnn, sss, kkk):
    'Niwarn World'
    print("X: %.1f, Y: %.1f, Z: %.1f"% (xfunc(nnn), yfunc(nnn, sss), zfunc(kkk)))
 
def xfunc(nnn):
    'xfuc'
    xxx = 2 + (math.log2(nnn**2) / (2 * nnn * math.log2(nnn)))
    return xxx
 
def yfunc(nnn, sss):
    'yfunc'
    yyy = (math.sin(math.radians(30)) + math.sqrt(2 * sss)) / (xfunc(nnn) + 3)
    return yyy
 
def zfunc(kkk):
    'zfunc'
    zzz = ((yfunc(kkk, kkk)) ** 2) + ((8456 * ((xfunc(kkk)) ** 4)) / (24 * kkk))
    return zzz
 
main(nnn=float(input()), sss=float(input()), kkk=float(input()))
