import sys

digit_string = sys.argv[1]

def sum(digit_string):
    sum = 0
    for i in digit_string:
        sum += int(i)
    return sum

if __name__ == '__main__':
    print(sum(digit_string))
