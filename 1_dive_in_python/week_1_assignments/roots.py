import sys
from math import sqrt

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

def roots(a, b, c):
    det = b**2 - 4*a*c
    root1 = (-b+sqrt(det))/(2*a)
    root2 = (-b-sqrt(det))/(2*a)
    print(int(root1))
    print(int(root2))


if __name__ == '__main__':
    roots(a, b, c)
