"""Home Run"""
def main():
    'Home Run'
    stage = int(input())
    hst = float(input())
    home_run = 0
    for i in range(stage):
        size = float(input())
        if hst > size:
            home_run += 1
    print(home_run)
main()
