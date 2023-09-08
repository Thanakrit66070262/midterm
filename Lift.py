"""Lift"""
def main():
    'Lift'
    total = 0
    safe = False
    people = int(input())
    limit = float(input())
    if people == 0:
        safe = True
    for _ in range(people):
        age = int(input())
        wei = float(input())
        total += wei
        if age >= 12:
            safe = True
    if total > limit:
        safe = False
    print((safe * "Safe") + (not safe) * "Not Safe")
main()
