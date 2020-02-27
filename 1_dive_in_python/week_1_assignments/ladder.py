import sys

digit_string = sys.argv[1]

def ladder(digit_string):
    n = range(1,int(digit_string)+1)
    for i in n:
        print(' '*(int(digit_string)-i) + '#'*i)


if __name__ == '__main__':
    ladder(digit_string)
