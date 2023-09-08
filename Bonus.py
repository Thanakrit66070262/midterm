"""bonus"""
def bonus():
    'bonus'
    pay = int(input())
    years = int(input())
    mon = int(input())
    if mon >= 10:
        years += 1
        mon = 0
    if years > 20:
        years = 20
    total = pay * years
    total = min(max(total, 5000), 1000000)
    print(total)
bonus()
