"""Bad Keyboard"""
def main(txt):
    'Bad Keyboard'
    result = ""
    for i in txt:
        if i == "i":
            result += "o"
        elif i == "o":
            result += "i"
        elif i == "I":
            result += "O"
        elif i == "O":
            result += "I"
        else:
            result += i
    print(result)
main(txt=input())
